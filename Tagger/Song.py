using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using PrettyGood.Util;

namespace Tagger
{
	public class Song
	{
		private string Resolve(Func<IdTag, string> get)
		{
			string s = get(tags);
			if( string.IsNullOrEmpty(s) ) return "<empty>";
			else return s;
		}

		private void Set(Action<IdTag> set)
		{
			set(tags);
		}

		public string FilePath;

		// v1
		public string Artist
		{
			get
			{
				return Resolve(x => x.Artist);
			}
			set
			{
				Set(t => t.Artist = value);
			}
		}

		public string Title
		{
			get
			{
				return Resolve(x => x.Title);
			}
			set
			{
				Set(t => t.Title = value);
			}
		}

		public string Album
		{
			get
			{
				return Resolve(x => x.Album);
			}
			set
			{
				Set(t => t.Album = value);
			}
		}
		public string TrackNumber
		{
			get
			{
				return Resolve(x => x.TrackNumber);
			}
			set
			{
				Set(t => t.TrackNumber = value);
			}
		}
		public string Genre
		{
			get
			{
				return Resolve(x => x.Genre);
			}
			set
			{
				Set(t => t.Genre = value);
			}
		}
		public string Year
		{
			get
			{
				return Resolve(x => x.Year);
			}
			set
			{
				Set(t => t.Year = value);
			}
		}
		public string Comments
		{
			get
			{
				return Resolve(x => x.Comments);
			}
			set
			{
				Set(t => t.Comments = value);
			}
		}

		// id v3

		public bool IsCover
		{
			get
			{
				return tags.IsCover;
			}
			set
			{
				tags.IsCover = value;
			}
		}

		public bool IsRemix
		{
			get
			{
				return tags.IsRemix;
			}
			set
			{
				tags.IsRemix = value;
			}
		}

		public string TotalTracks
		{
			get
			{
				return Resolve(x => x.TotalTracks);
			}
			set
			{
				Set(t => t.TotalTracks = value);
			}
		}

		IdTag tags = new IdTag();

		public void readTags()
		{
			IdTag t = new IdTag();
			t.readTagsFromFile(FilePath);
			set(t);
		}

		public void saveTags()
		{
			tags.saveTagsToFile(FilePath);
		}

		internal void set(IdTag t)
		{
			tags.merge(t);
		}
	}
}
