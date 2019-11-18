namespace SeriesNamer
{
    partial class UpdateTool
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
            this.dOutput = new System.Windows.Forms.TextBox();
            this.dAbort = new System.Windows.Forms.Button();
            this.dProgress = new System.Windows.Forms.ProgressBar();
            this.dWork = new System.ComponentModel.BackgroundWorker();
            this.SuspendLayout();
            // 
            // dOutput
            // 
            this.dOutput.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dOutput.Location = new System.Drawing.Point(12, 41);
            this.dOutput.Multiline = true;
            this.dOutput.Name = "dOutput";
            this.dOutput.ReadOnly = true;
            this.dOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.dOutput.Size = new System.Drawing.Size(268, 156);
            this.dOutput.TabIndex = 0;
            this.dOutput.WordWrap = false;
            // 
            // dAbort
            // 
            this.dAbort.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.dAbort.Location = new System.Drawing.Point(209, 203);
            this.dAbort.Name = "dAbort";
            this.dAbort.Size = new System.Drawing.Size(75, 23);
            this.dAbort.TabIndex = 1;
            this.dAbort.Text = "Abort";
            this.dAbort.UseVisualStyleBackColor = true;
            this.dAbort.Click += new System.EventHandler(this.dAbort_Click);
            // 
            // dProgress
            // 
            this.dProgress.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dProgress.Location = new System.Drawing.Point(12, 12);
            this.dProgress.Name = "dProgress";
            this.dProgress.Size = new System.Drawing.Size(268, 23);
            this.dProgress.TabIndex = 2;
            // 
            // dWork
            // 
            this.dWork.WorkerReportsProgress = true;
            this.dWork.WorkerSupportsCancellation = true;
            this.dWork.DoWork += new System.ComponentModel.DoWorkEventHandler(this.dWork_DoWork);
            this.dWork.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.dWork_RunWorkerCompleted);
            this.dWork.ProgressChanged += new System.ComponentModel.ProgressChangedEventHandler(this.dWork_ProgressChanged);
            // 
            // UpdateTool
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 237);
            this.Controls.Add(this.dProgress);
            this.Controls.Add(this.dAbort);
            this.Controls.Add(this.dOutput);
            this.Name = "UpdateTool";
            this.Text = "UpdateTool";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox dOutput;
        private System.Windows.Forms.Button dAbort;
        private System.Windows.Forms.ProgressBar dProgress;
        private System.ComponentModel.BackgroundWorker dWork;
    }
}