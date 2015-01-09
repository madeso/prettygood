namespace Tagger
{
    partial class AutoTagger
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
            this.dTags = new BrightIdeasSoftware.FastObjectListView();
            this.dFileName = new System.Windows.Forms.TextBox();
            this.olvcArtist = new BrightIdeasSoftware.OLVColumn();
            this.olvcTitle = new BrightIdeasSoftware.OLVColumn();
            this.olvcAlbum = new BrightIdeasSoftware.OLVColumn();
            this.olvcTrackNumber = new BrightIdeasSoftware.OLVColumn();
            this.olvcGenre = new BrightIdeasSoftware.OLVColumn();
            this.olvcYear = new BrightIdeasSoftware.OLVColumn();
            this.olvcComments = new BrightIdeasSoftware.OLVColumn();
            this.olvcIsCover = new BrightIdeasSoftware.OLVColumn();
            this.olvcIsRemix = new BrightIdeasSoftware.OLVColumn();
            this.olvcTotalTracks = new BrightIdeasSoftware.OLVColumn();
            this.olvcScore = new BrightIdeasSoftware.OLVColumn();
            this.olvcPattern = new BrightIdeasSoftware.OLVColumn();
            this.dIncludeInvalid = new System.Windows.Forms.CheckBox();
            this.olvcMessage = new BrightIdeasSoftware.OLVColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dTags)).BeginInit();
            this.SuspendLayout();
            // 
            // dTags
            // 
            this.dTags.AllColumns.Add(this.olvcTrackNumber);
            this.dTags.AllColumns.Add(this.olvcArtist);
            this.dTags.AllColumns.Add(this.olvcTitle);
            this.dTags.AllColumns.Add(this.olvcAlbum);
            this.dTags.AllColumns.Add(this.olvcTotalTracks);
            this.dTags.AllColumns.Add(this.olvcPattern);
            this.dTags.AllColumns.Add(this.olvcScore);
            this.dTags.AllColumns.Add(this.olvcGenre);
            this.dTags.AllColumns.Add(this.olvcYear);
            this.dTags.AllColumns.Add(this.olvcMessage);
            this.dTags.AllColumns.Add(this.olvcComments);
            this.dTags.AllColumns.Add(this.olvcIsCover);
            this.dTags.AllColumns.Add(this.olvcIsRemix);
            this.dTags.AllowColumnReorder = true;
            this.dTags.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dTags.CellEditActivation = BrightIdeasSoftware.ObjectListView.CellEditActivateMode.F2Only;
            this.dTags.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.olvcTrackNumber,
            this.olvcArtist,
            this.olvcTitle,
            this.olvcAlbum,
            this.olvcTotalTracks,
            this.olvcPattern,
            this.olvcScore,
            this.olvcGenre,
            this.olvcYear,
            this.olvcMessage,
            this.olvcComments,
            this.olvcIsCover,
            this.olvcIsRemix});
            this.dTags.FullRowSelect = true;
            this.dTags.Location = new System.Drawing.Point(12, 38);
            this.dTags.Name = "dTags";
            this.dTags.ShowGroups = false;
            this.dTags.Size = new System.Drawing.Size(859, 242);
            this.dTags.TabIndex = 0;
            this.dTags.UseAlternatingBackColors = true;
            this.dTags.UseCompatibleStateImageBehavior = false;
            this.dTags.View = System.Windows.Forms.View.Details;
            this.dTags.VirtualMode = true;
            this.dTags.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.dTags_MouseDoubleClick);
            // 
            // dFileName
            // 
            this.dFileName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dFileName.Location = new System.Drawing.Point(103, 12);
            this.dFileName.Name = "dFileName";
            this.dFileName.ReadOnly = true;
            this.dFileName.Size = new System.Drawing.Size(768, 20);
            this.dFileName.TabIndex = 1;
            // 
            // olvcArtist
            // 
            this.olvcArtist.AspectName = "tag.Artist";
            this.olvcArtist.Text = "Artist";
            // 
            // olvcTitle
            // 
            this.olvcTitle.AspectName = "tag.Title";
            this.olvcTitle.Text = "Title";
            // 
            // olvcAlbum
            // 
            this.olvcAlbum.AspectName = "tag.Album";
            this.olvcAlbum.Text = "Album";
            // 
            // olvcTrackNumber
            // 
            this.olvcTrackNumber.AspectName = "tag.TrackNumber";
            this.olvcTrackNumber.Text = "#";
            // 
            // olvcGenre
            // 
            this.olvcGenre.AspectName = "tag.Genre";
            this.olvcGenre.Text = "Genre";
            // 
            // olvcYear
            // 
            this.olvcYear.AspectName = "tag.Year";
            this.olvcYear.Text = "Year";
            // 
            // olvcComments
            // 
            this.olvcComments.AspectName = "tag.Comments";
            this.olvcComments.Text = "Comments";
            this.olvcComments.Width = 127;
            // 
            // olvcIsCover
            // 
            this.olvcIsCover.AspectName = "tag.IsCover";
            this.olvcIsCover.Text = "cover?";
            // 
            // olvcIsRemix
            // 
            this.olvcIsRemix.AspectName = "tag.IsRemix";
            this.olvcIsRemix.Text = "remix?";
            // 
            // olvcTotalTracks
            // 
            this.olvcTotalTracks.AspectName = "tag.TotalTracks";
            this.olvcTotalTracks.Text = "Total tracks";
            this.olvcTotalTracks.Width = 88;
            // 
            // olvcScore
            // 
            this.olvcScore.AspectName = "Score";
            this.olvcScore.IsEditable = false;
            this.olvcScore.Text = "Score";
            this.olvcScore.Width = 48;
            // 
            // olvcPattern
            // 
            this.olvcPattern.AspectName = "extractor.logic";
            this.olvcPattern.IsEditable = false;
            this.olvcPattern.Text = "Pattern";
            // 
            // dIncludeInvalid
            // 
            this.dIncludeInvalid.AutoSize = true;
            this.dIncludeInvalid.Location = new System.Drawing.Point(12, 14);
            this.dIncludeInvalid.Name = "dIncludeInvalid";
            this.dIncludeInvalid.Size = new System.Drawing.Size(85, 17);
            this.dIncludeInvalid.TabIndex = 2;
            this.dIncludeInvalid.Text = "Also invalid?";
            this.dIncludeInvalid.UseVisualStyleBackColor = true;
            this.dIncludeInvalid.CheckedChanged += new System.EventHandler(this.dIncludeInvalid_CheckedChanged);
            // 
            // olvcMessage
            // 
            this.olvcMessage.AspectName = "Message";
            this.olvcMessage.Text = "Message";
            this.olvcMessage.Width = 99;
            // 
            // AutoTagger
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(883, 292);
            this.Controls.Add(this.dIncludeInvalid);
            this.Controls.Add(this.dFileName);
            this.Controls.Add(this.dTags);
            this.Name = "AutoTagger";
            this.Text = "AutoTagger";
            ((System.ComponentModel.ISupportInitialize)(this.dTags)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private BrightIdeasSoftware.FastObjectListView dTags;
        private System.Windows.Forms.TextBox dFileName;
        private BrightIdeasSoftware.OLVColumn olvcArtist;
        private BrightIdeasSoftware.OLVColumn olvcTitle;
        private BrightIdeasSoftware.OLVColumn olvcAlbum;
        private BrightIdeasSoftware.OLVColumn olvcTrackNumber;
        private BrightIdeasSoftware.OLVColumn olvcGenre;
        private BrightIdeasSoftware.OLVColumn olvcYear;
        private BrightIdeasSoftware.OLVColumn olvcComments;
        private BrightIdeasSoftware.OLVColumn olvcIsCover;
        private BrightIdeasSoftware.OLVColumn olvcIsRemix;
        private BrightIdeasSoftware.OLVColumn olvcTotalTracks;
        private BrightIdeasSoftware.OLVColumn olvcScore;
        private BrightIdeasSoftware.OLVColumn olvcPattern;
        private System.Windows.Forms.CheckBox dIncludeInvalid;
        private BrightIdeasSoftware.OLVColumn olvcMessage;
    }
}