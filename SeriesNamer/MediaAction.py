using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SeriesNamer
{
    public class MediaAction
    {
        public string Source { get { return Show.FilePath; } }
        public string Target { set; get; }
        public ShowInfo Show { set; get; }
    }
}
