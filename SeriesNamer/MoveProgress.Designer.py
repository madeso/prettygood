namespace SeriesNamer
{
    partial class MoveProgress
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
            this.dProgress = new System.Windows.Forms.ProgressBar();
            this.dResult = new System.Windows.Forms.TextBox();
            this.dWorker = new System.ComponentModel.BackgroundWorker();
            this.SuspendLayout();
            // 
            // dProgress
            // 
            this.dProgress.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dProgress.Location = new System.Drawing.Point(12, 12);
            this.dProgress.Name = "dProgress";
            this.dProgress.Size = new System.Drawing.Size(268, 19);
            this.dProgress.TabIndex = 1;
            // 
            // dResult
            // 
            this.dResult.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dResult.Location = new System.Drawing.Point(12, 37);
            this.dResult.Multiline = true;
            this.dResult.Name = "dResult";
            this.dResult.ReadOnly = true;
            this.dResult.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.dResult.Size = new System.Drawing.Size(268, 216);
            this.dResult.TabIndex = 2;
            this.dResult.WordWrap = false;
            // 
            // dWorker
            // 
            this.dWorker.WorkerReportsProgress = true;
            this.dWorker.WorkerSupportsCancellation = true;
            this.dWorker.DoWork += new System.ComponentModel.DoWorkEventHandler(this.dWorker_DoWork);
            this.dWorker.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.dWorker_RunWorkerCompleted);
            this.dWorker.ProgressChanged += new System.ComponentModel.ProgressChangedEventHandler(this.dWorker_ProgressChanged);
            // 
            // MoverDialog
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 265);
            this.Controls.Add(this.dResult);
            this.Controls.Add(this.dProgress);
            this.Name = "MoverDialog";
            this.Text = "MoverDialog";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ProgressBar dProgress;
        private System.Windows.Forms.TextBox dResult;
        private System.ComponentModel.BackgroundWorker dWorker;
    }
}