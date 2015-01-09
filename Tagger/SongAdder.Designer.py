namespace Tagger
{
    partial class SongAdder
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
            this.dAbort = new System.Windows.Forms.Button();
            this.dCurrent = new System.Windows.Forms.TextBox();
            this.dWorker = new System.ComponentModel.BackgroundWorker();
            this.SuspendLayout();
            // 
            // dAbort
            // 
            this.dAbort.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.dAbort.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.dAbort.Location = new System.Drawing.Point(329, 38);
            this.dAbort.Name = "dAbort";
            this.dAbort.Size = new System.Drawing.Size(75, 23);
            this.dAbort.TabIndex = 0;
            this.dAbort.Text = "Abort";
            this.dAbort.UseVisualStyleBackColor = true;
            this.dAbort.Click += new System.EventHandler(this.dAbort_Click);
            // 
            // dCurrent
            // 
            this.dCurrent.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dCurrent.Location = new System.Drawing.Point(12, 12);
            this.dCurrent.Name = "dCurrent";
            this.dCurrent.ReadOnly = true;
            this.dCurrent.Size = new System.Drawing.Size(392, 20);
            this.dCurrent.TabIndex = 1;
            // 
            // dWorker
            // 
            this.dWorker.WorkerReportsProgress = true;
            this.dWorker.WorkerSupportsCancellation = true;
            this.dWorker.DoWork += new System.ComponentModel.DoWorkEventHandler(this.dWorker_DoWork);
            this.dWorker.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.dWorker_RunWorkerCompleted);
            this.dWorker.ProgressChanged += new System.ComponentModel.ProgressChangedEventHandler(this.dWorker_ProgressChanged);
            // 
            // SongAdder
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.dAbort;
            this.ClientSize = new System.Drawing.Size(421, 78);
            this.Controls.Add(this.dCurrent);
            this.Controls.Add(this.dAbort);
            this.Name = "SongAdder";
            this.Text = "SongAdder";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button dAbort;
        private System.Windows.Forms.TextBox dCurrent;
        private System.ComponentModel.BackgroundWorker dWorker;
    }
}