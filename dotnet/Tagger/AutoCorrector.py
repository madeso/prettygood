using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Tagger
{
    class AutoCorrector
    {
        Dictionary<string, string> artists = new Dictionary<string, string>();
        Dictionary<string, string> genres = new Dictionary<string, string>();

        internal void feed(IdTag current, IdTag old)
        {
            Feed(artists, current, old, x=>x.Artist);
            Feed(genres, current, old, x => x.Genre);
        }

        internal void correct(TagMatch t)
        {
            Correct(artists, ref t.Tag.Artist);
            Correct(genres, ref t.Tag.Genre);
        }

        private static void Feed(Dictionary<string, string> dict, IdTag current, IdTag old, Func<IdTag, string> getter)
        {
            string c = getter(current);
            string o = getter(old);

            if (string.IsNullOrEmpty(c) || string.IsNullOrEmpty(o)) return;
            if (o.CompareTo(c) == 0) return;

            dict[o] = c;
        }

        private static void Correct(Dictionary<string, string> dict, ref string value)
        {
            if (string.IsNullOrEmpty(value)) return;
            if (dict.ContainsKey(value)) value = dict[value];
        }
    }
}
