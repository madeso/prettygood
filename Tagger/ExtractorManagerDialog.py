using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Tagger
{
    public partial class ExtractorManagerDialog : Form
    {
        List<Extractor> extractors;
        public ExtractorManagerDialog(List<Extractor> extractors)
        {
            this.extractors = extractors;
            InitializeComponent();
            readData();
        }

        private void dOk_Click(object sender, EventArgs e)
        {
            apply();
            Close();
            DialogResult = DialogResult.OK;
        }

        private void dCancel_Click(object sender, EventArgs e)
        {
            Close();
            DialogResult = DialogResult.Cancel;
        }

        private void dApply_Click(object sender, EventArgs e)
        {
            apply();
        }

        private void addToolStripMenuItem_Click(object sender, EventArgs e)
        {
            addNewObject();
        }

        private void removeSelectedToolStripMenuItem_Click(object sender, EventArgs e)
        {
            removeSelected();
        }
        private void applyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            apply();
        }

        private void dExtractors_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Delete) removeSelected();
        }

        private void revertToolStripMenuItem_Click(object sender, EventArgs e)
        {
            readData();
        }

        private bool Dirty
        {
            set
            {
                dApply.Enabled = value;
                applyToolStripMenuItem.Enabled = value;
            }
        }

        // -----------

        private void removeSelected()
        {
            Dirty = true;
            dExtractors.RemoveObjects(dExtractors.SelectedObjects);
        }

        private void addNewObject()
        {
            dExtractors.AddObject(new Extractor { Pattern = "%artist%-%title%" });
            Dirty = true;
        }

        private void readData()
        {
            Dirty = false;
            List<Extractor> temp = new List<Extractor>();
            foreach (var e in extractors)
            {
                temp.Add(e.deepClone());
            }
            dExtractors.SetObjects(temp);
        }

        private void apply()
        {
            extractors.Clear();
            foreach (Extractor e in dExtractors.Objects)
            {
                extractors.Add(e);
            }
        }
    }
}
