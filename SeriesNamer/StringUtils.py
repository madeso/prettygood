using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SeriesNamer
{
    class StringUtils
    {
        internal static IEnumerable<string> Unique(IEnumerable<string> str)
        {
            Dictionary<string, string> dict = new Dictionary<string, string>();
            foreach (string s in str)
            {
                if (s == null) continue;
                string ls = s.ToLower();
                if (false == dict.ContainsKey(ls)) dict.Add(ls, s);
            }

            foreach(KeyValuePair<string, string> k in dict)
            {
                yield return k.Value;
            }
        }
    }
}
