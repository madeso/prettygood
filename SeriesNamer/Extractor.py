using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace SeriesNamer
{
    public static class Extractor
    {
        public static Dictionary<string, string> extract(string pattern, string filename)
        {
            Dictionary<string, string> res = new Dictionary<string, string>();
            try
            {
                string p = extractRegex(pattern, @"(?<${1}>.+)", x => Regex.Escape(x)); // dynamically generate a regex from the simpler input pattern
                Regex r = new Regex(p, RegexOptions.RightToLeft); // RightToLeft forces A_B_C to be split into A B_C instead of A_B C when splitting on _
                Match m = r.Match(filename);

                // skip the first one since it contains the whole expression
                for (int i = 1; i < m.Groups.Count; ++i)
                {
                    string name = r.GroupNameFromNumber(i);
                    string value = m.Groups[i].Value;
                    res[name] = value;
                }
            }
            catch (ArgumentException)
            {
                // todo: handle regex exception in a more graceful way
            }

            return res;
        }

        // pattern is %element% based.
        // Everything outside %element% is escaped with the escapor.
        // Everything inside is replaced with replacement, where ${1} is the text string encapsulated in the %s.
        // %% prdouces % that isnt included in the search
        private static string extractRegex(string pattern, string replacement, Func<string, string> escapor)
        {
            // return Regex.Replace(pattern, @"%([a-zA-Z0-9]+)%", replacement);
            StringBuilder result = new StringBuilder();

            StringBuilder mem = new StringBuilder();

            bool got = false;

            foreach (char c in pattern)
            {
                if (c == '%')
                {
                    string t = mem.ToString();
                    if (false == string.IsNullOrEmpty(t))
                    {
                        string str = got ? replacement.Replace("${1}", t) : escapor(t);
                        result.Append(str);
                        mem = new StringBuilder();
                    }
                    else if (got)
                    {
                        result.Append(escapor("%"));
                    }
                    got = !got;
                }
                else
                {
                    if (got && char.IsWhiteSpace(c))
                    {
                        string s = mem.ToString();
                        got = false;
                        mem = new StringBuilder("%" + s);
                    }
                    mem.Append(c);
                }
            }

            string extra = escapor(mem.ToString());
            if (got) extra = escapor("%") + extra;

            return result.ToString() + extra;
        }
    }
}
