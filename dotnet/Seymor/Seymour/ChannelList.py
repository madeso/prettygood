using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using PrettyGood.Util;
using System.Xml;
using System.Windows.Forms;
using BrightIdeasSoftware;

namespace Seymour
{
    public class ChannelList : Adder
    {
        TreeListView view;

        public TreeListView View
        {
            get
            {
                return view;
            }
        }

        public ChannelList(TreeListView view)
        {
            this.view = view;
        }

        public void add(Channel c)
        {
            view.AddObject(c);
            c.List = this;
            c.update();
        }

        internal IEnumerable<UpdateAction> updateList()
        {
            foreach (Channel c in Channels)
            {
                foreach (UpdateAction a in c.UpdateActions())
                {
                    yield return a;
                }
            }
        }

        public void save(string file)
        {
            ElementBuilder builder = new ElementBuilder().child("seymor");
            foreach (Channel c in view.Objects)
            {
                c.write(builder.child("channel"));
            }
            builder.Document.Save(file);
        }

        public void save()
        {
            save(ChannelsFile());
        }

        private static string ChannelsFile()
        {
            return FileUtil.GetUserPathFor().file("channels", "xml");
        }

        public void load(ProviderList p)
        {
            load(p, ChannelsFile());
        }

        int currentUnread()
        {
            int u = 0;
            foreach (Channel c in Channels)
            {
                u += c.unreadCount();
            }
            return u;
        }

        public bool hasNew()
        {
            foreach (Channel c in Channels)
            {
                if (c.hasNew()) return true;
            }
            return false;
        }

        public void markNew()
        {
            foreach (Channel c in Channels)
            {
                c.markNew();
            }
        }

        public IEnumerable<ItemRead> NewItems
        {
            get
            {
                foreach (Channel c in view.Objects)
                {
                    foreach (ItemRead r in c.NewItems)
                    {
                        yield return r;
                    }
                }
            }
        }

        public void load(ProviderList p, string paths)
        {
            XmlElement root = Xml.Open(Xml.FromFile(paths), "seymor");
            foreach(XmlElement el in Xml.ElementsNamed(root, "channel"))
            {
                Channel c = Channel.Load(p, el);
                add(c);
            }
        }

        public delegate void ItemAdded(ItemRead item);

        public event Delegates.VoidVoid OnSelectionUpdated;
        public event ItemAdded OnNewItem;

        public void updateNode(Channel c)
        {
            view.RefreshObject(c);
            if (view.SelectedObject == c)
            {
                if( OnSelectionUpdated != null ) OnSelectionUpdated();
            }

            if (OnNewItem != null)
            {
                bool shouldClear = false;
                foreach (ItemRead r in c.NewItems)
                {
                    OnNewItem(r);
                    shouldClear = true;
                }

                if (shouldClear) c.markNew();
            }
        }

        IEnumerable<Channel> Channels
        {
            get
            {
                foreach (Channel c in view.Objects)
                {
                    yield return c;
                }
            }
        }

        internal bool hasFeed(string feed)
        {
            string feedttl = feed.ToLower();
            foreach(Channel c in Channels)
            {
                if (c.Url.ToLower() == feedttl) return true;
            }
            return false;
        }
    }
}
