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
    public partial class FromFilename : Form
    {
        static Dictionary<string, int> widths = new Dictionary<string, int>();
        ShowListUtil lu;
        public FromFilename(List<ShowInfo> infos)
        {
            InitializeComponent();

            lu = new ShowListUtil(dResult, widths, 120);
            lu.addSeveral(infos);

            lu.removeAllHeaders();
            lu.addHeadersFromFirst();
            lu.updateAllText();
        }

        private void dPattern_TextChanged(object sender, EventArgs e)
        {
            applyPattern(dPattern.Text);
            lu.removeAllHeaders();
            lu.addHeadersFromFirst();
            lu.updateAllText();
        }

        private void applyPattern(string p)
        {
            foreach (ShowInfo info in lu.AllInfos)
            {
                info.setupAttributes(p);
            }
        }

        private void dDone_Click(object sender, EventArgs e)
        {
            Close();
            DialogResult = DialogResult.OK;
        }
    }
}
