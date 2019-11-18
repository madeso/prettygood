namespace Tagger
{
    partial class MainWindow
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
            this.dSongs = new BrightIdeasSoftware.FastObjectListView();
            this.olvArtist = new BrightIdeasSoftware.OLVColumn();
            this.olvTitle = new BrightIdeasSoftware.OLVColumn();
            this.olvAlbum = new BrightIdeasSoftware.OLVColumn();
            this.olvTracknumber = new BrightIdeasSoftware.OLVColumn();
            this.olvGenre = new BrightIdeasSoftware.OLVColumn();
            this.olvFilePath = new BrightIdeasSoftware.OLVColumn();
            this.olvYear = new BrightIdeasSoftware.OLVColumn();
            this.olvComments = new BrightIdeasSoftware.OLVColumn();
            this.olvIsCover = new BrightIdeasSoftware.OLVColumn();
            this.olvIsRemix = new BrightIdeasSoftware.OLVColumn();
            this.olvTotalTracks = new BrightIdeasSoftware.OLVColumn();
            this.dContext = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.lookupToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.manageExtractorsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            ((System.ComponentModel.ISupportInitialize)(this.dSongs)).BeginInit();
            this.dContext.SuspendLayout();
            this.SuspendLayout();
            // 
            // dSongs
            // 
            this.dSongs.AllColumns.Add(this.olvArtist);
            this.dSongs.AllColumns.Add(this.olvTitle);
            this.dSongs.AllColumns.Add(this.olvAlbum);
            this.dSongs.AllColumns.Add(this.olvTracknumber);
            this.dSongs.AllColumns.Add(this.olvGenre);
            this.dSongs.AllColumns.Add(this.olvFilePath);
            this.dSongs.AllColumns.Add(this.olvYear);
            this.dSongs.AllColumns.Add(this.olvComments);
            this.dSongs.AllColumns.Add(this.olvIsCover);
            this.dSongs.AllColumns.Add(this.olvIsRemix);
            this.dSongs.AllColumns.Add(this.olvTotalTracks);
            this.dSongs.AllowColumnReorder = true;
            this.dSongs.AllowDrop = true;
            this.dSongs.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dSongs.CellEditActivation = BrightIdeasSoftware.ObjectListView.CellEditActivateMode.DoubleClick;
            this.dSongs.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.olvArtist,
            this.olvTitle,
            this.olvAlbum,
            this.olvTracknumber,
            this.olvGenre,
            this.olvFilePath,
            this.olvYear,
            this.olvComments,
            this.olvIsCover,
            this.olvIsRemix,
            this.olvTotalTracks});
            this.dSongs.ContextMenuStrip = this.dContext;
            this.dSongs.FullRowSelect = true;
            this.dSongs.LabelEdit = true;
            this.dSongs.Location = new System.Drawing.Point(12, 12);
            this.dSongs.Name = "dSongs";
            this.dSongs.ShowGroups = false;
            this.dSongs.Size = new System.Drawing.Size(1244, 348);
            this.dSongs.TabIndex = 0;
            this.dSongs.TintSortColumn = true;
            this.dSongs.UseAlternatingBackColors = true;
            this.dSongs.UseCompatibleStateImageBehavior = false;
            this.dSongs.View = System.Windows.Forms.View.Details;
            this.dSongs.VirtualMode = true;
            this.dSongs.KeyUp += new System.Windows.Forms.KeyEventHandler(this.dSongs_KeyUp);
            // 
            // olvArtist
            // 
            this.olvArtist.AspectName = "Artist";
            this.olvArtist.DisplayIndex = 1;
            this.olvArtist.Text = "Artist";
            this.olvArtist.Width = 131;
            // 
            // olvTitle
            // 
            this.olvTitle.AspectName = "Title";
            this.olvTitle.DisplayIndex = 2;
            this.olvTitle.Text = "Title";
            this.olvTitle.Width = 175;
            // 
            // olvAlbum
            // 
            this.olvAlbum.AspectName = "Album";
            this.olvAlbum.DisplayIndex = 3;
            this.olvAlbum.Text = "Album";
            this.olvAlbum.Width = 174;
            // 
            // olvTracknumber
            // 
            this.olvTracknumber.AspectName = "TrackNumber";
            this.olvTracknumber.DisplayIndex = 0;
            this.olvTracknumber.Text = "#";
            this.olvTracknumber.Width = 28;
            // 
            // olvGenre
            // 
            this.olvGenre.AspectName = "Genre";
            this.olvGenre.Text = "Genre";
            this.olvGenre.Width = 95;
            // 
            // olvFilePath
            // 
            this.olvFilePath.AspectName = "FilePath";
            this.olvFilePath.Text = "File path";
            this.olvFilePath.Width = 77;
            // 
            // olvYear
            // 
            this.olvYear.AspectName = "Year";
            this.olvYear.Text = "Year";
            // 
            // olvComments
            // 
            this.olvComments.AspectName = "Comments";
            this.olvComments.Text = "Comments";
            this.olvComments.Width = 74;
            // 
            // olvIsCover
            // 
            this.olvIsCover.AspectName = "IsCover";
            this.olvIsCover.Text = "Cover?";
            // 
            // olvIsRemix
            // 
            this.olvIsRemix.AspectName = "IsRemix";
            this.olvIsRemix.Text = "Remix?";
            // 
            // olvTotalTracks
            // 
            this.olvTotalTracks.AspectName = "TotalTracks";
            this.olvTotalTracks.Text = "Total tracks";
            this.olvTotalTracks.Width = 73;
            // 
            // dContext
            // 
            this.dContext.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.lookupToolStripMenuItem,
            this.manageExtractorsToolStripMenuItem});
            this.dContext.Name = "dContext";
            this.dContext.Size = new System.Drawing.Size(189, 48);
            // 
            // lookupToolStripMenuItem
            // 
            this.lookupToolStripMenuItem.Name = "lookupToolStripMenuItem";
            this.lookupToolStripMenuItem.Size = new System.Drawing.Size(188, 22);
            this.lookupToolStripMenuItem.Text = "Lookup";
            this.lookupToolStripMenuItem.Click += new System.EventHandler(this.lookupToolStripMenuItem_Click);
            // 
            // manageExtractorsToolStripMenuItem
            // 
            this.manageExtractorsToolStripMenuItem.Name = "manageExtractorsToolStripMenuItem";
            this.manageExtractorsToolStripMenuItem.Size = new System.Drawing.Size(188, 22);
            this.manageExtractorsToolStripMenuItem.Text = "Manage extractors...";
            this.manageExtractorsToolStripMenuItem.Click += new System.EventHandler(this.manageExtractorsToolStripMenuItem_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1268, 372);
            this.Controls.Add(this.dSongs);
            this.Name = "MainWindow";
            this.Text = "Tagger";
            ((System.ComponentModel.ISupportInitialize)(this.dSongs)).EndInit();
            this.dContext.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private BrightIdeasSoftware.FastObjectListView dSongs;
        private BrightIdeasSoftware.OLVColumn olvArtist;
        private BrightIdeasSoftware.OLVColumn olvTitle;
        private BrightIdeasSoftware.OLVColumn olvAlbum;
        private BrightIdeasSoftware.OLVColumn olvTracknumber;
        private BrightIdeasSoftware.OLVColumn olvGenre;
        private BrightIdeasSoftware.OLVColumn olvFilePath;
        private BrightIdeasSoftware.OLVColumn olvYear;
        private BrightIdeasSoftware.OLVColumn olvComments;
        private BrightIdeasSoftware.OLVColumn olvIsCover;
        private BrightIdeasSoftware.OLVColumn olvIsRemix;
        private BrightIdeasSoftware.OLVColumn olvTotalTracks;
        private System.Windows.Forms.ContextMenuStrip dContext;
        private System.Windows.Forms.ToolStripMenuItem lookupToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem manageExtractorsToolStripMenuItem;

    }
}

