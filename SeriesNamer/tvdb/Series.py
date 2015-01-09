using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;

namespace SeriesNamer.tvdb
{
    public class Series
    {
        private readonly string seriesid;
        private readonly string name;

        public Series(string id, string name)
        {
            this.seriesid = id;
            this.name = name;
        }

        public string Id
        {
            get
            {
                return seriesid;
            }
        }

        public IEnumerable<Season> Seasons
        {
            get
            {
                foreach (KeyValuePair<int, Season> k in seasons)
                {
                    yield return k.Value;
                }
            }
        }

        Dictionary<int, Season> seasons = new Dictionary<int, Season>();

        public void add(Season s)
        {
            seasons.Add(s.Index, s);
        }

        public string Name
        {
            get
            {
                return name;
            }
        }

        internal Season getSeason(int s)
        {
            if (false == seasons.ContainsKey(s)) return null;
            return seasons[s];
        }

        internal void parse(XmlElement root)
        {
            foreach(XmlElement episode in Xml.ElementsNamed(root, "Episode") )
            {
                string seasonName = Xml.GetTextOfSubElement(episode, "Combined_season");
                Season s = getOrCreateSeason(seasonName);
                string episodeName = Xml.GetTextOfSubElement(episode, "EpisodeNumber").Trim();
                string title = Xml.GetTextOfSubElementOrNull(episode, "EpisodeName");
                string overview = Xml.GetTextOfSubElementOrNull(episode, "Overview");
                int episodeId = int.Parse(episodeName);
                s.add(new Episode(episodeId, title, overview));
            }
        }

        private Season getOrCreateSeason(string seasonName)
        {
            int season = int.Parse(seasonName);

            Season s = getSeason(season);
            if (s != null) return s;

            s = new Season(season);
            seasons.Add(season, s);
            return s;
        }
    }
}
