using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using MusicBrainz;
using PrettyGood.Util;

namespace Tagger
{
    class TagValidator
    {
        public bool validate(IdTag tag)
        {
            Artist artist = null;
            if (string.IsNullOrEmpty(tag.Artist) == false) artist = getArtist(tag.Artist);
            if (artist == null) return false;

            Release album = null;
            if (string.IsNullOrEmpty(tag.Album) == false) album = getRelease(artist, tag.Album);

            Track track = null;
            if (string.IsNullOrEmpty(tag.Title))
            {
                int num = int.Parse(tag.TrackNumber.RemoveLeadingZeros());
                num %= 100;
                track = album.GetTracks()[num];
            }
            else
            {
                foreach (var t in Track.Query(tag.Title, artist.GetName()))
                {
                    track = t;
                    break;
                }
            }

            if (track == null) return false;

            if (album == null)
            {
                foreach (var r in track.GetReleases())
                {
                    album = r;
                    break;
                }
            }

            tag.Artist = artist.GetName();
            tag.Album = album.GetTitle();
            tag.TrackNumber = track.GetTrackNumber(album).ToString();
            tag.TotalTracks = album.GetTracks().Count.ToString();
            //tag.Year = album.GetReleaseRelations()[0].BeginDate;

            return true;
        }

        private Release getRelease(Artist artist, string a)
        {
            string album = a.ToLower();
            foreach (Release r in artist.GetReleases())
            {
                if (album == r.GetTitle().ToLower()) return r;
            }
            return null;
        }

        private Artist getArtist(string art)
        {
            string artist = art.ToLower();
            if (artists.ContainsKey(artist)) return artists[artist];
            Artist info = null;

            System.Threading.Thread.Sleep(500);
            foreach (Artist a in Artist.Query(artist))
            {
                string name = a.GetName();
                if (artist.Contains(name.ToLower()))
                {
                    info = a;
                    break;
                }
            }

            artists.Add(artist, info);

            return info;
        }

        Dictionary<string, Artist> artists = new Dictionary<string, Artist>();
    }
}
