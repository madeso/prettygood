using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using System.IO;
using System.Xml.XPath;

namespace SeriesNamer
{
    public static class Xml
    {
        public static bool HasAttribute(XmlElement element, string search)
        {
            XmlAttribute attribute = element.Attributes[search];
            return attribute != null;
        }

        public static string GetAttributeString(XmlElement element, string name)
        {
            XmlAttribute attribute = element.Attributes[name];
            if (attribute == null) throw new Exception(element.Name + " is missing text attribute \"" + name + "\"");
            else return attribute.Value;
        }

        public static IEnumerable<XmlElement> ElementsNamed(XmlNode root, string childName)
        {
            foreach (XmlNode node in root.ChildNodes)
            {
                XmlElement el = node as XmlElement;
                if (el == null) continue;
                if (el.Name != childName) continue;
                yield return el;
            }
        }

        public static IEnumerable<XmlElement> Elements(XmlNode root)
        {
            foreach (XmlNode node in root.ChildNodes)
            {
                XmlElement el = node as XmlElement;
                if (el == null) continue;
                yield return el;
            }
        }

        private const string kValueType = "id";

        public static IEnumerable<XmlElement> ElementsNamed(XmlNode root, string childName, string valueName)
        {
            foreach (XmlNode node in root.ChildNodes)
            {
                XmlElement el = node as XmlElement;
                if (el == null) continue;
                if (el.Name != childName) continue;
                if (HasAttribute(el, kValueType) == false) continue;
                string val = GetAttributeString(el, kValueType);
                if (val != valueName) continue;
                yield return el;
            }
        }

        public static XmlElement Open(string path, string p)
        {
            return Open(FromFile(path), p);
        }

        public static IEnumerable<XmlElement> Enumerate(XmlNode root, string path)
        {
            string[] elements = path.Split("/".ToCharArray());

            List<XmlNode> active = new List<XmlNode>();
            List<XmlNode> future = new List<XmlNode>();
            active.Add(root);
            foreach (string p in elements)
            {
                foreach (XmlNode a in active)
                {
                    foreach (XmlElement e in ElementsNamed(a, p))
                    {
                        future.Add(e);
                    }
                }
                active.Clear();
                CSharp.Swap(ref active, ref future);
            }

            foreach (XmlNode node in active)
            {
                yield return (XmlElement)node;
            }
        }
        public static XmlElement FirstOrNull(IEnumerable<XmlElement> elements)
        {
            foreach (XmlElement e in elements)
            {
                return e;
            }
            return null;
        }
        public static XmlElement FirstOrNull(XmlNode root, string path)
        {
            return FirstOrNull(Enumerate(root, path));
        }

        public static XmlElement Open(Loader path, string p)
        {
            try
            {
                XmlDocument doc = Open(path);
                XmlElement el = FirstOrNull(doc, p);
                if (el == null) throw new Exception(p + " not found in " + path);
                else return el;
            }
            catch (Exception e)
            {
                throw new Exception("while reading " + path + " for node: " + p, e);
            }
        }

        public interface Loader
        {
            Stream load();
        }

        public static Loader FromFile(string path)
        {
            return new FileLoader(path);
        }
        public static Loader FromSource(string source)
        {
            return new SourceLoader(source);
        }

        private class FileLoader : Loader
        {
            private readonly string path;
            public FileLoader(string path)
            {
                this.path = path;
            }

            public Stream load()
            {
                return File.Open(path, FileMode.Open);
            }
            public override string ToString()
            {
                return path;
            }
        }
        private class SourceLoader : Loader
        {
            private readonly string source;
            public SourceLoader(string source)
            {
                this.source = source;
            }

            public Stream load()
            {
                return new MemoryStream(System.Text.ASCIIEncoding.ASCII.GetBytes(source));
            }

            public override string ToString()
            {
                return Strings.FirstChars(source, 10);
            }
        }

        private static XmlDocument Open(Loader loader)
        {
            try
            {
                XmlDocument doc = new XmlDocument();
                using (Stream s = loader.load())
                {
                    doc.Load(s);
                }
                return doc;
            }
            catch (Exception e)
            {
                throw new Exception("while opening xml: " + loader, e);
            }
        }

        public static IEnumerable<KeyValuePair<string, string>> Attributes(XmlElement el)
        {
            foreach (XmlAttribute a in el.Attributes)
            {
                yield return new KeyValuePair<string, string>(a.Name, a.Value);
            }
        }

        public static string NameOf(XmlElement element)
        {
            string attribute = "";
            if (HasAttribute(element, "id"))
            {
                attribute = "[" + GetAttributeString(element, "id") + "]";
            }
            return element.Name + attribute; ;
        }

        public static string PathOf(XmlElement element)
        {
            XmlElement c = element;
            string result = "";
            while (c != null)
            {
                result = NameOf(c) + "/" + result;
            }
            return result;
        }

        public static Dictionary<string, XmlElement> MapElements(XmlElement root, string type, string key)
        {
            if (root == null) return new Dictionary<string, XmlElement>();
            Dictionary<string, XmlElement> map = new Dictionary<string, XmlElement>();
            foreach (XmlElement module in Xml.ElementsNamed(root, type))
            {
                string name = Xml.GetAttributeString(module, key);
                map.Add(name, module);
            }
            return map;
        }

        public static string GetAttributeString(XmlElement element, string name, string def)
        {
            if (def == null || HasAttribute(element, name)) return GetAttributeString(element, name);
            else return def;
        }

        public static XmlElement AppendElement(XmlDocument doc, XmlNode cont, string name)
        {
            XmlElement el = doc.CreateElement(name);
            cont.AppendChild(el);
            return el;
        }
        public static void AddAttribute(XmlDocument doc, XmlNode elem, string name, string value)
        {
            XmlAttribute a = doc.CreateAttribute(name);
            a.InnerText = value;
            elem.Attributes.Append(a);
        }

        public static string GetTextOfSubElement(XmlNode node, string p)
        {
            string res = GetTextOfSubElementOrNull(node, p);
            if (res == null) throw new Exception("node is missing " + p + ", a requested sub node");
            else return res;
        }

        private static string GetSmartText(XmlNode el)
        {
            if (el is XmlText)
            {
                XmlText text = (XmlText)el;
                return text.Value;
            }
            else if (el is XmlCDataSection)
            {
                XmlCDataSection text = (XmlCDataSection)el;
                return text.Value;
            }
            else throw new Exception("Failed to get smart text of node");
        }

        public static string GetTextOfSubElementOrNull(XmlNode node, string p)
        {
            XmlElement el = GetFirstChild(node, p);
            if (el == null) return null;
            if (el.FirstChild == null) return null;
            return GetSmartText(el.FirstChild);
        }

        internal static XPathDocument OpenXpath(Loader loader)
        {
            try
            {
                using (Stream s = loader.load())
                {
                    XPathDocument doc = new XPathDocument(s);
                    return doc;
                }
            }
            catch (Exception e)
            {
                throw new Exception("while opening xml: " + loader, e);
            }
        }

        public static XmlElement GetFirstChild(XmlNode root, string p)
        {
            XmlElement e = FirstOrNull(ElementsNamed(root, p));
            if (e == null) throw new Exception("Missing element named " + p);
            return e;
        }
    }
}
