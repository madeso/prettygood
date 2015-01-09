using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using PrettyGood.Util;
using System.IO;

namespace Tagger
{
	public partial class AutoTagger : Form
	{
		AutoCorrector corrector;

		public AutoTagger()
		{
			InitializeComponent();
		}

		private void dTags_MouseDoubleClick(object sender, MouseEventArgs e)
		{
			var t = (TagMatch)dTags.SelectedObject;
			CurrentSong.set( t.Tag );
			corrector.feed(t.Tag, t.original);
			selectNext();
		}

		private void selectNext()
		{
			dSongs.RefreshObject(CurrentSong);
			++index;
			if (index >= songs.Count)
			{
				Close();
				return;
			}
			select();
		}

		private Song CurrentSong
		{
			get
			{
				return songs[index];
			}
		}

		private void select()
		{
			dFileName.Text = CurrentSong.FilePath;
			dTags.ClearObjects();
			foreach (var ext in extractors)
			{
				// .RemoveUnderscores()
				var r = ext.extract(new FileInfo(ext.cleanup(CurrentSong.FilePath)));
				if (r == null) continue;
				corrector.correct(r);
				if (r.seemsValid() == false && dIncludeInvalid.Checked == false) continue;
				dTags.AddObject(r);
			}
		}

		List<Song> songs;
		List<Extractor> extractors;
		int index = 0;
		BrightIdeasSoftware.FastObjectListView dSongs;

		internal static void DoTag(BrightIdeasSoftware.FastObjectListView dSongs, AutoCorrector corrector, List<Extractor> extractors)
		{
			AutoTagger tagger = new AutoTagger();
			tagger.corrector = corrector;
			tagger.songs = new List<Song>( CSharp.Convert(dSongs.SelectedObjects, x=>(Song)x));
            if (tagger.songs.Count == 0) return;
			tagger.extractors = extractors;
			tagger.dSongs = dSongs;
			tagger.select();
			tagger.ShowDialog();
		}

		private void dIncludeInvalid_CheckedChanged(object sender, EventArgs e)
		{
			select();
		}
	}
}
