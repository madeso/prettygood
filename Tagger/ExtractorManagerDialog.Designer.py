namespace Tagger
{
    partial class ExtractorManagerDialog
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.dExtractors = new BrightIdeasSoftware.FastObjectListView();
            this.dApply = new System.Windows.Forms.Button();
            this.dCancel = new System.Windows.Forms.Button();
            this.dOk = new System.Windows.Forms.Button();
            this.dContext = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.addToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.removeSelectedToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.revertToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.applyToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.olvcPattern = new BrightIdeasSoftware.OLVColumn();
            this.olvcScore = new BrightIdeasSoftware.OLVColumn();
            this.olvcRemoveUnderscore = new BrightIdeasSoftware.OLVColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dExtractors)).BeginInit();
            this.dContext.SuspendLayout();
            this.SuspendLayout();
            // 
            // dExtractors
            // 
            this.dExtractors.AllColumns.Add(this.olvcPattern);
            this.dExtractors.AllColumns.Add(this.olvcScore);
            this.dExtractors.AllColumns.Add(this.olvcRemoveUnderscore);
            this.dExtractors.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dExtractors.CellEditActivation = BrightIdeasSoftware.ObjectListView.CellEditActivateMode.DoubleClick;
            this.dExtractors.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.olvcPattern,
            this.olvcScore,
            this.olvcRemoveUnderscore});
            this.dExtractors.ContextMenuStrip = this.dContext;
            this.dExtractors.FullRowSelect = true;
            this.dExtractors.Location = new System.Drawing.Point(12, 12);
            this.dExtractors.Name = "dExtractors";
            this.dExtractors.ShowGroups = false;
            this.dExtractors.Size = new System.Drawing.Size(608, 302);
            this.dExtractors.TabIndex = 0;
            this.dExtractors.UseAlternatingBackColors = true;
            this.dExtractors.UseCompatibleStateImageBehavior = false;
            this.dExtractors.View = System.Windows.Forms.View.Details;
            this.dExtractors.VirtualMode = true;
            this.dExtractors.KeyUp += new System.Windows.Forms.KeyEventHandler(this.dExtractors_KeyUp);
            // 
            // dApply
            // 
            this.dApply.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.dApply.Location = new System.Drawing.Point(545, 320);
            this.dApply.Name = "dApply";
            this.dApply.Size = new System.Drawing.Size(75, 23);
            this.dApply.TabIndex = 2;
            this.dApply.Text = "Apply";
            this.dApply.UseVisualStyleBackColor = true;
            this.dApply.Click += new System.EventHandler(this.dApply_Click);
            // 
            // dCancel
            // 
            this.dCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.dCancel.Location = new System.Drawing.Point(464, 320);
            this.dCancel.Name = "dCancel";
            this.dCancel.Size = new System.Drawing.Size(75, 23);
            this.dCancel.TabIndex = 3;
            this.dCancel.Text = "Cancel";
            this.dCancel.UseVisualStyleBackColor = true;
            this.dCancel.Click += new System.EventHandler(this.dCancel_Click);
            // 
            // dOk
            // 
            this.dOk.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.dOk.Location = new System.Drawing.Point(383, 320);
            this.dOk.Name = "dOk";
            this.dOk.Size = new System.Drawing.Size(75, 23);
            this.dOk.TabIndex = 4;
            this.dOk.Text = "OK";
            this.dOk.UseVisualStyleBackColor = true;
            this.dOk.Click += new System.EventHandler(this.dOk_Click);
            // 
            // dContext
            // 
            this.dContext.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.addToolStripMenuItem,
            this.removeSelectedToolStripMenuItem,
            this.revertToolStripMenuItem,
            this.applyToolStripMenuItem});
            this.dContext.Name = "dContext";
            this.dContext.Size = new System.Drawing.Size(168, 92);
            // 
            // addToolStripMenuItem
            // 
            this.addToolStripMenuItem.Name = "addToolStripMenuItem";
            this.addToolStripMenuItem.Size = new System.Drawing.Size(167, 22);
            this.addToolStripMenuItem.Text = "Add";
            this.addToolStripMenuItem.Click += new System.EventHandler(this.addToolStripMenuItem_Click);
            // 
            // removeSelectedToolStripMenuItem
            // 
            this.removeSelectedToolStripMenuItem.Name = "removeSelectedToolStripMenuItem";
            this.removeSelectedToolStripMenuItem.Size = new System.Drawing.Size(167, 22);
            this.removeSelectedToolStripMenuItem.Text = "Remove selected";
            this.removeSelectedToolStripMenuItem.Click += new System.EventHandler(this.removeSelectedToolStripMenuItem_Click);
            // 
            // revertToolStripMenuItem
            // 
            this.revertToolStripMenuItem.Name = "revertToolStripMenuItem";
            this.revertToolStripMenuItem.Size = new System.Drawing.Size(167, 22);
            this.revertToolStripMenuItem.Text = "Revert";
            this.revertToolStripMenuItem.Click += new System.EventHandler(this.revertToolStripMenuItem_Click);
            // 
            // applyToolStripMenuItem
            // 
            this.applyToolStripMenuItem.Name = "applyToolStripMenuItem";
            this.applyToolStripMenuItem.Size = new System.Drawing.Size(167, 22);
            this.applyToolStripMenuItem.Text = "Apply";
            this.applyToolStripMenuItem.Click += new System.EventHandler(this.applyToolStripMenuItem_Click);
            // 
            // olvcPattern
            // 
            this.olvcPattern.AspectName = "Pattern";
            this.olvcPattern.Text = "Pattern";
            // 
            // olvcScore
            // 
            this.olvcScore.AspectName = "baseScore";
            this.olvcScore.Text = "Base score";
            // 
            // olvcRemoveUnderscore
            // 
            this.olvcRemoveUnderscore.AspectName = "removeUnderscores";
            this.olvcRemoveUnderscore.Text = "Remove underscore?";
            this.olvcRemoveUnderscore.Width = 130;
            // 
            // ExtractorManagerDialog
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(635, 355);
            this.Controls.Add(this.dApply);
            this.Controls.Add(this.dExtractors);
            this.Controls.Add(this.dOk);
            this.Controls.Add(this.dCancel);
            this.Name = "ExtractorManagerDialog";
            this.Text = "ExtractorGui";
            ((System.ComponentModel.ISupportInitialize)(this.dExtractors)).EndInit();
            this.dContext.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private BrightIdeasSoftware.FastObjectListView dExtractors;
        private System.Windows.Forms.Button dApply;
        private System.Windows.Forms.Button dCancel;
        private System.Windows.Forms.Button dOk;
        private System.Windows.Forms.ContextMenuStrip dContext;
        private System.Windows.Forms.ToolStripMenuItem addToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem removeSelectedToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem revertToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem applyToolStripMenuItem;
        private BrightIdeasSoftware.OLVColumn olvcPattern;
        private BrightIdeasSoftware.OLVColumn olvcScore;
        private BrightIdeasSoftware.OLVColumn olvcRemoveUnderscore;
    }
}