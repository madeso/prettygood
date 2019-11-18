using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Feed
{
    public class Item
    {
        public string Title { get; set; }
        public string Link { get; set; }
        public string Id { get; set; }
        public DateTime Updated { get; set; }
        public string Summary { get; set; }
    }
}
