using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Feed;

namespace Rss
{
	public class EntryPoint
	{
		public IEnumerable<ItemProvider> Providers()
		{
			yield return new RssProvider();
		}
	}
}
