using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Feed;

namespace Seymour
{
	public class ProviderList
	{
		List<ItemProvider> providers = new List<ItemProvider>();

		internal CurrentData provide(ref ItemProvider ap, string doc)
		{
			if (ap == null)
			{
				foreach (ItemProvider p in providers)
				{
					CurrentData d = p.sample(doc);
					if (d != null)
					{
						ap = p;
						return d;
					}
				}

				ap = new NullItemProvider();
				return null;
			}
			else
			{
				return ap.sample(doc);
			}
		}

		internal void add(IEnumerable<ItemProvider> ps)
		{
			foreach (ItemProvider p in ps)
			{
				providers.Add(p);
			}
		}
	}
}
