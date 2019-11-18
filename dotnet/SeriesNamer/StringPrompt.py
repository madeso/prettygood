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
    public partial class StringPrompt : Form
    {
        private StringPrompt()
        {
            InitializeComponent();
        }

        private void dOk_Click(object sender, EventArgs e)
        {
            DialogResult = DialogResult.OK;
            Close();
        }

        private void dCancel_Click(object sender, EventArgs e)
        {
            DialogResult = DialogResult.Cancel;
            Close();
        }

        public static string Show(string title, string caption, string start)
        {
            StringPrompt p = new StringPrompt();
            p.Text = title;
            p.dInfo.Text = caption;
            p.dInput.Text = start;
            return p.ShowDialog() == DialogResult.OK
                ? p.dInput.Text
                : string.Empty;
        }
    }
}
