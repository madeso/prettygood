using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace Tagger
{
    public partial class SongAdder : Form
    {
        public SongAdder()
        {
            InitializeComponent();
        }

        private void dWorker_DoWork(object sender, DoWorkEventArgs e)
        {
            try
            {
                dWorker.ReportProgress(0, "Starting...");
                var arg = (Arg)e.Argument;
                foreach (var file in arg.files)
                {
                    if (File.Exists(file))
                    {
                        dWorker.ReportProgress(0, file);
                        if (dWorker.CancellationPending) return;
                        arg.adder(file);
                    }
                    else if (Directory.Exists(file))
                    {
                        dWorker.ReportProgress(0, "Looking at files...");
                        foreach (FileInfo path in new DirectoryInfo(file).GetFiles("*", SearchOption.AllDirectories))
                        {
                            dWorker.ReportProgress(0, path.FullName);
                            if (dWorker.CancellationPending) return;
                            arg.adder(path.FullName);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                e.Result = ex;
            }
        }

        private void dWorker_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            dCurrent.Text = (string)e.UserState;
        }

        private void dWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            Close();
            if (e.Result != null)
            {
                throw (Exception)e.Result;
            }
        }

        private void dAbort_Click(object sender, EventArgs e)
        {
            dAbort.Enabled = false;
            dWorker.CancelAsync();
        }

        class Arg
        {
            public List<string> files;
            public Action<string> adder;
        }

        internal static void AddTo(IEnumerable<string> files, Action<string> adder)
        {
            SongAdder a = new SongAdder();
            a.start(new Arg { files = new List<string>(files), adder = adder });
        }

        private void start(Arg arg)
        {
            dWorker.RunWorkerAsync(arg);
            ShowDialog();
        }
    }
}
