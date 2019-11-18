using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace SeriesNamer
{
    public partial class MoveTool : Form
    {
        List<ShowInfo> shows;

        public MoveTool(IEnumerable<ShowInfo> shows)
        {
            InitializeComponent();
            this.shows = new List<ShowInfo>(shows);
            updatePreviewWindow();
        }

        private void dBroswseFolder_Click(object sender, EventArgs e)
        {
            if (dFolderBrowse.ShowDialog() == DialogResult.OK)
            {
                dTargetFolder.Text = dFolderBrowse.SelectedPath;
                updatePreviewWindow();
            }
        }

        private IEnumerable<MediaAction> Actions
        {
            get
            {
                string folder = dTargetFolder.Text;
                string patt = dTargetPattern.Text;

                // %series%\s%season%\%episode%-%title% 

                foreach (ShowInfo s in shows)
                {
                    string ss = Safe(folder, patt
                        .Replace("%series%", s["series"])
                        .Replace("%season%", s["season"])
                        .Replace("%title%", s["title"])
                        .Replace("%episode%", Zeroes(2, s["episode"]))
                        );
                    string t = Path.ChangeExtension(ss, Path.GetExtension(s.FilePath));

                    if (s.FilePath != t)
                    {
                        yield return new MediaAction { Target = t, Show = s };
                    }
                }
            }
        }

        private string Zeroes(int c, string s)
        {
            int i;
            if (false == int.TryParse(s, out i)) return s;
            return i.ToString(new string('0', c));
        }

        private static string Safe(string b, string a)
        {
            string[] st = a.Split(new char[] { Path.DirectorySeparatorChar });

            string r = b;

            int c = st.Length;

            for (int i = 0; i < c; ++i)
            {
                char[] invalids = (i == c - 1) ? Path.GetInvalidFileNameChars() : Path.GetInvalidPathChars();
                r = Path.Combine(r, ReplaceAllWithSafe(st[i], invalids).Trim());
            }

            return r;
        }

        private static string ReplaceAllWithSafe(string a, char[] invalids)
        {
            string s = a;
            foreach (char c in AppendInvalidCharacters(invalids))
            {
                s = s.Replace(c, '_');
            }
            return s;
        }

        private static IEnumerable<char> AppendInvalidCharacters(char[] invalids)
        {
            foreach (char c in invalids)
            {
                yield return c;
            }
            yield return '.';
            yield return ':';
            yield return ';';
            yield return '&';
            yield return '%';
        }

        private void dTargetPattern_TextChanged(object sender, EventArgs e)
        {
            updatePreviewWindow();
        }

        private void updatePreviewWindow()
        {
            dResultPreview.Items.Clear();
            foreach (MediaAction ma in Actions)
            {
                ListViewItem it = new ListViewItem(ma.Source);
                it.SubItems.Add(ma.Target);
                dResultPreview.Items.Add(it);
            }
        }

        private void dStartRename_Click(object sender, EventArgs e)
        {
            new MoveProgress().start(Actions);
        }
    }
}
