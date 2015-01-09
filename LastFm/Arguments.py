using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PrettyGood.LastFm
{
	internal class Arguments
	{
		internal Arguments()
		{
		}

		public Arguments arg(string key, string value)
		{
			if (false == string.IsNullOrEmpty(value))
			{
				args.Add(key, value);
			}
			return this;
		}
		public Arguments rarg(string key, string value)
		{
			if (string.IsNullOrEmpty(value)) throw new Exception("Value cannot be empty for " + key);
			args.Add(key, value);
			return this;
		}

		public Arguments lang(System.Globalization.CultureInfo ci)
		{
			return arg("lang", ci == null? null : ci.TwoLetterISOLanguageName);
		}

		internal IEnumerable<KeyValuePair<string, string>> Args
		{
			get
			{
				return args;
			}
		}

		Dictionary<string, string> args = new Dictionary<string, string>();
	}
}
