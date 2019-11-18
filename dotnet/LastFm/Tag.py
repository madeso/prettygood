using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using PrettyGood.Util;

namespace PrettyGood.LastFm
{
    public class Tag
    {
        public Tag( XmlElement el )
        {
            this.name = Xml.GetTextOfSubElement(el, "name");
            this.url = Xml.GetTextOfSubElement(el, "url");
        }

        public readonly string name;
        public readonly string url;
    }
}
