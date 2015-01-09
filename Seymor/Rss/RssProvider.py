using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Feed;
using PrettyGood.Util;
using System.Xml;

namespace Rss
{
	class RssProvider : ItemProvider
	{
		public override CurrentData sample(string adoc)
		{
			XmlElement root;

			string doc = adoc;
			doc = doc.Trim('?'); // some (invalid) rss feeds began with ???

			try
			{
				root = Xml.Open(Xml.FromSource(doc), "rss");
				string version = Xml.GetAttributeString(root, "version");
				if (version != "2.0") return null;
			}
			catch (Exception)
			{
				return null;
			}

			XmlElement channel = root["channel"];

			CurrentData data = new CurrentData();

			data.Info.Title = Xml.GetTextOfSubElement(channel, "title");
			data.Info.Link = Xml.GetTextOfSubElement(channel, "link");
			data.Info.SubTitle = Xml.GetTextOfSubElement(channel, "description");
			data.Info.Email = Xml.GetTextOfSubElementOrNull(channel, "managingEditor");
			data.Info.Updated = ParseDate(Xml.GetTextOfSubElementOrNull(channel, "lastBuildDate"));

			foreach (XmlElement i in Xml.ElementsNamed(channel, "item"))
			{
				Item it = new Item();

				it.Title = Xml.GetTextOfSubElement(i, "title");
				it.Link = Xml.GetTextOfSubElement(i, "link");
				it.Summary = Xml.GetTextOfSubElement(i, "description");
				it.Updated = ParseDate(Xml.GetTextOfSubElement(i, "pubDate"));
				it.Id = Xml.GetTextOfSubElementOrNull(i, "guid");
				if (string.IsNullOrEmpty(it.Id)) it.Id = it.Link;

				data.Items.Add(it);
			}

			return data;
		}

		private DateTime ParseDate(string p)
		{
			if (String.IsNullOrEmpty(p)) return DateTime.Now;
			// Wed, 27 May 2009 11:30:00 PDT
			return Parse.DateTime(p, "r", "D", "ddd, d MM yyyy HH:MM:SS PDT"); // ???
			//throw new NotImplementedException();
		}
	}
}
