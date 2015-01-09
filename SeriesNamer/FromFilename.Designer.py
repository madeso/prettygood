namespace SeriesNamer
{
    partial class FromFilename
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
            this.dDone = new System.Windows.Forms.Button();
            this.dResult = new System.Windows.Forms.ListView();
            this.dPattern = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // dDone
            // 
            this.dDone.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.dDone.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.dDone.Location = new System.Drawing.Point(460, 286);
            this.dDone.Name = "dDone";
            this.dDone.Size = new System.Drawing.Size(75, 23);
            this.dDone.TabIndex = 1;
            this.dDone.Text = "Done";
            this.dDone.UseVisualStyleBackColor = true;
            this.dDone.Click += new System.EventHandler(this.dDone_Click);
            // 
            // dResult
            // 
            this.dResult.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dResult.FullRowSelect = true;
            this.dResult.GridLines = true;
            this.dResult.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable;
            this.dResult.Location = new System.Drawing.Point(12, 38);
            this.dResult.Name = "dResult";
            this.dResult.Size = new System.Drawing.Size(523, 242);
            this.dResult.TabIndex = 2;
            this.dResult.UseCompatibleStateImageBehavior = false;
            this.dResult.View = System.Windows.Forms.View.Details;
            // 
            // dPattern
            // 
            this.dPattern.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dPattern.Location = new System.Drawing.Point(12, 12);
            this.dPattern.Name = "dPattern";
            this.dPattern.Size = new System.Drawing.Size(523, 20);
            this.dPattern.TabIndex = 3;
            this.dPattern.TextChanged += new System.EventHandler(this.dPattern_TextChanged);
            // 
            // FromFilename
            // 
            this.AcceptButton = this.dDone;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.dDone;
            this.ClientSize = new System.Drawing.Size(547, 321);
            this.Controls.Add(this.dPattern);
            this.Controls.Add(this.dResult);
            this.Controls.Add(this.dDone);
            this.DoubleBuffered = true;
            this.Name = "FromFilename";
            this.Text = "From filename";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button dDone;
        private System.Windows.Forms.ListView dResult;
        private System.Windows.Forms.TextBox dPattern;
    }
}