namespace SeriesNamer
{
    partial class StringPrompt
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
            this.dInfo = new System.Windows.Forms.Label();
            this.dOk = new System.Windows.Forms.Button();
            this.dCancel = new System.Windows.Forms.Button();
            this.dInput = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // dInfo
            // 
            this.dInfo.AutoSize = true;
            this.dInfo.Location = new System.Drawing.Point(12, 9);
            this.dInfo.Name = "dInfo";
            this.dInfo.Size = new System.Drawing.Size(35, 13);
            this.dInfo.TabIndex = 0;
            this.dInfo.Text = "label1";
            // 
            // dOk
            // 
            this.dOk.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dOk.Location = new System.Drawing.Point(124, 51);
            this.dOk.Name = "dOk";
            this.dOk.Size = new System.Drawing.Size(75, 23);
            this.dOk.TabIndex = 1;
            this.dOk.Text = "OK";
            this.dOk.UseVisualStyleBackColor = true;
            this.dOk.Click += new System.EventHandler(this.dOk_Click);
            // 
            // dCancel
            // 
            this.dCancel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.dCancel.Location = new System.Drawing.Point(205, 51);
            this.dCancel.Name = "dCancel";
            this.dCancel.Size = new System.Drawing.Size(75, 23);
            this.dCancel.TabIndex = 2;
            this.dCancel.Text = "Cancel";
            this.dCancel.UseVisualStyleBackColor = true;
            this.dCancel.Click += new System.EventHandler(this.dCancel_Click);
            // 
            // dInput
            // 
            this.dInput.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dInput.Location = new System.Drawing.Point(12, 25);
            this.dInput.Name = "dInput";
            this.dInput.Size = new System.Drawing.Size(268, 20);
            this.dInput.TabIndex = 3;
            // 
            // StringPrompt
            // 
            this.AcceptButton = this.dOk;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.dCancel;
            this.ClientSize = new System.Drawing.Size(292, 83);
            this.Controls.Add(this.dInput);
            this.Controls.Add(this.dCancel);
            this.Controls.Add(this.dOk);
            this.Controls.Add(this.dInfo);
            this.Name = "StringPrompt";
            this.Text = "StringPrompt";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label dInfo;
        private System.Windows.Forms.Button dOk;
        private System.Windows.Forms.Button dCancel;
        private System.Windows.Forms.TextBox dInput;
    }
}