using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using System.IO;

namespace SeriesNamer.tvdb
{
    public class Database
    {
        private readonly string apikey;
        private readonly string mirror;

        public Database(string apikey)
        {
            this.apikey = apikey;
            mirror = new MirrorList(GetXml("http://www.thetvdb.com/api/" + apikey + "/mirrors.xml", "Mirrors"))
                .suggest(YesNo.DontCare, YesNo.DontCare, YesNo.Yes);
            // string servertime = GetServerTime(GetXml("http://www.thetvdb.com/api/Updates.php?type=none"));
            readLoacalDatabase();
        }

        private static XmlElement GetXml(string p, string root)
        {
            string source = Web.FetchString(p);
            return Xml.Open(Xml.FromSource(source), root);
        }

        internal string suggestTitle(string series, int season, int episode, out string newName)
        {
            Series s = getSeries(series);
            if (s == null) throw new Exception("No series named " + series);
            Season sa = s.getSeason(season);
            if (sa == null) throw new Exception("No season " + season.ToString() + " for " + series);
            Episode e = sa.getEpisode(episode);
            if (e == null) throw new Exception("No episode " + episode + " in season " + season.ToString() + " for " + series);
            newName = s.Name;
            return e.Title;
        }

        private string getSeriesId(string series, out string newName)
        {
            XmlElement root = GetXml("http://www.thetvdb.com/api/GetSeries.php?seriesname=" + Safe(series), "Data");
            List<KeyValuePair<string, string>> id = new List<KeyValuePair<string, string>>();
            foreach (XmlElement el in Xml.ElementsNamed(root, "Series"))
            {
                string iid = Xml.GetTextOfSubElement(el, "seriesid");
                string actualName = Xml.GetTextOfSubElement(el, "SeriesName");
                if (actualName.ToLower().Trim() == series.ToLower().Trim())
                {
                    newName = actualName;
                    return iid;
                }
                id.Add(new KeyValuePair<string, string>(iid, actualName));
            }
            if (id.Count > 1) throw new Exception("More than one series... dont know what to do");
            if( id.Count == 0 ) throw new Exception("Show unknown");
            newName = id[0].Value;
            return id[0].Key;
        }

        private static string Safe(string series)
        {
            return series.Trim().Replace(" ", "%20");
        }

        Dictionary<string, Series> sDict = new Dictionary<string, Series>();

        const string kLocalDatabaseFile = "db.xml";

        private void readLoacalDatabase()
        {
            string path = getDtabaseDir();
            string filename = Path.Combine(path, kLocalDatabaseFile);
            if (false == File.Exists(filename)) return;
            XmlElement root = Xml.Open(Xml.FromFile(filename), "db");
            foreach(XmlElement seriesElement in Xml.ElementsNamed(root, "series") )
            {
                string seriesName = Xml.GetAttributeString(seriesElement, "name");
                string seriesId = Xml.GetAttributeString(seriesElement, "id");
                string ttl = seriesName.Trim().ToLower();
                Series series = new Series(seriesId, seriesName);
                foreach (XmlElement seasonElement in Xml.ElementsNamed(seriesElement, "season"))
                {
                    string idstr = Xml.GetAttributeString(seasonElement, "id");
                    int seasonId = int.Parse(idstr);
                    Season season = new Season(seasonId);
                    foreach (XmlElement episodeElement in Xml.ElementsNamed(seasonElement, "episode"))
                    {
                        string eidstr = Xml.GetAttributeString(episodeElement, "id");
                        int episodeId = int.Parse(eidstr);
                        string episodeTitle = Xml.GetAttributeString(episodeElement, "title");
                        string overview = Xml.GetTextOfSubElementOrNull(episodeElement, "overview");
                        Episode episode = new Episode(episodeId, episodeTitle, overview);
                        season.add(episode);
                    }
                    series.add(season);
                }
                sDict.Add(ttl, series);
            }
        }

        private string getDtabaseDir()
        {
            string cad = Environment.GetFolderPath(Environment.SpecialFolder.CommonApplicationData);
            return Path.Combine(Path.Combine(cad, "seriesnamer"), "db");
        }

        public void saveLocalDatabase()
        {
            ElementBuilder root = new ElementBuilder().child("db");

            foreach (KeyValuePair<string, Series> k in sDict)
            {
                ElementBuilder series = root.child("series").attribute("name", k.Value.Name).attribute("id", k.Value.Id);
                foreach (Season s in k.Value.Seasons)
                {
                    ElementBuilder season = series.child("season").attribute("id", s.Index.ToString());
                    foreach (Episode e in s.Episodes)
                    {
                        season.child("episode")
                            .attribute("id", e.Index.ToString())
                            .attribute("title", e.Title)
                            .child("overview").text(e.Overview);
                    }
                }
            }

            string dir = getDtabaseDir();
            FileUtil.MakeSureDirectoryExist(dir);

            root.Document.Save( Path.Combine(dir, kLocalDatabaseFile) );
        }

        private Series getSeries(string series)
        {
            string ttl = series.Trim().ToLower();
            if (sDict.ContainsKey(ttl)) return sDict[ttl];

            string name;
            string id = getSeriesId(series, out name);
            string language = "en";

            string basedir = Path.Combine(getDtabaseDir(), "downloaded");
            FileUtil.MakeSureDirectoryExist(basedir);

            string zipfile = Path.Combine(basedir, id + ".zip");
            string targetxml = Path.Combine(basedir, id + ".xml");
            string url = mirror + "/api/"+ apikey + "/series/" + id + "/all/" + language + ".zip";
            if (false == File.Exists(zipfile)) Web.DownloadTo(url, zipfile);
            ExtractZipfile(zipfile, language+".xml", targetxml);
            Series s = new Series(id, name);
            s.parse(Xml.Open(Xml.FromFile(targetxml), "Data"));

            sDict.Add(ttl, s);

            // we're done
            File.Delete(zipfile);

            return s;
        }

        private void ExtractZipfile(string zipfile, string fileInZip, string targetXml)
        {
            if( File.Exists(targetXml) ) File.Delete(targetXml);
            using (ZipFile zf = ZipFile.Read(zipfile))
            {
                using (Stream s = File.OpenWrite(targetXml))
                {
                    ZipEntry ze = zf[fileInZip];
                    ze.Extract(s);
                }
            }
        }
    }
}
