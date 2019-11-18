using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using PrettyGood.Util;

namespace PrettyGood.LastFm
{
    public class FoundAlbum
    {
        internal FoundAlbum(XmlElement el)
        {
            this.name = Xml.GetTextOfSubElement(el, "name");
            this.artist = Xml.GetTextOfSubElement(el, "artist");
            this.id = Xml.GetTextOfSubElement(el, "id");
            this.url = Xml.GetTextOfSubElement(el, "url");
            this.streamable = int.Parse(Xml.GetTextOfSubElement(el, "streamable")) == 1;
            this.images = Image.Read(el);
        }

        public readonly string name;
        public readonly string artist;
        public readonly string id;
        public readonly string url;
        public readonly bool streamable;
        public readonly List<Image> images;

    }
}
