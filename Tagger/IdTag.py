using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using PrettyGood.Util;
using HundredMilesSoftware.UltraID3Lib;

namespace Tagger
{
    public class IdTag
    {
        public string Artist;
        public string Title;
        public string Album;
        public string TrackNumber;
        public string Genre;
        public string Year;
        public string Comments;

        public bool IsCover;
        public bool IsRemix;
        public string TotalTracks;

        public void readTagsFromFile(string FilePath)
        {
            UltraID3 id = new UltraID3();
            id.Read(FilePath);
            Artist = id.ID3v1Tag.Artist;
            Title = id.ID3v1Tag.Title;
            Album = id.ID3v1Tag.Album;
            TrackNumber = id.ID3v1Tag.TrackNum.ToString();
            Genre = id.ID3v1Tag.GenreName;
            Year = id.ID3v1Tag.Year.ToString();
            Comments = id.ID3v1Tag.Comments;

            read(ref Artist, id.ID3v2Tag.Artist);
            read(ref Title, id.ID3v2Tag.Title);
            read(ref Album, id.ID3v2Tag.Album);
            read(ref TrackNumber, id.ID3v2Tag.TrackNum.ToString());
            read(ref Genre, id.ID3v2Tag.Genre);
            read(ref Year, id.ID3v2Tag.Year.ToString());
            read(ref Comments, id.ID3v2Tag.Comments);

            IsCover = id.ID3v2Tag.IsCover;
            IsRemix = id.ID3v2Tag.IsRemix;
            TotalTracks = id.ID3v2Tag.TrackCount.ToString();
            fix();
        }

        private static void read(ref string str, string v)
        {
            if (false == string.IsNullOrEmpty(v)) str = v;
        }

        public void saveTagsToFile(string FilePath)
        {
        }

        internal void readTagsFromDict(Dictionary<string, string> data)
        {
            Read(ref Artist, data, "artist");
            Read(ref Title, data, "title");
            Read(ref Album, data, "album");
            Read(ref Genre, data, "genre");
            Read(ref Comments, data, "comment");

            Read(ref TrackNumber, data, "track");
            Read(ref Year, data, "year");
            //bool IsCover;
            //bool IsRemix;
            Read(ref TotalTracks, data, "total");
            fix();
        }

        void fix()
        {
            Fix(ref Artist, x => x.RemoveUnderscores().Trim().Capitalize());
            Fix(ref Title, x => x.RemoveUnderscores().Trim().Capitalize());
            Fix(ref Album, x => x.RemoveUnderscores().Trim().Capitalize());
            Fix(ref Genre, x => x.RemoveUnderscores().Trim().Capitalize());
            Fix(ref Comments, x => x.RemoveUnderscores().Trim());

            Fix(ref TrackNumber, x => x.RemoveUnderscores().Trim().RemoveLeadingZeros());
            Fix(ref Year, x => workoutYear(x.RemoveUnderscores().Trim()));
            //bool IsCover;
            //bool IsRemix;
            Fix(ref TotalTracks, x => x.RemoveUnderscores().Trim().RemoveLeadingZeros());
        }

        private string workoutYear(string p)
        {
            p = p.RemoveLeadingZeros();
            if (p.Length == 0) return "2000";
            if (p.Length == 4) return p;
            if (p.Length == 3) return p;
            else
            {
                int n;
                if (int.TryParse(p, out n))
                {
                    string century = n < 30 ? "20" : "19";
                    if(p.Length == 1 ) century += "0";
                    return century + p;
                }
                else return p; // invalid year
            }
        }

        private static void Fix(ref string var, Func<string, string> fixer)
        {
            if (string.IsNullOrEmpty(var)) return;
            var = fixer(var);
        }

        private static void Read(ref string var, Dictionary<string, string> data, string name)
        {
            if (data.ContainsKey(name))
            {
                var = data[name].Trim();
            }
            else
            {
                var = null;
            }
        }

        internal bool seemsValid()
        {
            if (string.IsNullOrEmpty(Artist)) return false;
            if (string.IsNullOrEmpty(Title)) return false;
            if (IsEmpty(Album)) return false;
            if (IsEmpty(TrackNumber)) return false;
            else if (IsPositiveNumber(TrackNumber) == false) return false;
            if (IsEmpty(Genre)) return false;
            if (IsEmpty(Year)) return false;
            if (IsEmpty(Comments)) return false;
            //bool IsCover;
            //bool IsRemix;
            if (IsEmpty(TotalTracks)) return false;
            else if (IsPositiveNumber(TotalTracks) == false) return false;

            return true;
        }

        private bool IsPositiveNumber(string s)
        {
            if (s == null) return true;
            int number;
            if (int.TryParse(Strings.RemoveLeadingZeros(s), out number))
            {
                return number >= 0;
            }
            else return false;
        }

        private static bool IsEmpty(string s)
        {
            if (s == null) return false;
            return string.IsNullOrEmpty(s);
        }

        internal int getModification()
        {
            int mod = 0;
            if (string.IsNullOrEmpty(Title) == false && Title.ToLower().Contains("mp3")) mod -= 1;
            if (string.IsNullOrEmpty(Title) == false && Title.Contains("-")) mod -= 1;
            if (string.IsNullOrEmpty(Title) == false && Title.Contains("<")) mod -= 2;
            if (string.IsNullOrEmpty(Title) == false && Title.Contains(">")) mod -= 2;
            return mod;
        }

        private static bool IsValidName(string n)
        {
            string s = string.IsNullOrEmpty(n) ? string.Empty : n.RemoveUnderscores().Trim();
            return string.IsNullOrEmpty(s) == false;
        }
        private static bool IsValidNumber(string n)
        {
            string s = string.IsNullOrEmpty(n) ? string.Empty : n.RemoveUnderscores().Trim().RemoveLeadingZeros();
            int dummy;
            return string.IsNullOrEmpty(n) == false && int.TryParse(s, out dummy);
        }

        internal void merge(IdTag t)
        {
            Merge(ref Artist, IsValidName, t.Artist);
            Merge(ref Title, IsValidName, t.Title);
            Merge(ref Album, IsValidName, t.Album);
            Merge(ref Genre, IsValidName, t.Genre);
            Merge(ref Comments, IsValidName, t.Comments);

            Merge(ref TrackNumber, IsValidNumber, t.TrackNumber);
            Merge(ref Year, IsValidNumber, t.Year);
            IsCover = t.IsCover;
            IsRemix = t.IsRemix;
            Merge(ref TotalTracks, IsValidNumber, t.TotalTracks);
        }

        private void Merge(ref string member, Func<string, bool> isValid, string value)
        {
            /*
             * m | v | asign
             * --|---|---
             * 0 | 0 | don't care
             * 0 | 1 | 1
             * 1 | 0 | 0  <--- MARKED
             * 1 | 1 | 1
             */

            // this satisfies the MARKED condition
            if (isValid(member) == true && isValid(value) == false) return;

            // possibly do a actual merge if both are considered valid...?
            member = value;
        }
    }
}
