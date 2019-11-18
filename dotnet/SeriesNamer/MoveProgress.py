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
    public partial class MoveProgress : Form
    {
        public MoveProgress()
        {
            InitializeComponent();
        }

        public void start(IEnumerable<MediaAction> ma)
        {
            var m = new List<MediaAction>(ma);
            dWorker.RunWorkerAsync(m); 
            ShowDialog();
        }

        private void dWorker_DoWork(object sender, DoWorkEventArgs e)
        {
            List<MediaAction> mas = (List<MediaAction>)e.Argument;
            int c = mas.Count;

            for(int i=0; i<c; ++i)
            {
                MediaAction m = mas[i];
                if (dWorker.CancellationPending)
                {
                    e.Cancel = true;
                    e.Result = null;
                    return;
                }
                string message = String.Empty;

                if (false == File.Exists(m.Source))
                {
                    message = m.Source + " doesnt exist!";
                }
                else if (false==Path.IsPathRooted(m.Target))
                {
                    message = m.Target + " is not rooted";
                }
                else if (true == File.Exists(m.Target))
                {
                    message = m.Target + " already exist!";
                }
                else
                {
                    DirectoryInfo dir = new FileInfo(m.Target).Directory;
                    FileUtil.MakeSureDirectoryExist(dir);
                    int sub = moveExtra(m.Source, m.Target);
                    if (sub == -1)
                    {
                        message = m.Target + " existing SUB at destination path ";
                    }
                    else
                    {
                        m.Show.moveTo(m.Target);
                        message = m.Target + (sub==1 ? " (& SUB) " : "") + " DONE!";
                    }
                }

                dWorker.ReportProgress((int)(i+1/(float)c), message);
            }
        }

        int moveExtra(string src, string dest)
        {
            string[] ExtraExt = { ".srt", ".sub" };
            foreach (string ext in ExtraExt)
            {
                string s = Path.ChangeExtension(src, ext);
                if (File.Exists(s))
                {
                    string d = Path.ChangeExtension(dest, ext);
                    if (File.Exists(d)) return -1;
                    File.Move(s, d);
                    return 1;
                }
            }

            return 0;
        }

        private void dWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
        }

        private void dWorker_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            dProgress.Value = Math.Min(100,e.ProgressPercentage);
            dResult.AppendText( (string) e.UserState + Environment.NewLine );
        }
    }
}
