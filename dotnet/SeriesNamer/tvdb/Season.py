using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SeriesNamer.tvdb
{
    public class Season
    {
        private readonly int index;
        Dictionary<int, Episode> episodes = new Dictionary<int, Episode>();

        public Season(int index)
        {
            this.index = index;
        }

        public IEnumerable<Episode> Episodes
        {
            get
            {
                foreach (KeyValuePair<int, Episode> k in episodes)
                {
                    yield return k.Value;
                }
            }
        }

        public void add(Episode ep)
        {
            episodes.Add(ep.Index,  ep);
        }

        public int Index
        {
            get
            {
                return index;
            }
        }

        internal Episode getEpisode(int episode)
        {
            if (false == episodes.ContainsKey(episode)) return null;
            return episodes[episode];
        }
    }
}
