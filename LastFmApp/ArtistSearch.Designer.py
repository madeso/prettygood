namespace LastFmApp
{
    partial class ArtistSearch
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
            this.dArtistName = new System.Windows.Forms.TextBox();
            this.dSearch = new System.Windows.Forms.Button();
            this.dMusicBrainzId = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.dArtists = new BrightIdeasSoftware.ObjectListView();
            this.olvcName = new BrightIdeasSoftware.OLVColumn();
            this.olvcMbid = new BrightIdeasSoftware.OLVColumn();
            this.olvcUrl = new BrightIdeasSoftware.OLVColumn();
            this.olvcGoofy = new BrightIdeasSoftware.OLVColumn();
            this.dLanguage = new System.Windows.Forms.ComboBox();
            ((System.ComponentModel.ISupportInitialize)(this.dArtists)).BeginInit();
            this.SuspendLayout();
            // 
            // dArtistName
            // 
            this.dArtistName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dArtistName.Location = new System.Drawing.Point(93, 12);
            this.dArtistName.Name = "dArtistName";
            this.dArtistName.Size = new System.Drawing.Size(434, 20);
            this.dArtistName.TabIndex = 0;
            // 
            // dSearch
            // 
            this.dSearch.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.dSearch.Location = new System.Drawing.Point(452, 91);
            this.dSearch.Name = "dSearch";
            this.dSearch.Size = new System.Drawing.Size(75, 23);
            this.dSearch.TabIndex = 1;
            this.dSearch.Text = "Search";
            this.dSearch.UseVisualStyleBackColor = true;
            this.dSearch.Click += new System.EventHandler(this.dSearch_Click);
            // 
            // dMusicBrainzId
            // 
            this.dMusicBrainzId.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dMusicBrainzId.Location = new System.Drawing.Point(93, 38);
            this.dMusicBrainzId.Name = "dMusicBrainzId";
            this.dMusicBrainzId.Size = new System.Drawing.Size(434, 20);
            this.dMusicBrainzId.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Name";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(77, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Music-brainz id";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 67);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(55, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "Language";
            // 
            // dArtists
            // 
            this.dArtists.AllColumns.Add(this.olvcName);
            this.dArtists.AllColumns.Add(this.olvcMbid);
            this.dArtists.AllColumns.Add(this.olvcUrl);
            this.dArtists.AllColumns.Add(this.olvcGoofy);
            this.dArtists.AllowColumnReorder = true;
            this.dArtists.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dArtists.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.olvcName,
            this.olvcMbid,
            this.olvcUrl,
            this.olvcGoofy});
            this.dArtists.FullRowSelect = true;
            this.dArtists.HideSelection = false;
            this.dArtists.Location = new System.Drawing.Point(12, 119);
            this.dArtists.Name = "dArtists";
            this.dArtists.Size = new System.Drawing.Size(515, 135);
            this.dArtists.TabIndex = 7;
            this.dArtists.TintSortColumn = true;
            this.dArtists.UseAlternatingBackColors = true;
            this.dArtists.UseCompatibleStateImageBehavior = false;
            this.dArtists.View = System.Windows.Forms.View.Details;
            this.dArtists.DoubleClick += new System.EventHandler(this.dArtists_DoubleClick);
            // 
            // olvcName
            // 
            this.olvcName.AspectName = "name";
            this.olvcName.Text = "Name";
            this.olvcName.UseInitialLetterForGroup = true;
            this.olvcName.Width = 78;
            // 
            // olvcMbid
            // 
            this.olvcMbid.AspectName = "mbid";
            this.olvcMbid.Text = "Music-brainz";
            this.olvcMbid.UseInitialLetterForGroup = true;
            this.olvcMbid.Width = 73;
            // 
            // olvcUrl
            // 
            this.olvcUrl.AspectName = "url";
            this.olvcUrl.Text = "URL";
            this.olvcUrl.Width = 115;
            // 
            // olvcGoofy
            // 
            this.olvcGoofy.AspectName = "seemsGoofy";
            this.olvcGoofy.Text = "Goofy";
            this.olvcGoofy.UseInitialLetterForGroup = true;
            // 
            // dLanguage
            // 
            this.dLanguage.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.dLanguage.FormattingEnabled = true;
            this.dLanguage.Location = new System.Drawing.Point(93, 64);
            this.dLanguage.Name = "dLanguage";
            this.dLanguage.Size = new System.Drawing.Size(434, 21);
            this.dLanguage.TabIndex = 8;
            // 
            // ArtistSearch
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(539, 266);
            this.Controls.Add(this.dLanguage);
            this.Controls.Add(this.dArtists);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dMusicBrainzId);
            this.Controls.Add(this.dSearch);
            this.Controls.Add(this.dArtistName);
            this.Name = "ArtistSearch";
            this.Text = "ArtistSearch";
            ((System.ComponentModel.ISupportInitialize)(this.dArtists)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox dArtistName;
        private System.Windows.Forms.Button dSearch;
        private System.Windows.Forms.TextBox dMusicBrainzId;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private BrightIdeasSoftware.ObjectListView dArtists;
        private BrightIdeasSoftware.OLVColumn olvcName;
        private BrightIdeasSoftware.OLVColumn olvcMbid;
        private BrightIdeasSoftware.OLVColumn olvcUrl;
        private BrightIdeasSoftware.OLVColumn olvcGoofy;
        private System.Windows.Forms.ComboBox dLanguage;
    }
}