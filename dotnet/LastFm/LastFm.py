using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;
using PrettyGood.Util;
using System.Xml;
using System.Globalization;

namespace PrettyGood.LastFm
{
    public class LastFm
    {
        private readonly string api;
        private Encoding encoding = Encoding.UTF32;

        public LastFm(string api)
        {
            this.api = api;
            foreach (ApiItem item in Reflect.MembersOf<ApiItem, LastFm>(this))
            {
                item.app = this;
            }
        }

        public class ApiItem
        {
            internal LastFm app;
            internal XmlElement call(Arguments a)
            {
                return app.call(a);
            }
        }

        public static IEnumerable<System.Globalization.CultureInfo> Languages
        {
            get
            {
                Dictionary<string, CultureInfo> infos = new Dictionary<string, CultureInfo>();
                foreach( CultureInfo ci in CultureInfo.GetCultures(CultureTypes.AllCultures) )
                {
                    if (false == string.IsNullOrEmpty(ci.TwoLetterISOLanguageName) && false == infos.ContainsKey(ci.TwoLetterISOLanguageName) )
                    {
                        infos.Add(ci.TwoLetterISOLanguageName, ci);
                        yield return ci;
                    }
                }
            }
        }

        public class Artist : ApiItem
        {
            public ArtistInfo getInfo(string artist, string mbid, System.Globalization.CultureInfo lang)
            {
                XmlElement el = call(new Arguments().rarg("method", "artist.getInfo").arg("artist", artist).arg("mbid", mbid).lang(lang));
                return new ArtistInfo(el);
            }

            public IEnumerable<FoundArtist> search(string artist, string mbid, System.Globalization.CultureInfo lang)
            {
                XmlElement el = call(new Arguments().rarg("method", "artist.search").arg("artist", artist).arg("mbid", mbid).lang(lang));
                XmlElement matches = Xml.GetFirstChild( Xml.GetFirstChild(el, "results") , "artistmatches");
                foreach (XmlElement ael in Xml.ElementsNamed(matches, "artist"))
                {
                    yield return new FoundArtist(ael);
                }
            }

            public ArtistInfo getInfo(FoundArtist artist, System.Globalization.CultureInfo lang)
            {
                return getInfo(artist.name, artist.mbid, lang);
            }
        }

        public class Album : ApiItem
        {
            public IEnumerable<FoundAlbum> search(string album)
            {
                XmlElement el = call(new Arguments().rarg("method", "album.search").arg("album", album));
                XmlElement matches = Xml.GetFirstChild(Xml.GetFirstChild(el, "results"), "albummatches");
                foreach (XmlElement ael in Xml.ElementsNamed(matches, "album"))
                {
                    yield return new FoundAlbum(ael);
                }
            }
        }

        internal static string buildUrl(Arguments a)
        {
            string args = new StringListCombiner("&")
                .combineFromEnumerable(
                    Util.CSharp.Convert(
                            a.Args, k => k.Key + "=" + Web.Escape(k.Value)
                        )
                    );
            return "http://ws.audioscrobbler.com/2.0/?" + args;
        }

        public Artist artist = new Artist();
        public Album album = new Album();

        internal XmlElement call(Arguments a)
        {
            string url = buildUrl(a.rarg("api_key", api));
            string source = Web.FetchString(url, ref encoding);
            XmlElement root = Xml.Open(Xml.FromSource(source), "lfm");
            ThrowIfError(root);
            return root;
        }

        private static void ThrowIfError(XmlElement root)
        {
            string status = Xml.GetAttributeString(root, "status");
            if (status != "ok") throw new Error(root);
        }
    }
}
