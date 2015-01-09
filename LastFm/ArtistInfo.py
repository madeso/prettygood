using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using PrettyGood.Util;

namespace PrettyGood.LastFm
{
    public class ArtistInfo
    {
        internal ArtistInfo(XmlElement el)
        {
            XmlElement artist = Xml.GetFirstChild(el, "artist");
            this.name = Xml.GetTextOfSubElement(artist, "name");
            this.mbid = Xml.GetTextOfSubElementOrNull(artist, "mbid");
            this.url = Xml.GetTextOfSubElement(artist, "url");
            
            this.similar = new List<SimilarArtist>(CSharp.Convert(Xml.ElementsNamed(Xml.GetFirstChild(artist, "similar"), "artist") , x => new SimilarArtist(x)));
            this.tags = new List<Tag>(CSharp.Convert(Xml.ElementsNamed(Xml.GetFirstChild(artist, "tags"), "tag"), x => new Tag(x)));

            this.images = Image.Read(artist);

            XmlElement stats = Xml.GetFirstChild(artist, "stats");

            this.stats = new Stats {
                   listeners = long.Parse( Xml.GetTextOfSubElement(stats, "listeners"))
                 , playcount = long.Parse( Xml.GetTextOfSubElement(stats, "playcount"))
            };

            XmlElement bio = Xml.GetFirstChild(artist, "bio");

            this.bio = new Bio{
                   published = Xml.GetTextOfSubElementOrNull(bio, "published")
                 ,  content = Xml.GetTextOfSubElementOrNull(bio, "summary")
                 ,  summary = Xml.GetTextOfSubElementOrNull(bio, "content")
            };

            this.streamable = int.Parse(Xml.GetTextOfSubElement(artist, "streamable"))==1;
        }

        public readonly string name;
        public readonly string mbid;
        public readonly string url;
        public readonly bool streamable;
        public readonly Stats stats;
        public readonly Bio bio;

        public readonly List<SimilarArtist> similar;
        public readonly List<Tag> tags;
        public readonly List<Image> images;

        public struct Stats
        {
            public long listeners;
            public long playcount;
        }
        
        public struct Bio
        {
            public string published;
            public string summary;
            public string content;
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

        public string suggestAlternative()
        {
            if (similar.Count == 0) return string.Empty;
            return similar[0].name;
        }

        public struct SimilarArtist
        {
            public SimilarArtist(XmlElement sart)
            {
                name = Xml.GetTextOfSubElement(sart, "name");
                url = Xml.GetTextOfSubElement(sart, "url");
            }
            public readonly string name;
            public readonly string url;
        }
    }
}
