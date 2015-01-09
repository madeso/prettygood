using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Tagger
{
	public class TagMatch
	{
		private IdTag tag = new IdTag();
		public IdTag Tag
		{
			get
			{
				return tag;
			}
		}
		public IdTag original = new IdTag();
		public Extractor extractor;
		public string Message;
		public bool Valid;
		public bool seemsValid()
		{
			return Valid && tag.seemsValid();
		}
		public int Score
		{
			get
			{
				return extractor.baseScore + tag.getModification();
			}
		}

		internal void readTagsFromDict(Dictionary<string, string> data)
		{
			tag.readTagsFromDict(data);
			original.readTagsFromDict(data);
		}
	}
}
