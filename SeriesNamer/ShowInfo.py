using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace SeriesNamer
{
    public class ShowInfo
    {
        private string path;

        public ShowInfo(string path)
        {
            this.path = path;
        }

        public string FilePath
        {
            get
            {
                return path;
            }
        }

        public void moveTo(string newPath)
        {
            File.Move(path, newPath);
            path = newPath;
        }

        Dictionary<string, string> attributes = new Dictionary<string, string>();

        public string this[string name, string def]
        {
            get
            {
                string n = name.ToLower();
                if (n == "path") return path;
                else if (attributes.ContainsKey(n)) return attributes[n];
                else return def;
            }
        }

        public string this[string name]
        {
            get
            {
                return this[name, ""];
            }
            set
            {
                string n = name.ToLower();
                if (n == "path") return;
                else attributes[n] = value;
            }
        }

        internal List<string> match(List<string> cols)
        {
            List<string> vals = new List<string>();
            foreach (string name in cols)
            {
                vals.Add(this[name]);
            }
            return vals;
        }

        public IEnumerable<string> AttributeNames
        {
            get
            {
                yield return "path";
                foreach (KeyValuePair<string, string> kv in attributes)
                {
                    yield return kv.Key;
                }
            }
        }

        public IEnumerable<KeyValuePair<string, string>> Attributes
        {
            get
            {
                return attributes;
            }
        }

        internal void setupAttributes(string p)
        {
            attributes.Clear();
            string name = GetFileName(FilePath, NumberOfseperatorsIn(p));
            Dictionary<string, string> data = Extractor.extract(p, name);
            foreach (KeyValuePair<string, string> kvp in data)
            {
                this[kvp.Key] = kvp.Value;
            }
        }

        private static string GetFileName(string path, int seperatorCount)
        {
            StringBuilder sb = new StringBuilder();

            DirectoryInfo d = new FileInfo(path).Directory;
            for (int s = 0; s < seperatorCount; ++s)
            {
                sb.Insert(0, Path.DirectorySeparatorChar);
                sb.Insert(0, d.Name);
                d = d.Parent;
            }

            sb.Append(Path.GetFileNameWithoutExtension(path));
            
            return sb.ToString();
        }

        static int NumberOfseperatorsIn(string s)
        {
            int count = 0;
            foreach (char c in s)
            {
                if (c == Path.DirectorySeparatorChar) ++count;
            }
            return count;
        }

        internal static HashSet<string> ExtractUsedAttributes(IEnumerable<ShowInfo> Infos)
        {
            HashSet<string> set = new HashSet<string>();
            foreach (ShowInfo sh in Infos)
            {
                foreach (string s in sh.AttributeNames)
                {
                    if (false == set.Contains(s)) set.Add(s);
                }
            }
            return set;
        }

        internal static IEnumerable<string> AttributeFor(IEnumerable<ShowInfo> infos, string s)
        {
            foreach (ShowInfo sh in infos)
            {
                yield return sh[s];
            }
        }
    }
}
