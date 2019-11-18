using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Feed
{
    public class NullItemProvider : ItemProvider
    {
        public override CurrentData sample(string doc)
        {
            return null;
        }
    }
}
