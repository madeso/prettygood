using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace SeriesNamer
{
    public partial class AttributeTools : Form
    {
        List<ShowInfo> infos;

        public AttributeTools(IEnumerable<ShowInfo> infos)
        {
            InitializeComponent();
            this.infos = new List<ShowInfo>(infos);

            updateView();
        }

        private void updateView()
        {
            dAttributes.Items.Clear();
            HashSet<string> attributes = ShowInfo.ExtractUsedAttributes(infos);
            foreach (string s in attributes)
            {
                ListViewItem it = new ListViewItem();
                it.Text = getSmartValueFor(s);
                it.SubItems.Add(s);
                dAttributes.Items.Add(it);
            }
        }

        const int kMax = 3;

        private string getSmartValueFor(string name)
        {
            List<string> values = new List<string>(StringUtils.Unique(ShowInfo.AttributeFor(infos, name)));
            
            bool tooboig = (values.Count > kMax);
            StringSeperator sep = new StringSeperator(", ", tooboig ? ", " : " and ", "<empty>");

            int count=0;
            foreach(string v in values)
            {
                sep.Append(v);
                if( count > kMax ) break;
                ++count;
            }
            if( tooboig ) sep.Append("...");

            return sep.ToString();
        }

        private void capitalizeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            apply( x => Capitalize(x) );
            updateItems();
        }

        private void updateItems()
        {
            updateView();
        }

        private string Capitalize(string x)
        {
            bool doCap = true;

            StringBuilder b = new StringBuilder();
            foreach (char c in x)
            {
                b.Append(doCap ? char.ToUpper(c) : c);
                doCap = false;
                if (char.IsWhiteSpace(c)) doCap = true;
            }
            return b.ToString();
        }

        private void apply(Func<string, string> action)
        {
            foreach (ListViewItem it in dAttributes.SelectedItems)
            {
                string attributename = AttributeNameFor(it);
                foreach (ShowInfo sh in infos)
                {
                    string value = sh[attributename];
                    string newvalue = action(value);
                    sh[attributename] = newvalue;
                }
            }
        }

        private static string AttributeNameFor(ListViewItem it)
        {
            return it.SubItems[1].Text;
        }

        private void trimToolStripMenuItem_Click(object sender, EventArgs e)
        {
            apply(x => x.Trim());
            updateItems();
        }

        private void replaceToolStripMenuItem_Click(object sender, EventArgs e)
        {
            apply(x => Replace(x));
            updateItems();
        }

        private void trimAndReplaceToolStripMenuItem_Click(object sender, EventArgs e)
        {
            apply(x => x.Trim());
            apply(x => Replace(x));
            updateItems();
        }

        private string Replace(string x)
        {
            char space = ' ';
            return x
                .Replace('.', space)
                .Replace('-', space)
                .Replace('_', space);
        }

        private void dAttributes_BeforeLabelEdit(object sender, LabelEditEventArgs e)
        {
            //if (e.Item != 3) e.CancelEdit = true;
        }

        private void dAttributes_AfterLabelEdit(object sender, LabelEditEventArgs e)
        {
            string attribute = AttributeNameFor(dAttributes.Items[e.Item]);
            setAttribute(attribute, e.Label);
            updateItems();
        }

        private void setAttribute(string attributename, string newvalue)
        {
            foreach (ShowInfo sh in infos)
            {
                sh[attributename] = newvalue;
            }
        }

        private void dDone_Click(object sender, EventArgs e)
        {
            DialogResult = DialogResult.OK;
            Close();
        }

        private void newAttributeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string att = StringPrompt.Show("New Attribute?", "Enter the name of the new attribute", "");
            if (string.IsNullOrEmpty(att)) return;
            setAttribute(att, "");
            updateItems();
        }

        private void stripLeadingZeroesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            apply(x => StripLeadingZeroes(x));
            updateItems();
        }

        private static string StripLeadingZeroes(string s)
        {
            return s.Trim().TrimStart('0').TrimStart();
        }
    }
}
