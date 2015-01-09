using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace LastFmApp
{
	public partial class MainWindow : Form
	{
		public MainWindow()
		{
			InitializeComponent();
			PrettyGood.Util.App.Setup("codingatlunch", "LastFM demo", "lastfmdemo");
		}

		public class Data
		{
			public string ApiKey;
			public string User;
			public string Password;
		}

		protected Data FormData
		{
			get
			{
				return new Data { ApiKey = dApiKey.Text, User = dUser.Text, Password = dPassword.Text };
			}
		}

		private void dSearchArtist_Click(object sender, EventArgs e)
		{
			new ArtistSearch(FormData).ShowDialog();
		}

		private void dSearchAlbum_Click(object sender, EventArgs e)
		{
			new AlbumSearch(FormData).ShowDialog();
		}
	}
}
