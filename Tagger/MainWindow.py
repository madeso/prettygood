using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using BrightIdeasSoftware;
using PrettyGood.Util;
using System.IO;
using MusicBrainz;

namespace Tagger
{
	public partial class MainWindow : Form
	{
		public MainWindow()
		{
			InitializeComponent();

			new FileDrop(dSongs, x => addFileOrDirectory(x) );

			extractors.Add(new Extractor { Pattern = "%artist%-%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%\\%artist%-%title%" });
			extractors.Add(new Extractor { Pattern = "%track%-%artist%-%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%\\%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%\\%track%_%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%\\%album%\\%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%-%album%-%track%-%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%-%album%\\%track% %title%" });
			extractors.Add(new Extractor { Pattern = "%artist%\\(%track%) %artist%-%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%-%album%-%junk%\\%artist%-%junk2%-%track%-%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%-%album%\\%track% - %artist% - Keanu" });
			extractors.Add(new Extractor { Pattern = "%artist%-%album%-%year%-%ripper%\\%track%-%artist%-%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%\\%artist% Track %track%" });
			extractors.Add(new Extractor { Pattern = "%artist%-%year%-%album%-%junk%-%ripper%\\%track%-%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%-%album%-%year%\\%track%-%title%-%ripper%" });
			extractors.Add(new Extractor { Pattern = "%artist%-%album%(%year%) -%title%" });
			extractors.Add(new Extractor { Pattern = "%artist%\\%track%-%artist%-_-%title%-mp3-" });
		}

		private void addFileOrDirectory(IEnumerable<string> files)
		{
			SongAdder.AddTo(files, x => addFile(x));
		}

		public void addFile(string file)
		{
			if (Gui.SmartInvoke(dSongs, new { Main = this, File = file }, x => x.Main.addFile(x.File))) return;
			string ext = Path.GetExtension(file).ToLower();
			/*if( ext == ".ini" ) return;
			if (ext == ".jpg") return;
			if (ext == ".m3u") return;
			if (ext == ".nfo") return;
			if (ext == ".nsf") return; // nintendo sound file
			if (ext == ".db") return; // database file, usually thumbs.db
			if (ext == ".sfv") return; // simple file verification
			if (ext == ".url") return; // link
			if (ext == ".url") return; // link
			if (ext != ".mp3") throw new Exception("Unknown extention " + ext + " for " + file);*/
			if (ext != ".mp3") return;
			Song s = new Song { FilePath = file };
			s.readTags();
			dSongs.AddObject(s);
		}

		private void lookupToolStripMenuItem_Click(object sender, EventArgs e)
		{
			AutoTagger.DoTag(dSongs, corrector, extractors);
		}

		List<Extractor> extractors = new List<Extractor>();
		AutoCorrector corrector = new AutoCorrector();

		TagValidator lastfm = new TagValidator();

		private void dSongs_KeyUp(object sender, KeyEventArgs e)
		{
			if (e.KeyCode == Keys.Delete)
			{
				dSongs.RemoveObjects(dSongs.SelectedObjects);
			}
		}

		private void manageExtractorsToolStripMenuItem_Click(object sender, EventArgs e)
		{
			new ExtractorManagerDialog(extractors).ShowDialog();
		}
	}
}
