using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Xml;

namespace SeriesNamer
{
    public partial class Main : Form
    {
        ShowListUtil lu;
        public Main()
        {
            InitializeComponent();
            lu = new ShowListUtil(dFiles, new Dictionary<string, int>(), 60);
            loadSongs();
        }

        private void dAddFile_Click(object sender, EventArgs e)
        {
            if (dFileBrowse.ShowDialog() == DialogResult.OK)
            {
                foreach (string file in dFileBrowse.FileNames)
                {
                    addFile(file);
                }
                saveSongs();
            }
        }

        private void addFile(string file)
        {
            if (isMovieFile(file))
            {
                lu.addSingle(new ShowInfo(file));
            }
        }

        private bool isMovieFile(string file)
        {
            string ext = Path.GetExtension(file);
            if (ext == ".avi") return true;
            else if (ext == ".divx") return true;
            else if (ext == ".mkv") return true;
            else if (ext == ".ogm") return true;
            else return false;
        }

        private void dAddFolder_Click(object sender, EventArgs e)
        {
            if (dFolderBrowse.ShowDialog() == DialogResult.OK)
            {
                addFolder(dFolderBrowse.SelectedPath);
            }
        }

        private void addFolder(string p)
        {
            foreach (string file in Directory.GetFiles(p, "*.*", SearchOption.AllDirectories))
            {
                addFile(file);
            }
            saveSongs();
        }

        private void tagToolStripMenuItem_Click(object sender, EventArgs e)
        {
            List<ShowInfo> infos = new List<ShowInfo>(lu.SelectedInfos);
            FromFilename st = new FromFilename(infos);
            if (st.ShowDialog() == DialogResult.OK)
            {
                lu.updateAllText(lu.SelectedItems);
                saveSongs();
            }
        }

        private void lookUpInfoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            UpdateTool st = new UpdateTool(lu.SelectedInfos);
            st.ShowDialog();// == DialogResult.OK)
            lu.updateAllText(lu.SelectedItems);
            saveSongs();
        }

        private void attributeToolsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            AttributeTools st = new AttributeTools(lu.SelectedInfos);
            if (st.ShowDialog() == DialogResult.OK)
            {
                lu.updateAllText(lu.SelectedItems);
                saveSongs();
            }
        }



        private string getShowDir()
        {
            return Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "SeriesNamer");
        }

        private string getShowPath()
        {
            return Path.Combine(getShowDir(), "shows.xml");
        }

        private void loadSongs()
        {
            try
            {
                XmlElement root = Xml.Open(Xml.FromFile(getShowPath()), "media");
                foreach (XmlElement e in Xml.ElementsNamed(root, "show"))
                {
                    ShowInfo s = new ShowInfo(Xml.GetAttributeString(e, "path"));
                    foreach (XmlElement a in Xml.ElementsNamed(e, "attribute"))
                    {
                        s[Xml.GetAttributeString(a, "name")] = Xml.GetAttributeString(a, "value");
                    }

                    lu.addSingle(s);
                }
            }
            catch (Exception)
            {
            }
        }

        private void saveSongs()
        {
            ElementBuilder b = new ElementBuilder().child("media");
            foreach (ShowInfo s in lu.AllInfos)
            {
                ElementBuilder c = b.child("show").attribute("path", s.FilePath);
                foreach (KeyValuePair<string, string> a in s.Attributes)
                {
                    c.child("attribute").attribute("name", a.Key).attribute("value", a.Value);
                }
            }
            FileUtil.MakeSureDirectoryExist(getShowDir());
            b.Document.Save(getShowPath());
        }

        private void moveFilesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MoveTool st = new MoveTool(lu.SelectedInfos);
            st.ShowDialog();
            lu.updateAllText(lu.SelectedItems);
            saveSongs();
        }

        private void removeSelectedToolStripMenuItem_Click(object sender, EventArgs e)
        {
            lu.remove(lu.SelectedItems);
        }
    }
}
