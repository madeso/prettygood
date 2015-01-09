using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void dWork_DoWork(object sender, DoWorkEventArgs e)
        {
            mess("started...");
            var dir = (string)e.Argument;
            work(dir);
            mess("all done!");
        }

        private void work(string dir)
        {
            foreach (var d in Directory.GetDirectories(dir))
            {
                work(d);
            }

            foreach (var f in Directory.GetFiles(dir))
            {
                var fi = new FileInfo(f);
                if ((fi.Attributes & FileAttributes.Hidden) == FileAttributes.Hidden)
                {
                    mess("Setting " + f + " from " + fi.Attributes.ToString() + " to normal");
                    fi.Attributes = FileAttributes.Normal;
                }
            }
        }



        private void mess(string m)
        {
            dWork.ReportProgress(0, m);
        }

        private void dWork_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            dOutput.AppendText((string)e.UserState + Environment.NewLine);
        }

        private void dWork_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            dInput.Enabled = true;
            dGo.Enabled = true;
        }

        private void dGo_Click(object sender, EventArgs e)
        {
            dInput.Enabled = false;
            dGo.Enabled = false;

            dOutput.Text = "";
            dWork.RunWorkerAsync(dInput.Text);
        }
    }
}
