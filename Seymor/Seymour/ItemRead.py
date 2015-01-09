using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Feed;
using System.Windows.Forms;
using PrettyGood.Util;

namespace Seymour
{
    public class ItemRead
    {
        internal void write(ElementBuilder b)
        {
            b
                .attribute("title", Item.Title)
                .attribute("link", Item.Link)
                .attribute("id", Item.Id)
                .attribute("updated", Item.Updated.ToFileTimeUtc().ToString())
                .cdata(Item.Summary);
        }

        internal static ItemRead Load(System.Xml.XmlElement e, Channel c)
        {
            return new ItemRead(new Item {
                  Title = Xml.GetAttributeString(e, "title")
                , Link = Xml.GetAttributeString(e, "link")
                , Id = Xml.GetAttributeString(e, "id")
                , Updated = DateTime.FromFileTimeUtc( long.Parse(Xml.GetAttributeString(e, "updated")))
                , Summary = Xml.GetFirstText(e)
            }
                    , c);
        }

        public ItemRead(Item i, Channel c)
        {
            Item = i;
            Channel = c;
        }
        public Item Item { get; set; }
        public bool Read
        {
            get
            {
                return Channel.isRead(this);
            }
        }
        public bool read()
        {
            return Channel.read(this);
        }
        public Channel Channel { get; set; }

        public string LocalPath
        {
            get
            {
                return FileUtil.GetUserPathFor()
                    .dir(Channel.Title.Trim().ToLower())
                    .dir(Item.Updated.Year.ToString())
                    .dir(Item.Updated.ToString("MMM", System.Globalization.CultureInfo.CreateSpecificCulture("en-US")))
                    .file(Item.Title.Trim().ToLower(), "html");
            }
        }

        public List<string> Html
        {
            get
            {
                List<string> lines = new List<string>();

                lines.Add("<html>");
                lines.Add("<body>");
                lines.Add(Item.Summary);
                lines.Add("</body>");
                lines.Add("</html>");

                return lines;
            }
        }
    }
}
