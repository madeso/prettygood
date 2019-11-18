using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using PrettyGood.Util;
using System.Xml;

namespace Seymour
{
    class Opml
    {
        public static IEnumerable<string> FeedsFromFile(string p)
        {
            XmlElement opml = Xml.Open(Xml.FromFile(p), "opml");
            foreach(XmlElement e in Xml.ElementsNamed(opml["body"], "outline") )
            {
                yield return Xml.GetAttributeString(e, "xmlUrl");
            }
        }
    }
}
