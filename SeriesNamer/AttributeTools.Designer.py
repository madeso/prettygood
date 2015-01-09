namespace SeriesNamer
{
    partial class AttributeTools
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
            this.components = new System.ComponentModel.Container();
            this.dDone = new System.Windows.Forms.Button();
            this.dAttributes = new System.Windows.Forms.ListView();
            this.columnHeaderValues = new System.Windows.Forms.ColumnHeader();
            this.columnHeaderAttribute = new System.Windows.Forms.ColumnHeader();
            this.dAttributeTools = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.capitalizeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.trimToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.replaceToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.trimAndReplaceToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.newAttributeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.stripLeadingZeroesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem2 = new System.Windows.Forms.ToolStripSeparator();
            this.dAttributeTools.SuspendLayout();
            this.SuspendLayout();
            // 
            // dDone
            // 
            this.dDone.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.dDone.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.dDone.Location = new System.Drawing.Point(205, 230);
            this.dDone.Name = "dDone";
            this.dDone.Size = new System.Drawing.Size(75, 23);
            this.dDone.TabIndex = 0;
            this.dDone.Text = "Done";
            this.dDone.UseVisualStyleBackColor = true;
            this.dDone.Click += new System.EventHandler(this.dDone_Click);
            // 
            // dAttributes
            // 
            this.dAttributes.AllowColumnReorder = true;
            this.dAttributes.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dAttributes.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeaderValues,
            this.columnHeaderAttribute});
            this.dAttributes.ContextMenuStrip = this.dAttributeTools;
            this.dAttributes.FullRowSelect = true;
            this.dAttributes.GridLines = true;
            this.dAttributes.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable;
            this.dAttributes.LabelEdit = true;
            this.dAttributes.LabelWrap = false;
            this.dAttributes.Location = new System.Drawing.Point(12, 12);
            this.dAttributes.Name = "dAttributes";
            this.dAttributes.Size = new System.Drawing.Size(268, 212);
            this.dAttributes.TabIndex = 1;
            this.dAttributes.UseCompatibleStateImageBehavior = false;
            this.dAttributes.View = System.Windows.Forms.View.Details;
            this.dAttributes.AfterLabelEdit += new System.Windows.Forms.LabelEditEventHandler(this.dAttributes_AfterLabelEdit);
            this.dAttributes.BeforeLabelEdit += new System.Windows.Forms.LabelEditEventHandler(this.dAttributes_BeforeLabelEdit);
            // 
            // columnHeaderValues
            // 
            this.columnHeaderValues.DisplayIndex = 1;
            this.columnHeaderValues.Text = "Attributes";
            this.columnHeaderValues.Width = 163;
            // 
            // columnHeaderAttribute
            // 
            this.columnHeaderAttribute.DisplayIndex = 0;
            this.columnHeaderAttribute.Text = "Values";
            this.columnHeaderAttribute.Width = 89;
            // 
            // dAttributeTools
            // 
            this.dAttributeTools.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.capitalizeToolStripMenuItem,
            this.trimAndReplaceToolStripMenuItem,
            this.stripLeadingZeroesToolStripMenuItem,
            this.toolStripMenuItem2,
            this.trimToolStripMenuItem,
            this.replaceToolStripMenuItem,
            this.toolStripMenuItem1,
            this.newAttributeToolStripMenuItem});
            this.dAttributeTools.Name = "dAttributeTools";
            this.dAttributeTools.Size = new System.Drawing.Size(206, 170);
            // 
            // capitalizeToolStripMenuItem
            // 
            this.capitalizeToolStripMenuItem.Name = "capitalizeToolStripMenuItem";
            this.capitalizeToolStripMenuItem.Size = new System.Drawing.Size(205, 22);
            this.capitalizeToolStripMenuItem.Text = "Capitalize";
            this.capitalizeToolStripMenuItem.Click += new System.EventHandler(this.capitalizeToolStripMenuItem_Click);
            // 
            // trimToolStripMenuItem
            // 
            this.trimToolStripMenuItem.Name = "trimToolStripMenuItem";
            this.trimToolStripMenuItem.Size = new System.Drawing.Size(205, 22);
            this.trimToolStripMenuItem.Text = "Trim";
            this.trimToolStripMenuItem.Click += new System.EventHandler(this.trimToolStripMenuItem_Click);
            // 
            // replaceToolStripMenuItem
            // 
            this.replaceToolStripMenuItem.Name = "replaceToolStripMenuItem";
            this.replaceToolStripMenuItem.Size = new System.Drawing.Size(205, 22);
            this.replaceToolStripMenuItem.Text = "Replace";
            this.replaceToolStripMenuItem.Click += new System.EventHandler(this.replaceToolStripMenuItem_Click);
            // 
            // trimAndReplaceToolStripMenuItem
            // 
            this.trimAndReplaceToolStripMenuItem.Name = "trimAndReplaceToolStripMenuItem";
            this.trimAndReplaceToolStripMenuItem.Size = new System.Drawing.Size(205, 22);
            this.trimAndReplaceToolStripMenuItem.Text = "Trim and replace";
            this.trimAndReplaceToolStripMenuItem.Click += new System.EventHandler(this.trimAndReplaceToolStripMenuItem_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(202, 6);
            // 
            // newAttributeToolStripMenuItem
            // 
            this.newAttributeToolStripMenuItem.Name = "newAttributeToolStripMenuItem";
            this.newAttributeToolStripMenuItem.Size = new System.Drawing.Size(205, 22);
            this.newAttributeToolStripMenuItem.Text = "New attribute...";
            this.newAttributeToolStripMenuItem.Click += new System.EventHandler(this.newAttributeToolStripMenuItem_Click);
            // 
            // stripLeadingZeroesToolStripMenuItem
            // 
            this.stripLeadingZeroesToolStripMenuItem.Name = "stripLeadingZeroesToolStripMenuItem";
            this.stripLeadingZeroesToolStripMenuItem.Size = new System.Drawing.Size(205, 22);
            this.stripLeadingZeroesToolStripMenuItem.Text = "Strip leading zeroes";
            this.stripLeadingZeroesToolStripMenuItem.Click += new System.EventHandler(this.stripLeadingZeroesToolStripMenuItem_Click);
            // 
            // toolStripMenuItem2
            // 
            this.toolStripMenuItem2.Name = "toolStripMenuItem2";
            this.toolStripMenuItem2.Size = new System.Drawing.Size(202, 6);
            // 
            // AttributeTools
            // 
            this.AcceptButton = this.dDone;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.dDone;
            this.ClientSize = new System.Drawing.Size(292, 265);
            this.Controls.Add(this.dAttributes);
            this.Controls.Add(this.dDone);
            this.DoubleBuffered = true;
            this.Name = "AttributeTools";
            this.Text = "AttributeTools";
            this.dAttributeTools.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button dDone;
        private System.Windows.Forms.ListView dAttributes;
        private System.Windows.Forms.ContextMenuStrip dAttributeTools;
        private System.Windows.Forms.ColumnHeader columnHeaderAttribute;
        private System.Windows.Forms.ColumnHeader columnHeaderValues;
        private System.Windows.Forms.ToolStripMenuItem capitalizeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem trimToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem replaceToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem trimAndReplaceToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem newAttributeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem stripLeadingZeroesToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem2;
    }
}