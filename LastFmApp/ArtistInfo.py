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
	public partial class ArtistInfo : Form
	{
		public ArtistInfo( PrettyGood.LastFm.LastFm app, FoundArtist artist)
		{
			InitializeComponent();

			var info = app.artist.getInfo(artist, null);

			dName.Text = info.name;
			dMbid.Text = info.mbid;
			dUrl.Text = info.url;
			dTags.Text = new StringList().AddRange(info.tags, x => x.name).Combine(new StringListCombiner(", ", " and "));
			dSimilar.Text = new StringList().AddRange(info.similar, x => x.name).Combine(new StringListCombiner(", ", " and "));
			dBio.Text = "";
			if( string.IsNullOrEmpty(info.bio.summary) == false ) dBio.AppendText(info.bio.summary);
		}
	}
}
