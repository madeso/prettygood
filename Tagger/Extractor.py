using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using PrettyGood.Util;
using System.IO;

namespace Tagger
{
	public class Extractor
	{
		public KeyValueExtractor logic;
		public int baseScore = 0;
		public bool removeUnderscores = false;

		public string Pattern
		{
			get
			{
				return logic.ToString();
			}
			set
			{
				logic = KeyValueExtractor.Compile(value);
				var c = logic.CalculateComplexity();
				baseScore = c.Arguments + c.Verifiers * 2;
				removeUnderscores = logic.countInText( x => x.CountCharacters(ch=>ch=='_')) == 0;
			}
		}

		public TagMatch extract(FileInfo file)
		{
			string message;
			var data = logic.extract(file, out message);
			if (data == null) return null;
			TagMatch tag = new TagMatch();
			tag.readTagsFromDict(data);
			tag.extractor = this;
			tag.Valid = string.IsNullOrEmpty(message);
			tag.Message = message;
			return tag;
		}

		internal string cleanup(string p)
		{
			string r = p;
			if (removeUnderscores) r = r.RemoveUnderscores();
			return r;
		}

		internal Extractor deepClone()
		{
			Extractor e = new Extractor();
			e.Pattern = Pattern;
			e.baseScore = baseScore;
			e.removeUnderscores = removeUnderscores;
			return e;
		}
	}
}
