namespace LastFmApp
{
    partial class AlbumSearch
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
            this.dAlbum = new System.Windows.Forms.TextBox();
            this.dSearch = new System.Windows.Forms.Button();
            this.dResult = new BrightIdeasSoftware.ObjectListView();
            this.olvcName = new BrightIdeasSoftware.OLVColumn();
            this.olvcArtist = new BrightIdeasSoftware.OLVColumn();
            this.olvcId = new BrightIdeasSoftware.OLVColumn();
            this.olvcUrl = new BrightIdeasSoftware.OLVColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dResult)).BeginInit();
            this.SuspendLayout();
            // 
            // dAlbum
            // 
            this.dAlbum.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dAlbum.Location = new System.Drawing.Point(12, 14);
            this.dAlbum.Name = "dAlbum";
            this.dAlbum.Size = new System.Drawing.Size(189, 20);
            this.dAlbum.TabIndex = 0;
            // 
            // dSearch
            // 
            this.dSearch.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.dSearch.Location = new System.Drawing.Point(207, 12);
            this.dSearch.Name = "dSearch";
            this.dSearch.Size = new System.Drawing.Size(73, 23);
            this.dSearch.TabIndex = 1;
            this.dSearch.Text = "Search";
            this.dSearch.UseVisualStyleBackColor = true;
            this.dSearch.Click += new System.EventHandler(this.dSearch_Click);
            // 
            // dResult
            // 
            this.dResult.AllColumns.Add(this.olvcName);
            this.dResult.AllColumns.Add(this.olvcArtist);
            this.dResult.AllColumns.Add(this.olvcId);
            this.dResult.AllColumns.Add(this.olvcUrl);
            this.dResult.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dResult.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.olvcName,
            this.olvcArtist,
            this.olvcId,
            this.olvcUrl});
            this.dResult.Location = new System.Drawing.Point(12, 50);
            this.dResult.Name = "dResult";
            this.dResult.Size = new System.Drawing.Size(268, 204);
            this.dResult.TabIndex = 2;
            this.dResult.UseCompatibleStateImageBehavior = false;
            this.dResult.View = System.Windows.Forms.View.Details;
            // 
            // olvcName
            // 
            this.olvcName.AspectName = "name";
            this.olvcName.Text = "Name";
            this.olvcName.UseInitialLetterForGroup = true;
            // 
            // olvcArtist
            // 
            this.olvcArtist.AspectName = "artist";
            this.olvcArtist.Text = "Artist";
            this.olvcArtist.UseInitialLetterForGroup = true;
            // 
            // olvcId
            // 
            this.olvcId.AspectName = "id";
            this.olvcId.Text = "ID";
            this.olvcId.UseInitialLetterForGroup = true;
            // 
            // olvcUrl
            // 
            this.olvcUrl.AspectName = "url";
            this.olvcUrl.Text = "URL";
            this.olvcUrl.UseInitialLetterForGroup = true;
            // 
            // AlbumSearch
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 266);
            this.Controls.Add(this.dResult);
            this.Controls.Add(this.dSearch);
            this.Controls.Add(this.dAlbum);
            this.Name = "AlbumSearch";
            this.Text = "AlbumSearch";
            ((System.ComponentModel.ISupportInitialize)(this.dResult)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox dAlbum;
        private System.Windows.Forms.Button dSearch;
        private BrightIdeasSoftware.ObjectListView dResult;
        private BrightIdeasSoftware.OLVColumn olvcName;
        private BrightIdeasSoftware.OLVColumn olvcArtist;
        private BrightIdeasSoftware.OLVColumn olvcId;
        private BrightIdeasSoftware.OLVColumn olvcUrl;
    }
}