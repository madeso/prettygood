using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Feed
{
	public abstract class ItemProvider
	{
		// return null if data is "unsuported"
		public abstract CurrentData sample(string doc);
	}
}
