using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SeriesNamer.tvdb
{
    public class Episode
    {
        private int index;
        private string title;
        private string overview;

        public Episode(int index, string title, string overview)
        {
            this.index = index;
            this.title = title;
            this.overview = overview;
        }

        public string Title
        {
            get
            {
                return title;
            }
        }

        public int Index
        {
            get
            {
                return index;
            }
        }

        public string Overview
        {
            get
            {
                return overview;
            }
        }
    }
}
