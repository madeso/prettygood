using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using PrettyGood.LastFm;
using PrettyGood.Util;

namespace LastFmApp
{
    public partial class AlbumSearch : Form
    {
        public AlbumSearch(MainWindow.Data data)
        {
            InitializeComponent();

            app = new PrettyGood.LastFm.LastFm(data.ApiKey);
        }

        PrettyGood.LastFm.LastFm app;

        private void dSearch_Click(object sender, EventArgs e)
        {
            dResult.ClearObjects();
            try
            {
                dResult.SetObjects(app.album.search(dAlbum.Text));
            }
            catch (Error err)
            {
                Gui.error(err.Message);
            }
        }
    }
}
