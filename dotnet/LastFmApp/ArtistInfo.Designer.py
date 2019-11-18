namespace LastFmApp
{
    partial class ArtistInfo
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
            this.dName = new System.Windows.Forms.TextBox();
            this.dMbid = new System.Windows.Forms.TextBox();
            this.dUrl = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.dTags = new System.Windows.Forms.TextBox();
            this.dSimilar = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.dBio = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // dName
            // 
            this.dName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dName.Location = new System.Drawing.Point(84, 12);
            this.dName.Name = "dName";
            this.dName.Size = new System.Drawing.Size(210, 20);
            this.dName.TabIndex = 0;
            // 
            // dMbid
            // 
            this.dMbid.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dMbid.Location = new System.Drawing.Point(84, 38);
            this.dMbid.Name = "dMbid";
            this.dMbid.Size = new System.Drawing.Size(210, 20);
            this.dMbid.TabIndex = 1;
            // 
            // dUrl
            // 
            this.dUrl.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dUrl.Location = new System.Drawing.Point(84, 64);
            this.dUrl.Name = "dUrl";
            this.dUrl.ReadOnly = true;
            this.dUrl.Size = new System.Drawing.Size(210, 20);
            this.dUrl.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "Name";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(66, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "Music-brainz";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 67);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(18, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "url";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 93);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(31, 13);
            this.label4.TabIndex = 6;
            this.label4.Text = "Tags";
            // 
            // dTags
            // 
            this.dTags.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dTags.Location = new System.Drawing.Point(84, 90);
            this.dTags.Name = "dTags";
            this.dTags.ReadOnly = true;
            this.dTags.Size = new System.Drawing.Size(210, 20);
            this.dTags.TabIndex = 7;
            // 
            // dSimilar
            // 
            this.dSimilar.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dSimilar.Location = new System.Drawing.Point(84, 116);
            this.dSimilar.Name = "dSimilar";
            this.dSimilar.ReadOnly = true;
            this.dSimilar.Size = new System.Drawing.Size(210, 20);
            this.dSimilar.TabIndex = 8;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 119);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(37, 13);
            this.label5.TabIndex = 9;
            this.label5.Text = "Similar";
            // 
            // dBio
            // 
            this.dBio.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dBio.Location = new System.Drawing.Point(15, 142);
            this.dBio.Multiline = true;
            this.dBio.Name = "dBio";
            this.dBio.ReadOnly = true;
            this.dBio.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.dBio.Size = new System.Drawing.Size(279, 137);
            this.dBio.TabIndex = 10;
            // 
            // ArtistInfo
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(306, 291);
            this.Controls.Add(this.dBio);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.dSimilar);
            this.Controls.Add(this.dTags);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dUrl);
            this.Controls.Add(this.dMbid);
            this.Controls.Add(this.dName);
            this.Name = "ArtistInfo";
            this.Text = "ArtistInfo";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox dName;
        private System.Windows.Forms.TextBox dMbid;
        private System.Windows.Forms.TextBox dUrl;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox dTags;
        private System.Windows.Forms.TextBox dSimilar;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox dBio;
    }
}