using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;

namespace SeriesNamer.tvdb
{
    public class MirrorList
    {
        public MirrorList(XmlElement root)
        {
            foreach (XmlElement e in Xml.ElementsNamed(root, "Mirror"))
            {
                Mirror m = new Mirror();
                m.id = Xml.GetTextOfSubElement(e, "id");
                m.url = Xml.GetTextOfSubElement(e, "mirrorpath");
                int typemask = int.Parse(Xml.GetTextOfSubElement(e, "typemask"));
                m.xml = (typemask & 1) != 0;
                m.banner = (typemask & 2) != 0;
                m.zip = (typemask & 4) != 0;
                mirrors.Add(m);
            }
        }

        private List<Mirror> mirrors = new List<Mirror>();

        private struct Mirror
        {
            public string id;
            public string url;
            public bool xml;
            public bool banner;
            public bool zip;

            public bool match(YesNo xml, YesNo banner, YesNo zip)
            {
                return match(this.xml, xml)
                    && match(this.banner, banner)
                    && match(this.zip, zip)
                    ;
            }

            private static bool match(bool b, YesNo y)
            {
                if( b == false && y == YesNo.Yes) return false;
                if( b == true && y == YesNo.No) return false;
                return true;
            }
        }

        internal string suggest(YesNo xml, YesNo banner, YesNo zip)
        {
            List<Mirror> suitables = new List<Mirror>();
            foreach (Mirror m in mirrors)
            {
                if (m.match(xml, banner, zip))
                    suitables.Add(m);
            }

            int count = suitables.Count;
            if( count == 0 ) throw new Exception("No sutiable mirror found");

            // pick a random suitable
            Random r = new Random();
            int index = r.Next(count);
            return suitables[index].url;
        }
    }
}
