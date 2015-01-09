using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Feed;
using System.Windows.Forms;
using PrettyGood.Util;
using System.Xml;

namespace Seymour.Channels
{
	public class Folder : Channel, Adder
	{
		List<Channel> subs = new List<Channel>();
		public override string Url
		{
			get { return string.Empty; }
		}

		public override bool HasInfo
		{
			get { return true; }
		}

		private string name = "folder";

		public override string Title
		{
			get { return name; }
			set { name = value; }
		}

		public override string Link
		{
			get { return ""; }
		}

		public override string Subtitle
		{
			get { return ""; }
		}

		public const string TypeName = "folder";

		internal override void write(ElementBuilder b)
		{
			b.attribute(Channel.TypeAttributeName, TypeName).attribute("name", name);
			foreach (Channel c in subs)
			{
				c.write(b.child("channel"));
			}
		}

		public override IEnumerable<UpdateAction> UpdateActions()
		{
			foreach (Channel c in subs)
			{
				foreach (UpdateAction a in c.UpdateActions())
				{
					yield return a;
				}
			}
		}

		internal override void unread(ItemRead r)
		{
			foreach (Channel c in subs)
			{
				c.unread(r);
			}
		}

		public override IEnumerable<ItemRead> Items
		{
			get
			{
				foreach (Channel c in subs)
				{
					foreach (ItemRead i in c.Items)
					{
						yield return i;
					}
				}
			}
		}

		public override bool isRead(ItemRead it)
		{
			foreach (Channel c in subs)
			{
				if (c.isRead(it)) return true;
			}
			return false;
		}

		public override bool read(ItemRead it)
		{
			foreach (Channel c in subs)
			{
				if (c.read(it)) return true;
			}
			return false;
		}

		internal override int unreadCount()
		{
			int count = 0;
			foreach (Channel c in subs)
			{
				count += c.unreadCount();
			}
			return count;
		}

		internal override void markNew()
		{
			foreach (Channel c in subs)
			{
				c.markNew();
			}
		}

		public override IEnumerable<ItemRead> NewItems
		{
			get
			{
				foreach (Channel c in subs)
				{
					foreach (ItemRead i in c.NewItems)
					{
						yield return i;
					}
				}
			}
		}

		public override Adder Adder
		{
			get { return this; }
		}
		
		public void add(Channel c)
		{
			subs.Add(c);
			c.List = List;
			c.update();
			update();
		}

		public override bool HasSubFeeds
		{
			get { return true; }
		}

		public override IEnumerable<Channel> Feeds
		{
			get { return subs; }
		}

		internal static Channel DoLoad(ProviderList p, System.Xml.XmlElement el)
		{
			Folder f = new Folder();

			f.name = Xml.GetAttributeString(el, "name");

			foreach (XmlElement x in Xml.ElementsNamed(el, "channel"))
			{
				f.subs.Add(Channel.Load(p, x));
			}

			return f;
		}
	}
}