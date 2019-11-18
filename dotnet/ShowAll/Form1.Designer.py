namespace WindowsFormsApplication1
{
    partial class Form1
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
            this.dGo = new System.Windows.Forms.Button();
            this.dOutput = new System.Windows.Forms.TextBox();
            this.dInput = new System.Windows.Forms.TextBox();
            this.dWork = new System.ComponentModel.BackgroundWorker();
            this.SuspendLayout();
            // 
            // dGo
            // 
            this.dGo.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.dGo.Location = new System.Drawing.Point(484, 12);
            this.dGo.Name = "dGo";
            this.dGo.Size = new System.Drawing.Size(75, 23);
            this.dGo.TabIndex = 0;
            this.dGo.Text = "Go!";
            this.dGo.UseVisualStyleBackColor = true;
            this.dGo.Click += new System.EventHandler(this.dGo_Click);
            // 
            // dOutput
            // 
            this.dOutput.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dOutput.Location = new System.Drawing.Point(12, 38);
            this.dOutput.Multiline = true;
            this.dOutput.Name = "dOutput";
            this.dOutput.ReadOnly = true;
            this.dOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.dOutput.Size = new System.Drawing.Size(547, 346);
            this.dOutput.TabIndex = 1;
            this.dOutput.WordWrap = false;
            // 
            // dInput
            // 
            this.dInput.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dInput.Location = new System.Drawing.Point(12, 12);
            this.dInput.Name = "dInput";
            this.dInput.Size = new System.Drawing.Size(466, 20);
            this.dInput.TabIndex = 2;
            // 
            // dWork
            // 
            this.dWork.WorkerReportsProgress = true;
            this.dWork.DoWork += new System.ComponentModel.DoWorkEventHandler(this.dWork_DoWork);
            this.dWork.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.dWork_RunWorkerCompleted);
            this.dWork.ProgressChanged += new System.ComponentModel.ProgressChangedEventHandler(this.dWork_ProgressChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(571, 396);
            this.Controls.Add(this.dInput);
            this.Controls.Add(this.dOutput);
            this.Controls.Add(this.dGo);
            this.Name = "Form1";
            this.Text = "Show All!";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button dGo;
        private System.Windows.Forms.TextBox dOutput;
        private System.Windows.Forms.TextBox dInput;
        private System.ComponentModel.BackgroundWorker dWork;
    }
}

