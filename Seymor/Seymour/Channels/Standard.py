using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Feed;
using PrettyGood.Util;
using System.Windows.Forms;
using System.IO;
using System.Xml;
using BrightIdeasSoftware;

namespace Seymour.Channels
{
    public class Standard : Channel
    {
        public Standard(ProviderList providers, string url)
        {
            this.providers = providers;
            this.url = url;
        }

        ProviderList providers;
        readonly string url;

        public override string Url
        {
            get
            {
                return url;
            }
        }

        ItemProvider provider = null;

        private List<ItemRead> list = new List<ItemRead>();
        private Dictionary<string, ItemRead> dict = new Dictionary<string, ItemRead>();
        Dictionary<string, ItemRead> unreadItems = new Dictionary<string, ItemRead>();

        public Info Info;
        private Encoding Encoding = Encoding.UTF8;

        public override string Title
        {
            get
            {
                if (Info == null) return url;
                else return Info.Title;
            }
            set
            {
                throw new Exception("implement support for renaming standard feeds");
            }
        }

        public override string Subtitle
        {
            get
            {
                if (Info == null) return "";
                else return Info.SubTitle;
            }
        }

        public const string TypeName = "standard";

        internal override void write(ElementBuilder b)
        {
            b
                .attribute(Channel.TypeAttributeName, TypeName)
                .attribute("url", url)
                .attribute("hasInfo", (Info != null).ToString())
                .attribute("encoding", Encoding.CodePage.ToString());
            if (null != Info)
            {
                b
                    .attribute("title", Info.Title)
                    .attribute("subtitle", Info.SubTitle)
                    .attribute("updated", Info.Updated.ToFileTimeUtc().ToString())
                    .attribute("author", Info.Author)
                    .attribute("email", Info.Email)
                    .attribute("link", Info.Link);
            }

            ElementBuilder e = b.child("items");
            foreach (ItemRead i in list)
            {
                i.write(e.child("item"));
            }

            ElementBuilder u = b.child("unread");
            foreach (var v in unreadItems)
            {
                u.child("item").attribute("id", v.Key);
            }
        }

        private ItemRead getFromId(string p)
        {
            return dict[p];
        }

        internal static Standard DoLoad(ProviderList p, XmlElement el)
        {
            Standard c = new Standard(p, Xml.GetAttributeString(el, "url"));
            c.Encoding = System.Text.Encoding.GetEncoding(int.Parse(Xml.GetAttributeString(el, "encoding")));

            if (Xml.GetAttributeBool(el, "hasInfo", false))
            {
                c.Info = new Info
                {
                    Title = Xml.GetAttributeString(el, "title")
                    ,
                    SubTitle = Xml.GetAttributeString(el, "subtitle")
                    ,
                    Updated = DateTime.FromFileTimeUtc(long.Parse(Xml.GetAttributeString(el, "updated")))
                    ,
                    Author = Xml.GetAttributeString(el, "author")
                    ,
                    Email = Xml.GetAttributeString(el, "email")
                    ,
                    Link = Xml.GetAttributeString(el, "link")
                };
            }

            foreach (XmlElement e in Xml.ElementsNamed(el["items"], "item"))
            {
                ItemRead r = ItemRead.Load(e, c);
                c.addExisting(r);
            }

            foreach (XmlElement e in Xml.ElementsNamed(el["unread"], "item"))
            {
                c.unread(c.getFromId(Xml.GetAttributeString(e, "id")));
            }

            return c;
        }



        private string fetchSource()
        {
            string doc = Web.FetchString(url, ref Encoding);
            return doc;
        }

        private class FetchSourceAction : UpdateAction
        {
            public Standard Standard;
            public string Source;

            public override void perform()
            {
                Source = Standard.fetchSource();
            }
        }

        private CurrentData provide(string doc)
        {
            CurrentData d = providers.provide(ref provider, doc);
            return d;
        }

        private class ProvideDataAction : UpdateAction
        {
            public Standard Standard;
            public FetchSourceAction Source;
            public CurrentData Data;

            public override void perform()
            {
                Data = Standard.provide(Source.Source);
            }
        }

        private void addIfNotFound(CurrentData d)
        {
            if (d == null) return;
            Info = d.Info;

            foreach (Item i in d.Items)
            {
                if (false == has(i))
                {
                    addNew(i);
                }
            }
        }

        private class UpdateDataAction : UpdateAction
        {
            public Standard Standard;
            public ProvideDataAction ProvideDataAction;

            public override void perform()
            {
                Standard.addIfNotFound(ProvideDataAction.Data);
            }
        }

        private void updateNode()
        {
            clist.updateNode(this);
        }

        private class UpdateNodeAction : UpdateAction
        {
            public Standard Standard;
            public TreeListView treeListView;

            public override void perform()
            {
                Gui.InvokeOrCall(treeListView, new Action(delegate { Standard.updateNode(); }));
            }
        }

        public override IEnumerable<UpdateAction> UpdateActions()
        {
            FetchSourceAction fsa = new FetchSourceAction { Standard = this };
            ProvideDataAction pda = new ProvideDataAction { Standard = this, Source = fsa };
            UpdateDataAction uda = new UpdateDataAction { Standard = this, ProvideDataAction = pda };

            yield return fsa;
            yield return pda;
            yield return uda;
            yield return new UpdateNodeAction { treeListView = clist.View, Standard = this };
        }

        private bool has(Item i)
        {
            return dict.ContainsKey(i.Id);
        }

        private void addNew(Item i)
        {
            ItemRead r = new ItemRead(i, this);

            r.Channel = this;
            FileUtil.MakeSurePathExist(r.LocalPath);
            File.WriteAllLines(r.LocalPath, r.Html.ToArray(), Encoding);

            newItems.Add(r);

            addExisting(r);
            unread(r);
        }

        internal override void unread(ItemRead r)
        {
            unreadItems.Add(r.Item.Id, r);
        }

        internal void addExisting(ItemRead r)
        {
            dict.Add(r.Item.Id, r);
            list.Add(r);
        }

        public override IEnumerable<ItemRead> Items
        {
            get
            {
                return list;
            }
        }

        public override bool isRead(ItemRead it)
        {
            return false == unreadItems.ContainsKey(it.Item.Id);
        }

        public override bool read(ItemRead it)
        {
            if (unreadItems.ContainsKey(it.Item.Id))
            {
                unreadItems.Remove(it.Item.Id);
                return true;
            }
            else return false;
        }

        IEnumerable<ItemRead> UnreadItems
        {
            get
            {
                foreach (var v in unreadItems)
                {
                    yield return v.Value;
                }
            }
        }

        internal override  int unreadCount()
        {
            return unreadItems.Count;
        }

        List<ItemRead> newItems = new List<ItemRead>();

        internal override void markNew()
        {
            newItems.Clear();
        }
        public override IEnumerable<ItemRead> NewItems
        {
            get
            {
                return newItems;
            }
        }

        public override bool HasInfo
        {
            get { return Info != null; }
        }

        public override string Link
        {
            get { return Info.Link; }
        }

        public override bool HasSubFeeds
        {
            get { return false; }
        }

        public override IEnumerable<Channel> Feeds
        {
            get { yield return null; }
        }
    }

}
