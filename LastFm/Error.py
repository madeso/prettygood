using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using PrettyGood.Util;

namespace PrettyGood.LastFm
{
	public class Error : Exception
	{
		public readonly int error;
		public readonly string message;

		public Error(XmlElement error)
		{
			XmlElement errel = Xml.GetFirstChild(error, "error");
			this.error = int.Parse(Xml.GetAttributeString(errel, "code"));
			this.message = errel.InnerText;
		}

		public override string ToString()
		{
			return "Last.fm error: " + message;
		}
	}
}
