using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Net;
using System.Diagnostics;
using System.Xml;

namespace PrettyGood.Util
{
    public static class Web
    {
        public static bool PageExist(string url)
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            //request.ReadWriteTimeout = 1000;
            request.AllowAutoRedirect = true;

            // execute the request
            try
            {
                using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
                {
                    // we will read data via the response stream
                    using (Stream s = response.GetResponseStream())
                    {
                        return true;
                    }
                }
            }
            catch (WebException ex)
            {
                if (ex.Status == WebExceptionStatus.ProtocolError)
                {
                    return false;
                }
                else throw ex;
            }
        }

        public static bool IsUrl(string text)
        {
            Uri.IsWellFormedUriString(text, UriKind.Absolute);
            return true;
        }

        public static string FetchString(string url, ref Encoding enc)
        {
            WebRequest request = WebRequest.Create(url);
            request.Credentials = CredentialCache.DefaultCredentials;
            
            WebResponse response;
            WebException exp = null;

            try
            {
                response = request.GetResponse();
            }
            catch(WebException web)
            {
                exp = web;
                response = web.Response;
                if (response == null) throw web;
            }
            
            Stream dataStream = response.GetResponseStream();
            StreamReader reader = new StreamReader(dataStream);
            string responseFromServer = reader.ReadToEnd();
            reader.Close();
            response.Close();

            // if we didnt get any response and we failed earlier, rethrow that web-error
            if (string.IsNullOrEmpty(responseFromServer) && exp != null) throw exp;

            return responseFromServer;
        }

        public static string FetchStringOld(string url, ref Encoding enc)
        {
            // used to build entire input
            int count = 0;

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.ReadWriteTimeout = 1000;

            // execute the request
            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            {
                // we will read data via the response stream
                using (Stream resStream = response.GetResponseStream())
                {
                    MemoryStream ms = new MemoryStream();
                    byte[] buf = new byte[8192];
                    do
                    {
                        count = resStream.Read(buf, 0, buf.Length);
                        ms.Write(buf, 0, count);
                    }
                    while (count > 0);
                    if (false == string.IsNullOrEmpty(response.CharacterSet)) enc = Encoding.GetEncoding(response.CharacterSet);

                    string temp = GetString(ms, enc);
                    Encoding oldEnc = enc;
                    try
                    {
                        XmlDocument doc = new XmlDocument();
                        Xml.FromSource(temp).load(doc);
                        enc = Xml.GetEncoding(doc, oldEnc);
                    }
                    catch (Exception) {}
                    if (enc != oldEnc) temp = GetString(ms, enc);

                    return temp;
                }
            }
        }

        private static string GetString(MemoryStream ms, Encoding enc)
        {
            ms.Seek(0, SeekOrigin.Begin);
            int count = 0;
            byte[] buf = new byte[8192];
            StringBuilder sb = new StringBuilder();
            do
            {
                count = ms.Read(buf, 0, buf.Length);
                if (count > 0)
                {
                    string tempString = enc.GetString(buf, 0, count);
                    sb.Append(tempString);
                }
            } while (count > 0);

            return sb.ToString();
        }

        public static void OpenUrl(string url)
        {
            Process.Start(url);
        }

        public static void DownloadFile(string url, string target)
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.ReadWriteTimeout = 1000;

            // execute the request
            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            {
                // we will read data via the response stream
                using (Stream resStream = response.GetResponseStream())
                {
                    using (FileStream fs = File.Open(target, FileMode.Create))
                    {
                        byte[] buf = new byte[8192];
                        int count = 0;
                        do
                        {
                            count = resStream.Read(buf, 0, buf.Length);

                            if (count != 0)
                            {
                                fs.Write(buf, 0, count);
                            }
                        }
                        while (count > 0);
                    }
                }
            }
        }

        public static string Escape(string p)
        {
            return p.Replace(" ", "%20");
        }
    }
}