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

namespace Seymour
{
	public abstract class Channel
	{
		public const string TypeAttributeName = "type";

		public abstract string Url
		{
			get;
		}

		public abstract bool HasInfo
		{
			get;
		}

		public abstract string Title
		{
			get;
			set;
		}

		public abstract string Link
		{
			get;
		}

		public abstract string Subtitle
		{
			get;
		}

		internal abstract void write(ElementBuilder b);

		
		internal static Channel Load(ProviderList p, XmlElement el)
		{
			string type = Xml.GetAttributeString(el, TypeAttributeName);

			if (type == Channels.Standard.TypeName) return Channels.Standard.DoLoad(p, el);
			if (type == Channels.Folder.TypeName) return Channels.Folder.DoLoad(p, el);
			
			throw new Exception("Unsupported type " + type);
		}

		public abstract IEnumerable<UpdateAction> UpdateActions();

		internal abstract void unread(ItemRead r);

		public abstract IEnumerable<ItemRead> Items
		{
			get;
		}

		public abstract bool isRead(ItemRead it);

		public abstract bool read(ItemRead it);

		internal abstract int unreadCount();

		public string NameAndCount
		{
			get
			{
				int uc = unreadCount();
				string format = uc == 0 ? "{0}" : "{0} ({1})";
				return string.Format(format, Title, uc);
			}
		}

		internal abstract void markNew();

		public abstract IEnumerable<ItemRead> NewItems
		{
			get;
		}

		public bool hasNew()
		{
			foreach (ItemRead r in NewItems)
			{
				return true;
			}

			return false;
		}

		/*internal static Channel Create(ProviderList providers, string url, Adder adder)
		{
			return Channels.Standard.Create(providers, url, adder);
		}*/

		protected ChannelList clist;
		public ChannelList List
		{
			get
			{
				return clist;
			}
			set
			{
				if (clist != null) throw new Exception("programmer misstake: already contains a list");
				clist = value;
			}
		}

		protected Adder parent;

		public virtual Adder Adder
		{
			get
			{
				return parent;
			}
			set
			{
				parent = value;
			}
		}

		public void update()
		{
			List.updateNode(this);
		}

		public abstract bool HasSubFeeds { get; }
		public abstract IEnumerable<Channel> Feeds { get; }
	}
}
