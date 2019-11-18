namespace LastFmApp
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
            this.dApiKey = new System.Windows.Forms.TextBox();
            this.dUser = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.dPassword = new System.Windows.Forms.MaskedTextBox();
            this.dSearchArtist = new System.Windows.Forms.Button();
            this.dSearchAlbum = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // dApiKey
            // 
            this.dApiKey.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dApiKey.Location = new System.Drawing.Point(71, 12);
            this.dApiKey.Name = "dApiKey";
            this.dApiKey.Size = new System.Drawing.Size(209, 20);
            this.dApiKey.TabIndex = 0;
            this.dApiKey.Text = "b25b959554ed76058ac220b7b2e0a026";
            // 
            // dUser
            // 
            this.dUser.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dUser.Location = new System.Drawing.Point(71, 38);
            this.dUser.Name = "dUser";
            this.dUser.Size = new System.Drawing.Size(209, 20);
            this.dUser.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(44, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "API-key";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "User";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 67);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(53, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Password";
            // 
            // dPassword
            // 
            this.dPassword.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dPassword.Location = new System.Drawing.Point(71, 64);
            this.dPassword.Name = "dPassword";
            this.dPassword.Size = new System.Drawing.Size(209, 20);
            this.dPassword.TabIndex = 6;
            // 
            // dSearchArtist
            // 
            this.dSearchArtist.Location = new System.Drawing.Point(15, 90);
            this.dSearchArtist.Name = "dSearchArtist";
            this.dSearchArtist.Size = new System.Drawing.Size(75, 23);
            this.dSearchArtist.TabIndex = 7;
            this.dSearchArtist.Text = "Artist";
            this.dSearchArtist.UseVisualStyleBackColor = true;
            this.dSearchArtist.Click += new System.EventHandler(this.dSearchArtist_Click);
            // 
            // dSearchAlbum
            // 
            this.dSearchAlbum.Location = new System.Drawing.Point(96, 90);
            this.dSearchAlbum.Name = "dSearchAlbum";
            this.dSearchAlbum.Size = new System.Drawing.Size(75, 23);
            this.dSearchAlbum.TabIndex = 8;
            this.dSearchAlbum.Text = "Album";
            this.dSearchAlbum.UseVisualStyleBackColor = true;
            this.dSearchAlbum.Click += new System.EventHandler(this.dSearchAlbum_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 136);
            this.Controls.Add(this.dSearchAlbum);
            this.Controls.Add(this.dSearchArtist);
            this.Controls.Add(this.dPassword);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dUser);
            this.Controls.Add(this.dApiKey);
            this.Name = "MainWindow";
            this.Text = "Last.Fm demo";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox dApiKey;
        private System.Windows.Forms.TextBox dUser;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.MaskedTextBox dPassword;
        private System.Windows.Forms.Button dSearchArtist;
        private System.Windows.Forms.Button dSearchAlbum;

    }
}

