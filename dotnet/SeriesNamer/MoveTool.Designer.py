namespace SeriesNamer
{
    partial class MoveTool
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
            this.dResultPreview = new System.Windows.Forms.ListView();
            this.columnHeaderSource = new System.Windows.Forms.ColumnHeader();
            this.columnHeaderTarget = new System.Windows.Forms.ColumnHeader();
            this.dTargetPattern = new System.Windows.Forms.TextBox();
            this.dTargetFolder = new System.Windows.Forms.TextBox();
            this.dStartRename = new System.Windows.Forms.Button();
            this.dBroswseFolder = new System.Windows.Forms.Button();
            this.dFolderBrowse = new System.Windows.Forms.FolderBrowserDialog();
            this.SuspendLayout();
            // 
            // dResultPreview
            // 
            this.dResultPreview.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dResultPreview.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeaderSource,
            this.columnHeaderTarget});
            this.dResultPreview.GridLines = true;
            this.dResultPreview.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable;
            this.dResultPreview.LabelWrap = false;
            this.dResultPreview.Location = new System.Drawing.Point(12, 70);
            this.dResultPreview.Name = "dResultPreview";
            this.dResultPreview.Size = new System.Drawing.Size(352, 183);
            this.dResultPreview.TabIndex = 9;
            this.dResultPreview.UseCompatibleStateImageBehavior = false;
            this.dResultPreview.View = System.Windows.Forms.View.Details;
            // 
            // columnHeaderSource
            // 
            this.columnHeaderSource.Text = "Source";
            this.columnHeaderSource.Width = 151;
            // 
            // columnHeaderTarget
            // 
            this.columnHeaderTarget.Text = "Target";
            this.columnHeaderTarget.Width = 173;
            // 
            // dTargetPattern
            // 
            this.dTargetPattern.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dTargetPattern.Location = new System.Drawing.Point(12, 43);
            this.dTargetPattern.Name = "dTargetPattern";
            this.dTargetPattern.Size = new System.Drawing.Size(310, 20);
            this.dTargetPattern.TabIndex = 8;
            this.dTargetPattern.Text = "%series%\\s%season%\\%episode% - %title%";
            this.dTargetPattern.TextChanged += new System.EventHandler(this.dTargetPattern_TextChanged);
            // 
            // dTargetFolder
            // 
            this.dTargetFolder.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dTargetFolder.Location = new System.Drawing.Point(12, 14);
            this.dTargetFolder.Name = "dTargetFolder";
            this.dTargetFolder.ReadOnly = true;
            this.dTargetFolder.Size = new System.Drawing.Size(310, 20);
            this.dTargetFolder.TabIndex = 7;
            // 
            // dStartRename
            // 
            this.dStartRename.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.dStartRename.Location = new System.Drawing.Point(328, 41);
            this.dStartRename.Name = "dStartRename";
            this.dStartRename.Size = new System.Drawing.Size(36, 23);
            this.dStartRename.TabIndex = 6;
            this.dStartRename.Text = "Go";
            this.dStartRename.UseVisualStyleBackColor = true;
            this.dStartRename.Click += new System.EventHandler(this.dStartRename_Click);
            // 
            // dBroswseFolder
            // 
            this.dBroswseFolder.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.dBroswseFolder.Location = new System.Drawing.Point(328, 12);
            this.dBroswseFolder.Name = "dBroswseFolder";
            this.dBroswseFolder.Size = new System.Drawing.Size(36, 23);
            this.dBroswseFolder.TabIndex = 5;
            this.dBroswseFolder.Text = "...";
            this.dBroswseFolder.UseVisualStyleBackColor = true;
            this.dBroswseFolder.Click += new System.EventHandler(this.dBroswseFolder_Click);
            // 
            // MoveTool
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(376, 265);
            this.Controls.Add(this.dResultPreview);
            this.Controls.Add(this.dTargetPattern);
            this.Controls.Add(this.dTargetFolder);
            this.Controls.Add(this.dStartRename);
            this.Controls.Add(this.dBroswseFolder);
            this.Name = "MoveTool";
            this.Text = "MoveTool";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListView dResultPreview;
        private System.Windows.Forms.ColumnHeader columnHeaderSource;
        private System.Windows.Forms.ColumnHeader columnHeaderTarget;
        private System.Windows.Forms.TextBox dTargetPattern;
        private System.Windows.Forms.TextBox dTargetFolder;
        private System.Windows.Forms.Button dStartRename;
        private System.Windows.Forms.Button dBroswseFolder;
        private System.Windows.Forms.FolderBrowserDialog dFolderBrowse;
    }
}