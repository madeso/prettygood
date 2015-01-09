namespace Seymour
{
	partial class Main
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
			this.dMainSplit = new System.Windows.Forms.SplitContainer();
			this.dFeeds = new BrightIdeasSoftware.TreeListView();
			this.olvFeedname = new BrightIdeasSoftware.OLVColumn();
			this.dFeedsContextStrip = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.addFeedToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.addFolderToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.importOpmlToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.updateToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
			this.dSubSplit = new System.Windows.Forms.SplitContainer();
			this.dItems = new BrightIdeasSoftware.ObjectListView();
			this.olvName = new BrightIdeasSoftware.OLVColumn();
			this.olvDate = new BrightIdeasSoftware.OLVColumn();
			this.dBrowse = new System.Windows.Forms.WebBrowser();
			this.dSearch = new System.Windows.Forms.TextBox();
			this.dTopHeader = new System.Windows.Forms.FlowLayoutPanel();
			this.dFullscreen = new System.Windows.Forms.Button();
			this.flowLayoutPanel1 = new System.Windows.Forms.FlowLayoutPanel();
			this.flowLayoutPanel2 = new System.Windows.Forms.FlowLayoutPanel();
			this.dFeedTitle = new System.Windows.Forms.LinkLabel();
			this.dPostTitle = new System.Windows.Forms.LinkLabel();
			this.dItemCount = new System.Windows.Forms.Label();
			this.dSubTitle = new System.Windows.Forms.Label();
			this.dStrip = new System.Windows.Forms.StatusStrip();
			this.dUpdateProgress = new System.Windows.Forms.ToolStripProgressBar();
			this.dStatusText = new System.Windows.Forms.ToolStripStatusLabel();
			this.dWebPageProgress = new System.Windows.Forms.ToolStripProgressBar();
			this.dProgressBytes = new System.Windows.Forms.ToolStripStatusLabel();
			this.dHtmlLinkInfo = new System.Windows.Forms.ToolStripStatusLabel();
			this.dNotify = new System.Windows.Forms.NotifyIcon(this.components);
			this.dNotifyMenuStrip = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.updateToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.dUpdator = new System.ComponentModel.BackgroundWorker();
			this.dOpmlBrowser = new System.Windows.Forms.OpenFileDialog();
			this.dMainSplit.Panel1.SuspendLayout();
			this.dMainSplit.Panel2.SuspendLayout();
			this.dMainSplit.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.dFeeds)).BeginInit();
			this.dFeedsContextStrip.SuspendLayout();
			this.dSubSplit.Panel1.SuspendLayout();
			this.dSubSplit.Panel2.SuspendLayout();
			this.dSubSplit.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.dItems)).BeginInit();
			this.dTopHeader.SuspendLayout();
			this.flowLayoutPanel1.SuspendLayout();
			this.flowLayoutPanel2.SuspendLayout();
			this.dStrip.SuspendLayout();
			this.dNotifyMenuStrip.SuspendLayout();
			this.SuspendLayout();
			// 
			// dMainSplit
			// 
			this.dMainSplit.Dock = System.Windows.Forms.DockStyle.Fill;
			this.dMainSplit.Location = new System.Drawing.Point(0, 58);
			this.dMainSplit.Name = "dMainSplit";
			// 
			// dMainSplit.Panel1
			// 
			this.dMainSplit.Panel1.Controls.Add(this.dFeeds);
			// 
			// dMainSplit.Panel2
			// 
			this.dMainSplit.Panel2.Controls.Add(this.dSubSplit);
			this.dMainSplit.Size = new System.Drawing.Size(642, 398);
			this.dMainSplit.SplitterDistance = 213;
			this.dMainSplit.TabIndex = 0;
			// 
			// dFeeds
			// 
			this.dFeeds.AllColumns.Add(this.olvFeedname);
			this.dFeeds.CellEditActivation = BrightIdeasSoftware.ObjectListView.CellEditActivateMode.DoubleClick;
			this.dFeeds.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.olvFeedname});
			this.dFeeds.ContextMenuStrip = this.dFeedsContextStrip;
			this.dFeeds.Dock = System.Windows.Forms.DockStyle.Fill;
			this.dFeeds.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.None;
			this.dFeeds.Location = new System.Drawing.Point(0, 0);
			this.dFeeds.Name = "dFeeds";
			this.dFeeds.OwnerDraw = true;
			this.dFeeds.ShowGroups = false;
			this.dFeeds.Size = new System.Drawing.Size(213, 398);
			this.dFeeds.TabIndex = 0;
			this.dFeeds.UseCompatibleStateImageBehavior = false;
			this.dFeeds.View = System.Windows.Forms.View.Details;
			this.dFeeds.VirtualMode = true;
			this.dFeeds.SelectionChanged += new System.EventHandler(this.dFeeds_SelectionChanged);
			// 
			// olvFeedname
			// 
			this.olvFeedname.AspectName = "NameAndCount";
			this.olvFeedname.FillsFreeSpace = true;
			// 
			// dFeedsContextStrip
			// 
			this.dFeedsContextStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.addFeedToolStripMenuItem,
            this.addFolderToolStripMenuItem,
            this.importOpmlToolStripMenuItem,
            this.updateToolStripMenuItem1});
			this.dFeedsContextStrip.Name = "dFeedsContextStrip";
			this.dFeedsContextStrip.Size = new System.Drawing.Size(155, 92);
			// 
			// addFeedToolStripMenuItem
			// 
			this.addFeedToolStripMenuItem.Name = "addFeedToolStripMenuItem";
			this.addFeedToolStripMenuItem.Size = new System.Drawing.Size(154, 22);
			this.addFeedToolStripMenuItem.Text = "Add feed...";
			this.addFeedToolStripMenuItem.Click += new System.EventHandler(this.addFeedToolStripMenuItem_Click);
			// 
			// addFolderToolStripMenuItem
			// 
			this.addFolderToolStripMenuItem.Name = "addFolderToolStripMenuItem";
			this.addFolderToolStripMenuItem.Size = new System.Drawing.Size(154, 22);
			this.addFolderToolStripMenuItem.Text = "Add folder";
			this.addFolderToolStripMenuItem.Click += new System.EventHandler(this.addFolderToolStripMenuItem_Click);
			// 
			// importOpmlToolStripMenuItem
			// 
			this.importOpmlToolStripMenuItem.Name = "importOpmlToolStripMenuItem";
			this.importOpmlToolStripMenuItem.Size = new System.Drawing.Size(154, 22);
			this.importOpmlToolStripMenuItem.Text = "Import opml...";
			this.importOpmlToolStripMenuItem.Click += new System.EventHandler(this.importOpmlToolStripMenuItem_Click);
			// 
			// updateToolStripMenuItem1
			// 
			this.updateToolStripMenuItem1.Name = "updateToolStripMenuItem1";
			this.updateToolStripMenuItem1.Size = new System.Drawing.Size(154, 22);
			this.updateToolStripMenuItem1.Text = "Update";
			this.updateToolStripMenuItem1.Click += new System.EventHandler(this.updateToolStripMenuItem1_Click);
			// 
			// dSubSplit
			// 
			this.dSubSplit.Dock = System.Windows.Forms.DockStyle.Fill;
			this.dSubSplit.Location = new System.Drawing.Point(0, 0);
			this.dSubSplit.Name = "dSubSplit";
			this.dSubSplit.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// dSubSplit.Panel1
			// 
			this.dSubSplit.Panel1.Controls.Add(this.dItems);
			// 
			// dSubSplit.Panel2
			// 
			this.dSubSplit.Panel2.Controls.Add(this.dBrowse);
			this.dSubSplit.Size = new System.Drawing.Size(425, 398);
			this.dSubSplit.SplitterDistance = 143;
			this.dSubSplit.TabIndex = 0;
			// 
			// dItems
			// 
			this.dItems.Activation = System.Windows.Forms.ItemActivation.OneClick;
			this.dItems.AllColumns.Add(this.olvName);
			this.dItems.AllColumns.Add(this.olvDate);
			this.dItems.AllowColumnReorder = true;
			this.dItems.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.olvName,
            this.olvDate});
			this.dItems.Dock = System.Windows.Forms.DockStyle.Fill;
			this.dItems.FullRowSelect = true;
			this.dItems.Location = new System.Drawing.Point(0, 0);
			this.dItems.Name = "dItems";
			this.dItems.Size = new System.Drawing.Size(425, 143);
			this.dItems.SortGroupItemsByPrimaryColumn = false;
			this.dItems.TabIndex = 1;
			this.dItems.UseAlternatingBackColors = true;
			this.dItems.UseCompatibleStateImageBehavior = false;
			this.dItems.UseHotItem = true;
			this.dItems.View = System.Windows.Forms.View.Details;
			this.dItems.SelectedIndexChanged += new System.EventHandler(this.dItems_SelectedIndexChanged);
			// 
			// olvName
			// 
			this.olvName.AspectName = "Item.Title";
			this.olvName.FillsFreeSpace = true;
			this.olvName.IsEditable = false;
			this.olvName.IsTileViewColumn = true;
			this.olvName.Text = "Name";
			this.olvName.UseInitialLetterForGroup = true;
			// 
			// olvDate
			// 
			this.olvDate.AspectName = "Item.Updated";
			this.olvDate.IsEditable = false;
			this.olvDate.IsTileViewColumn = true;
			this.olvDate.Text = "Date";
			this.olvDate.Width = 90;
			// 
			// dBrowse
			// 
			this.dBrowse.Dock = System.Windows.Forms.DockStyle.Fill;
			this.dBrowse.Location = new System.Drawing.Point(0, 0);
			this.dBrowse.MinimumSize = new System.Drawing.Size(20, 20);
			this.dBrowse.Name = "dBrowse";
			this.dBrowse.Size = new System.Drawing.Size(425, 251);
			this.dBrowse.TabIndex = 0;
			this.dBrowse.ProgressChanged += new System.Windows.Forms.WebBrowserProgressChangedEventHandler(this.dBrowse_ProgressChanged);
			this.dBrowse.Navigating += new System.Windows.Forms.WebBrowserNavigatingEventHandler(this.dBrowse_Navigating);
			this.dBrowse.DocumentCompleted += new System.Windows.Forms.WebBrowserDocumentCompletedEventHandler(this.dBrowse_DocumentCompleted);
			// 
			// dSearch
			// 
			this.dSearch.Location = new System.Drawing.Point(9, 19);
			this.dSearch.Margin = new System.Windows.Forms.Padding(9, 19, 3, 3);
			this.dSearch.Name = "dSearch";
			this.dSearch.Size = new System.Drawing.Size(100, 20);
			this.dSearch.TabIndex = 0;
			this.dSearch.WordWrap = false;
			// 
			// dTopHeader
			// 
			this.dTopHeader.BackColor = System.Drawing.SystemColors.ControlDark;
			this.dTopHeader.Controls.Add(this.dSearch);
			this.dTopHeader.Controls.Add(this.dFullscreen);
			this.dTopHeader.Controls.Add(this.flowLayoutPanel1);
			this.dTopHeader.Dock = System.Windows.Forms.DockStyle.Top;
			this.dTopHeader.Location = new System.Drawing.Point(0, 0);
			this.dTopHeader.Name = "dTopHeader";
			this.dTopHeader.Size = new System.Drawing.Size(642, 58);
			this.dTopHeader.TabIndex = 2;
			this.dTopHeader.WrapContents = false;
			// 
			// dFullscreen
			// 
			this.dFullscreen.Location = new System.Drawing.Point(115, 18);
			this.dFullscreen.Margin = new System.Windows.Forms.Padding(3, 18, 3, 3);
			this.dFullscreen.Name = "dFullscreen";
			this.dFullscreen.Size = new System.Drawing.Size(24, 23);
			this.dFullscreen.TabIndex = 3;
			this.dFullscreen.Text = "F";
			this.dFullscreen.UseVisualStyleBackColor = true;
			this.dFullscreen.Click += new System.EventHandler(this.dFullscreen_Click);
			// 
			// flowLayoutPanel1
			// 
			this.flowLayoutPanel1.AutoSize = true;
			this.flowLayoutPanel1.Controls.Add(this.flowLayoutPanel2);
			this.flowLayoutPanel1.Controls.Add(this.dSubTitle);
			this.flowLayoutPanel1.FlowDirection = System.Windows.Forms.FlowDirection.TopDown;
			this.flowLayoutPanel1.Location = new System.Drawing.Point(145, 3);
			this.flowLayoutPanel1.Name = "flowLayoutPanel1";
			this.flowLayoutPanel1.Size = new System.Drawing.Size(318, 50);
			this.flowLayoutPanel1.TabIndex = 4;
			// 
			// flowLayoutPanel2
			// 
			this.flowLayoutPanel2.AutoSize = true;
			this.flowLayoutPanel2.Controls.Add(this.dFeedTitle);
			this.flowLayoutPanel2.Controls.Add(this.dPostTitle);
			this.flowLayoutPanel2.Controls.Add(this.dItemCount);
			this.flowLayoutPanel2.Location = new System.Drawing.Point(3, 3);
			this.flowLayoutPanel2.Name = "flowLayoutPanel2";
			this.flowLayoutPanel2.Size = new System.Drawing.Size(312, 31);
			this.flowLayoutPanel2.TabIndex = 3;
			// 
			// dFeedTitle
			// 
			this.dFeedTitle.AutoSize = true;
			this.dFeedTitle.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.dFeedTitle.Location = new System.Drawing.Point(3, 0);
			this.dFeedTitle.Name = "dFeedTitle";
			this.dFeedTitle.Size = new System.Drawing.Size(135, 31);
			this.dFeedTitle.TabIndex = 4;
			this.dFeedTitle.TabStop = true;
			this.dFeedTitle.Text = "Feed Title";
			this.dFeedTitle.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.dFeedTitle_LinkClicked);
			// 
			// dPostTitle
			// 
			this.dPostTitle.AutoSize = true;
			this.dPostTitle.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.dPostTitle.Location = new System.Drawing.Point(144, 11);
			this.dPostTitle.Margin = new System.Windows.Forms.Padding(3, 11, 3, 0);
			this.dPostTitle.Name = "dPostTitle";
			this.dPostTitle.Size = new System.Drawing.Size(69, 20);
			this.dPostTitle.TabIndex = 5;
			this.dPostTitle.TabStop = true;
			this.dPostTitle.Text = "post title";
			this.dPostTitle.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.dPostTitle_LinkClicked);
			// 
			// dItemCount
			// 
			this.dItemCount.AutoSize = true;
			this.dItemCount.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.dItemCount.Location = new System.Drawing.Point(219, 11);
			this.dItemCount.Margin = new System.Windows.Forms.Padding(3, 11, 3, 0);
			this.dItemCount.Name = "dItemCount";
			this.dItemCount.Size = new System.Drawing.Size(90, 20);
			this.dItemCount.TabIndex = 2;
			this.dItemCount.Text = "913 unread";
			// 
			// dSubTitle
			// 
			this.dSubTitle.AutoSize = true;
			this.dSubTitle.Location = new System.Drawing.Point(3, 37);
			this.dSubTitle.Name = "dSubTitle";
			this.dSubTitle.Padding = new System.Windows.Forms.Padding(15, 0, 0, 0);
			this.dSubTitle.Size = new System.Drawing.Size(145, 13);
			this.dSubTitle.TabIndex = 4;
			this.dSubTitle.Text = "Some wicked cool subtitle";
			// 
			// dStrip
			// 
			this.dStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.dUpdateProgress,
            this.dStatusText,
            this.dWebPageProgress,
            this.dProgressBytes,
            this.dHtmlLinkInfo});
			this.dStrip.Location = new System.Drawing.Point(0, 456);
			this.dStrip.Name = "dStrip";
			this.dStrip.Size = new System.Drawing.Size(642, 22);
			this.dStrip.TabIndex = 3;
			this.dStrip.Text = "statusStrip1";
			// 
			// dUpdateProgress
			// 
			this.dUpdateProgress.Name = "dUpdateProgress";
			this.dUpdateProgress.Size = new System.Drawing.Size(100, 16);
			this.dUpdateProgress.Visible = false;
			// 
			// dStatusText
			// 
			this.dStatusText.Name = "dStatusText";
			this.dStatusText.Size = new System.Drawing.Size(50, 17);
			this.dStatusText.Text = "Ready...";
			// 
			// dWebPageProgress
			// 
			this.dWebPageProgress.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
			this.dWebPageProgress.Name = "dWebPageProgress";
			this.dWebPageProgress.Size = new System.Drawing.Size(100, 16);
			this.dWebPageProgress.Visible = false;
			// 
			// dProgressBytes
			// 
			this.dProgressBytes.Name = "dProgressBytes";
			this.dProgressBytes.Size = new System.Drawing.Size(109, 17);
			this.dProgressBytes.Text = "toolStripStatusLabel1";
			// 
			// dHtmlLinkInfo
			// 
			this.dHtmlLinkInfo.Name = "dHtmlLinkInfo";
			this.dHtmlLinkInfo.Size = new System.Drawing.Size(82, 17);
			this.dHtmlLinkInfo.Text = "www.google.se";
			// 
			// dNotify
			// 
			this.dNotify.ContextMenuStrip = this.dNotifyMenuStrip;
			this.dNotify.Text = "notifyIcon1";
			this.dNotify.Visible = true;
			this.dNotify.MouseClick += new System.Windows.Forms.MouseEventHandler(this.dNotify_MouseClick);
			// 
			// dNotifyMenuStrip
			// 
			this.dNotifyMenuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.updateToolStripMenuItem});
			this.dNotifyMenuStrip.Name = "dNotifyMenuStrip";
			this.dNotifyMenuStrip.Size = new System.Drawing.Size(133, 26);
			// 
			// updateToolStripMenuItem
			// 
			this.updateToolStripMenuItem.Name = "updateToolStripMenuItem";
			this.updateToolStripMenuItem.Size = new System.Drawing.Size(132, 22);
			this.updateToolStripMenuItem.Text = "Update...";
			this.updateToolStripMenuItem.Click += new System.EventHandler(this.updateToolStripMenuItem_Click);
			// 
			// dUpdator
			// 
			this.dUpdator.WorkerReportsProgress = true;
			this.dUpdator.DoWork += new System.ComponentModel.DoWorkEventHandler(this.dUpdator_DoWork);
			this.dUpdator.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.dUpdator_RunWorkerCompleted);
			this.dUpdator.ProgressChanged += new System.ComponentModel.ProgressChangedEventHandler(this.dUpdator_ProgressChanged);
			// 
			// dOpmlBrowser
			// 
			this.dOpmlBrowser.Filter = "OPML files|*.opml|All files|*.*";
			// 
			// Main
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(642, 478);
			this.Controls.Add(this.dMainSplit);
			this.Controls.Add(this.dStrip);
			this.Controls.Add(this.dTopHeader);
			this.Name = "Main";
			this.Text = "Seymour";
			this.dMainSplit.Panel1.ResumeLayout(false);
			this.dMainSplit.Panel2.ResumeLayout(false);
			this.dMainSplit.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.dFeeds)).EndInit();
			this.dFeedsContextStrip.ResumeLayout(false);
			this.dSubSplit.Panel1.ResumeLayout(false);
			this.dSubSplit.Panel2.ResumeLayout(false);
			this.dSubSplit.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.dItems)).EndInit();
			this.dTopHeader.ResumeLayout(false);
			this.dTopHeader.PerformLayout();
			this.flowLayoutPanel1.ResumeLayout(false);
			this.flowLayoutPanel1.PerformLayout();
			this.flowLayoutPanel2.ResumeLayout(false);
			this.flowLayoutPanel2.PerformLayout();
			this.dStrip.ResumeLayout(false);
			this.dStrip.PerformLayout();
			this.dNotifyMenuStrip.ResumeLayout(false);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.SplitContainer dMainSplit;
		private System.Windows.Forms.TextBox dSearch;
		private System.Windows.Forms.FlowLayoutPanel dTopHeader;
		private System.Windows.Forms.Label dItemCount;
		private System.Windows.Forms.SplitContainer dSubSplit;
		private System.Windows.Forms.WebBrowser dBrowse;
		private System.Windows.Forms.Button dFullscreen;
		private System.Windows.Forms.StatusStrip dStrip;
		private System.Windows.Forms.ToolStripProgressBar dUpdateProgress;
		private System.Windows.Forms.ToolStripStatusLabel dStatusText;
		private System.Windows.Forms.NotifyIcon dNotify;
		private System.Windows.Forms.ContextMenuStrip dNotifyMenuStrip;
		private System.Windows.Forms.ToolStripMenuItem updateToolStripMenuItem;
		private System.ComponentModel.BackgroundWorker dUpdator;
		private System.Windows.Forms.FlowLayoutPanel flowLayoutPanel1;
		private System.Windows.Forms.FlowLayoutPanel flowLayoutPanel2;
		private System.Windows.Forms.Label dSubTitle;
		private System.Windows.Forms.ToolStripStatusLabel dHtmlLinkInfo;
		private System.Windows.Forms.ToolStripProgressBar dWebPageProgress;
		private System.Windows.Forms.LinkLabel dFeedTitle;
		private System.Windows.Forms.ToolStripStatusLabel dProgressBytes;
		private System.Windows.Forms.LinkLabel dPostTitle;
		private BrightIdeasSoftware.ObjectListView dItems;
		private BrightIdeasSoftware.OLVColumn olvName;
		private BrightIdeasSoftware.OLVColumn olvDate;
		private BrightIdeasSoftware.TreeListView dFeeds;
		private BrightIdeasSoftware.OLVColumn olvFeedname;
		private System.Windows.Forms.ContextMenuStrip dFeedsContextStrip;
		private System.Windows.Forms.ToolStripMenuItem addFeedToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem importOpmlToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem updateToolStripMenuItem1;
		private System.Windows.Forms.OpenFileDialog dOpmlBrowser;
		private System.Windows.Forms.ToolStripMenuItem addFolderToolStripMenuItem;


	}
}

