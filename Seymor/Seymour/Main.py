using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using PrettyGood.Util;
using System.Xml;
using BrightIdeasSoftware;
using System.Text.RegularExpressions;

namespace Seymour
{
    public partial class Main : Form
    {
        ProviderList providers = new ProviderList();
        ChannelList channels;
        Message message;

        public Main()
        {
            App.Setup("codingatlunch", "Seymor", "seymor");
            message = new Message(true);
            InitializeComponent();
            channels = new ChannelList(dFeeds);

            dProgressBytes.Text = "";
            dHtmlLinkInfo.Text = "";

            olvDate.GroupKeyGetter = x => DateClassFunc.Classify(((ItemRead)x).Item.Updated);
            //olvDate.GroupKeyToTitleConverter = x => Classify((DateTime)x).ToString();
            dItems.RowFormatter = x => x.Font = Gui.MakeBold(x.Font, ((ItemRead)x.RowObject).Read ==false);
            dFeeds.RowFormatter = x => x.Font = Gui.MakeBold(x.Font, ((Channel)x.RowObject).unreadCount() != 0);
            dFeeds.CanExpandGetter = x => ((Channel)x).HasSubFeeds;
            dFeeds.ChildrenGetter = x => ((Channel)x).Feeds;
            //dFeeds.DragSource = new SimpleDragSource();
            //dFeeds.DropSink = new RearrangingDropSink(false);
            olvFeedname.AspectPutter = delegate(object channel, object name)
            {
                ((Channel)channel).Title = name.ToString();
                channels.save();
            };

            clearBrowser();
            Text = App.ReadableAppName;
            dNotify.Text = App.ReadableAppName;
            updateCompleteNoFeed();
            providers.add( new Rss.EntryPoint().Providers() );

            channels.OnSelectionUpdated += new Delegates.VoidVoid(channels_OnSelectionUpdated);
            channels.OnNewItem += new ChannelList.ItemAdded(channels_OnNewItem);

            if ("Hejsan urg svejsan tutelut" != ClearHtml("Hejsan <hello arg=\"apa\"><a>urg</a> svejsan</hello> tutelut"))
                throw new Exception("error epic fail unittest");

            channels.load(providers);
            updateFeeds();

            dItems.Sort(olvDate, SortOrder.Descending);
        }

        void channels_OnNewItem(ItemRead item)
        {
            message.notifyNewMessage(item.LocalPath, item.Item.Title, Strings.FirstChars(ClearHtml(item.Item.Summary), 50));
        }

        private string ClearHtml(string html)
        {
            string s = html;
            s = new Regex("<[ a-zA-Z0-9]*([ a-zA-Z0-9]*=\\\"[^\\\"]*\\\")*>").Replace(s, "");
            s = new Regex("</[ a-zA-Z0-9]*>").Replace(s, "");
            return s;
        }

        void channels_OnSelectionUpdated()
        {
            var c = (Channel) dFeeds.SelectedObject;
            updateViewBasedOn(c);
        }

        private void clearBrowser()
        {
            dPostTitle.Text = "";
            dPostTitle.Tag = null;

            dBrowse.Navigate(@"about:blank");
        }

        private void importOpml(string p)
        {
            foreach (string feed in Opml.FeedsFromFile(p))
            {
                if (false == channels.hasFeed(feed))
                {
                    //addFeed(feed);
                    throw new Exception("Not implemented");
                }
            }
        }

        private void dFullscreen_Click(object sender, EventArgs e)
        {
            if (Colapsed) Colapsed = false;
            else Colapsed = true;
        }

        private bool Colapsed
        {
            get
            {
                return dMainSplit.Panel1Collapsed;
            }
            set
            {
                dMainSplit.Panel1Collapsed = value;
                dSubSplit.Panel1Collapsed = value;
            }
        }

        private void updateToolStripMenuItem_Click(object sender, EventArgs e)
        {
            updateFeeds();
        }

        private void updateFeeds()
        {
            if (false == dUpdator.IsBusy)
            {
                channels.markNew();
                dUpdator.RunWorkerAsync();
            }
        }

        private void dUpdator_DoWork(object sender, DoWorkEventArgs e)
        {
            List<UpdateAction> actions = new List<UpdateAction>( channels.updateList() );

            int c = actions.Count;

            for (int i = 0; i < c; ++i)
            {
                UpdateAction a = actions[i];
                dUpdator.ReportProgress(ToPercent(i, c), "Working...");
                a.perform();
            }

            channels.save();
        }

        private static int ToPercent(int i, int c)
        {
            return (int)((100*i) / (double)(c));
        }

        private void dUpdator_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            dUpdateProgress.Visible = true;
            dUpdateProgress.Value = e.ProgressPercentage;
            dStatusText.Text = (string)e.UserState;
        }

        private void dUpdator_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            if (channels.hasNew())
            {
                updateCompleteFeed();
                channels.save();
            }
            else
            {
                updateCompleteNoFeed();
            }
        }

        private void updateCompleteFeed()
        {
            dUpdateProgress.Visible = false;
            dStatusText.Text = "Ready";
            dNotify.Icon = Resources.feed;

            List<ItemRead> ni = new List<ItemRead>(channels.NewItems);
            Dictionary<string, List<ItemRead>> data = new Dictionary<string, List<ItemRead>>();

            foreach (ItemRead v in ni)
            {
                List<ItemRead> r;
                if (data.ContainsKey(v.Channel.Url))
                {
                    r = data[v.Channel.Url];
                }
                else
                {
                    r = new List<ItemRead>();
                    data.Add(v.Channel.Url, r);
                }
                r.Add(v);
            }

            const int maxCount = 4;
            List<string> sep = new List<string>();
            if (data.Count == 1)
            {
                int count = 0;
                foreach (ItemRead i in ni)
                {
                    sep.Add(i.Item.Title);
                    if (count > maxCount)
                    {
                        sep.Add("more...");
                        break;
                    }
                    ++count;
                }
            }
            else
            {
                int count = 0;
                foreach (var v in data)
                {
                    sep.Add(v.Value[0].Channel.Title);
                    if (count > maxCount)
                    {
                        sep.Add("more...");
                        break;
                    }
                    ++count;
                }
            }

            dNotify.ShowBalloonTip(1000, string.Format("{0} new message(s) available, {1} channel(s)",ni.Count, data.Count), new StringListCombiner(", ", " and ", "").combine(sep), ToolTipIcon.Info);
        }

        private void updateCompleteNoFeed()
        {
            dUpdateProgress.Visible = false;
            dStatusText.Text = "Ready";
            dNotify.Icon = Resources.nofeed;
        }

        FormWindowState oldState = FormWindowState.Normal;

        private void dNotify_MouseClick(object sender, MouseEventArgs e)
        {
            if (WindowState != FormWindowState.Minimized && false == Focused)
            {
                /*TopMost = true;
                Show();
                TopMost = false;
                //BringToFront();
                Focus();*/
                Activate();
            }
            else
            {
                if (WindowState == FormWindowState.Minimized)
                {
                    WindowState = oldState;
                }
                else
                {
                    oldState = WindowState;
                    WindowState = FormWindowState.Minimized;
                }
            }
        }

        private void updateViewBasedOn(Channel c)
        {
            if (c.HasInfo)
            {
                dFeedTitle.Text = c.Title;
                dFeedTitle.Tag = c.Link;
                dSubTitle.Text = c.Subtitle;
            }
            clearBrowser();

            dItems.SetObjects(c.Items);
        }

        private void dItems_SelectedIndexChanged(object sender, EventArgs e)
        {
            var r = (ItemRead)dItems.SelectedObject;
            if (r != null)
            {
                show(r);
            }
            else
            {
                clearBrowser();
            }
        }

        private void show(ItemRead r)
        {
            stopBrowser = false;
            dBrowse.Navigate(r.LocalPath);
            dPostTitle.Text = r.Item.Title;
            dPostTitle.Tag = r.Item.Link;
            if (r.read())
            {
                channels.updateNode(r.Channel);
                channels.save();
            }
            dItems.RefreshObject(r);
        }

        private void linkifyChildren(HtmlElement root)
        {
            foreach (HtmlElement e in root.Children)
            {
                if (e.TagName.ToLower() == "a")
                {
                    e.MouseEnter += new HtmlElementEventHandler(e_MouseEnter);
                    e.MouseLeave += new HtmlElementEventHandler(e_MouseLeave);
                }
                linkifyChildren(e);
            }
        }

        void e_MouseLeave(object sender, HtmlElementEventArgs e)
        {
            dHtmlLinkInfo.Text = "";
        }

        void e_MouseEnter(object sender, HtmlElementEventArgs e)
        {
            string url = e.ToElement.GetAttribute("href");
            dHtmlLinkInfo.Text = url;
        }

        bool stopBrowser = false;
        private void dBrowse_Navigating(object sender, WebBrowserNavigatingEventArgs e)
        {
            if (stopBrowser)
            {
                string source = e.Url.AbsoluteUri.ToLower().Trim();
                if (source != "about:blank")
                {
                    e.Cancel = true;
                    Web.OpenUrl(e.Url.AbsoluteUri);
                }
            }
        }

        private void dBrowse_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            dWebPageProgress.Visible = false;

            HtmlElement root = dBrowse.Document.Body;
            linkifyChildren(root);
            stopBrowser = true;
        }

        private void dBrowse_ProgressChanged(object sender, WebBrowserProgressChangedEventArgs e)
        {
            dProgressBytes.Text = string.Format("{0}/{1}", e.CurrentProgress, e.MaximumProgress);
            if (e.MaximumProgress != 0)
            {
                int percent = percent = (int)((e.CurrentProgress / (float)e.MaximumProgress) * 100);

                dWebPageProgress.Value = Math.Max(0, Math.Min(100, percent));
                dWebPageProgress.Visible = true;
            }
            else
            {
                dWebPageProgress.Visible = false;
            }
        }

        private void dFeedTitle_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            OpenLink(dFeedTitle);
        }

        private static void OpenLink(LinkLabel v)
        {
            if (null == v.Tag) return;
            string link = (string)v.Tag;
            Web.OpenUrl(link);
        }

        private void dPostTitle_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            OpenLink(dPostTitle);
        }

        private void dFeeds_SelectionChanged(object sender, EventArgs e)
        {
            if (dFeeds.SelectedObject == null) return;
            updateViewBasedOn((Channel)dFeeds.SelectedObject);
        }

        private void updateToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            updateFeeds();
        }

        private void addFeedToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Adder a = getSelectedFeedAdder();
            AddFeedDialog feed = new AddFeedDialog();
            if (feed.ShowDialog() == DialogResult.OK)
            {
                a.add(new Channels.Standard(providers, feed.Url));
            }
        }

        private Adder getSelectedFeedAdder()
        {
            var c = (Channel)dFeeds.SelectedObject;
            Adder a = channels;
            if (c != null) a = c.Adder;
            return a;
        }

        private void importOpmlToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (dOpmlBrowser.ShowDialog() == DialogResult.OK )
            {
                importOpml(dOpmlBrowser.FileName);
            }
        }

        private void addFolderToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Adder a = getSelectedFeedAdder();
            a.add(new Channels.Folder());
        }
    }
}
