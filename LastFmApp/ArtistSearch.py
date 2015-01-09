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
	public partial class ArtistSearch : Form
	{
		public ArtistSearch(MainWindow.Data data)
		{
			InitializeComponent();

			app = new PrettyGood.LastFm.LastFm(data.ApiKey);

			foreach (var ci in PrettyGood.LastFm.LastFm.Languages)
			{
				dLanguage.Items.Add(ci);
			}
		}

		PrettyGood.LastFm.LastFm app;

		private void dSearch_Click(object sender, EventArgs e)
		{
			try
			{
				dArtists.ClearObjects();
				dArtists.SetObjects(app.artist.search(dArtistName.Text, dMusicBrainzId.Text, selectedLanguage()));
			}
			catch (Error err)
			{
				Gui.error(err.message);
			}
		}

		private System.Globalization.CultureInfo selectedLanguage()
		{
			return (System.Globalization.CultureInfo)dLanguage.SelectedItem;
		}

		private void dArtists_DoubleClick(object sender, EventArgs e)
		{
			var artist = (FoundArtist)dArtists.SelectedObject;
			//var info = app.artist.getInfo(artist, selectedLanguage());
			new ArtistInfo(app, artist).ShowDialog();
		}
	}
}
