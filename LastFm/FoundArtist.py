using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using PrettyGood.Util;

namespace PrettyGood.LastFm
{
	public class FoundArtist
	{
		internal FoundArtist(XmlElement el)
		{
			this.name = Xml.GetTextOfSubElement(el, "name");
			this.mbid = Xml.GetTextOfSubElementOrNull(el, "mbid");
			this.url = Xml.GetTextOfSubElement(el, "url");
		}

		public bool seemsGoofy
		{
			get
			{
				if (string.IsNullOrEmpty(mbid)) return true;
				else if (url.Contains("+noredirect")) return true;
				else return false;
			}
		}

		public readonly string name;
		public readonly string mbid;
		public readonly string url;
	}
}
