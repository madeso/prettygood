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
    public partial class UpdateTool : Form
    {
        private bool autoClose = true;
        public UpdateTool(IEnumerable<ShowInfo> infos)
        {
            InitializeComponent();
            var a = new List<ShowInfo>(infos);
            dWork.RunWorkerAsync(a);
        }

        private void dAbort_Click(object sender, EventArgs e)
        {
            if (dWork.IsBusy)
            {
                dWork.CancelAsync();
                dAbort.Enabled = false;
            }
            else
            {
                Close();
            }
        }

        private void dWork_DoWork(object sender, DoWorkEventArgs e)
        {
            tvdb.Database db = new tvdb.Database("B0E69F9968919E02");
            List<ShowInfo> infos = (List<ShowInfo>)e.Argument;
            int index = 0;
            int count = infos.Count;
            foreach (ShowInfo info in infos)
            {
                if (dWork.CancellationPending)
                {
                    e.Cancel = true;
                    db.saveLocalDatabase();
                    return;
                }
                string message = "";

                string series = info["series", string.Empty];
                string season = info["season", string.Empty];
                string episode = info["episode", string.Empty];

                StringSeperator sep = new StringSeperator(", ", " and ", "none");
                StringSeperator values = new StringSeperator(", ", " and ", "none");

                int missing = 0;
                if (string.IsNullOrEmpty(series))
                {
                    sep.Append("series");
                    ++missing;
                }
                else values.Append("series: " + series);

                if (string.IsNullOrEmpty(season))
                {
                    sep.Append("season");
                    ++missing;
                }
                else values.Append("season: " + season);

                if (string.IsNullOrEmpty(episode))
                {
                    sep.Append("episode");
                    ++missing;
                }
                else values.Append("episode: " + episode);

                if (missing == 0)
                {
                    int seasonNumber = 0;
                    int episodeNumber = 0;
                    
                    if (false == int.TryParse(season, out seasonNumber))
                    {
                        message = "Unable to format season to integer for " + series + ": " + season;
                    }
                    else if (false == int.TryParse(episode, out episodeNumber))
                    {
                        message = "Unable to format episode to integer for " + series + " season " + season + ": " + episode;
                    }
                    else
                    {
                        string newSeries;
                        try
                        {
                            string title = db.suggestTitle(series, seasonNumber, episodeNumber, out newSeries);
                            if (series != newSeries)
                            {
                                info["series"] = newSeries;
                            }
                            info["title"] = title;
                        }
                        catch (Exception ex)
                        {
                            message = ex.Message;
                        }
                    }
                }
                else
                {
                    message = "Missing " + sep.ToString() + " and got " + values.ToString() + " from " + info.FilePath + " - nothing done!";
                }

                dWork.ReportProgress((int)(100.0*index/count), message);
                ++index;
            }
            db.saveLocalDatabase();
        }

        private void dWork_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            dProgress.Value = e.ProgressPercentage;
            string message = (string)e.UserState;
            if (false == string.IsNullOrEmpty(message))
            {
                dOutput.AppendText( message + Environment.NewLine );
            }
            autoClose = false;
        }

        private void dWork_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            dAbort.Enabled = true;
            dAbort.Text = "Close";
            if (e.Cancelled)
            {
                Close();
            }

            if (autoClose) Close();
        }
    }
}
