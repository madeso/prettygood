using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing;
using System.Collections;

namespace PrettyGood.Util
{
	// todo: add sorting
	// todo: move formating to column/row script
	// todo: add gui for adding/removing/changing columns
	// todo: add editiable cels
	// todo: add filter function
	// todo: add saving above data
	public class Listview<T>
	{
		ListView view;
		Sorter sorter;

		private class Item
		{
			public T t;
			public int Index;
		}

		private class Sorter : IComparer
		{
			Listview<T> viewer;
			CaseInsensitiveComparer cmp = new CaseInsensitiveComparer();
			public SortOrder SortMethod = SortOrder.Ascending;
			public Column SelectedColumn = null;

			public Sorter(Listview<T> viewer)
			{
				this.viewer = viewer;
			}

			public int Compare(object x, object y)
			{
				if (SelectedColumn == null) return 0;
				var lx = (ListViewItem)x;
				var ly = (ListViewItem)y;
				Item ix = (Item)lx.Tag;
				Item iy = (Item)ly.Tag;
				string sx = viewer.resolve(SelectedColumn.Sort, ix.t);
				string sy = viewer.resolve(SelectedColumn.Sort, iy.t);
				int result = Strings.StringCompare(sx, sy);// cmp.Compare(sx, sy);

				switch (SortMethod)
				{
					case SortOrder.Ascending:
						return result;
					case SortOrder.Descending:
						return -result;
					default: // case SortOrder.None:
						return 0;
				}

			}
		}

		public Listview(ListView view)
		{
			if (null == view) throw new NullReferenceException();
			this.view = view;
			sorter = new Listview<T>.Sorter(this);

			view.ListViewItemSorter = sorter;
			view.View = View.Details;
			view.SmallImageList = new ImageList();
			view.LargeImageList = new ImageList();

			view.ColumnClick += new ColumnClickEventHandler(view_ColumnClick);
		}

		void view_ColumnClick(object sender, ColumnClickEventArgs e)
		{
			Column c = (Column)view.Columns[e.Column].Tag;

			if (c == sorter.SelectedColumn)
			{
				if (sorter.SortMethod == SortOrder.Ascending) sorter.SortMethod = SortOrder.Descending;
				else sorter.SortMethod = SortOrder.Ascending;
			}
			else
			{
				sorter.SelectedColumn = c;
				sorter.SortMethod = SortOrder.Ascending;
			}

			view.Sort();
			//removeAndAddAll();
		}

		private void removeAndAddAll()
		{
			view.BeginUpdate();

			List<ListViewItem> items = new List<ListViewItem>(view.Items.Count);
			foreach (ListViewItem v in view.Items) items.Add(v);
			view.Items.Clear();
			view.Items.AddRange(items.ToArray());

			view.EndUpdate();
		}

		public void add(Column c)
		{
			ColumnHeader ch = new ColumnHeader();
			ch.Tag = c;
			c.Header = ch;
			view.Columns.Add(ch);

			if (sorter.SelectedColumn == null) sorter.SelectedColumn = c;
		}

		public void specify(Column c, ColumnHeader ch)
		{
			ch.Tag = c;
			c.Header = ch;
		}

		IEnumerable<Column> Columns
		{
			get
			{
				foreach (ColumnHeader ch in view.Columns)
				{
					if (null == ch.Tag) yield return new Column(ch.Text);
					else yield return (Column)ch.Tag;
				}
			}
		}

		IndexCreator index = new IndexCreator();

		public ListViewItem add(T t)
		{
			ListViewItem it = new ListViewItem();
			Item i = new Item();
			i.t = t;
			it.Tag = i;
			i.Index = index.generate();
			updateText(it);
			view.Items.Add(it);
			return it;
		}

		public void updateText(ListViewItem it)
		{
			it.SubItems.Clear();
			bool first = true;

			Item i = (Item)it.Tag;
			T t = i.t;

			if (null == gf) it.Group = null;
			else it.Group = GetGroup(gf(t));

			if (bf != null)
			{
				it.Font = Gui.MakeBold(it.Font, bf(t));
			}

			SmallLargeImage si = null;
			if (smalliconf != null) si = smalliconf(t);
			if (si == null)
			{
				it.ImageIndex = -1;
			}
			else
			{
				it.ImageIndex = i.Index;
				Set(view.SmallImageList, i.Index, si.Small);
				Set(view.LargeImageList, i.Index, si.Large);
			}

			foreach (Column c in Columns)
			{
				string v = resolve(c.Display, t);
				if (first)
				{
					it.Text = v;
					first = false;
				}
				else
				{
					it.SubItems.Add(v);
				}
			}
		}

		static Bitmap emptyBitmap = new Bitmap(1, 1);

		private void Set(ImageList list, int index, Image image)
		{
			while (index >= list.Images.Count)
			{
				list.Images.Add(emptyBitmap);
			}
			list.Images[index] = image;
		}

		private ListViewGroup GetGroup(string p)
		{
			ListViewGroup g = view.Groups[p];
			if (g != null) return g;
			return view.Groups.Add(p, p);
		}

		Dictionary<string, Func<T, string>> converters = new Dictionary<string, Func<T, string>>();
		Func<T, string> gf;
		Func<T, bool> bf;
		Func<T, SmallLargeImage> smalliconf;

		public void add(string name, Func<T, string> c)
		{
			converters.Add(name, c);
		}

		public void groupfunction(Func<T, string> g)
		{
			gf = g;
		}

		public void icons(Func<T, SmallLargeImage> g)
		{
			smalliconf = g;
		}

		public void boldfunc(Func<T, bool> b)
		{
			bf = b;
		}

		private string lookup(T t, string name)
		{
			string ttl = name.ToLower();
			if (converters.ContainsKey(ttl))
			{
				return converters[ttl](t);
			}
			else return null;
		}

		public string resolve(Pattern p, T t)
		{
			return p.resolve(name => lookup(t, name));
		}

		public void clear()
		{
			view.Items.Clear();
			view.Groups.Clear();
			index.clear();
		}

		public T SingleSelectedItemOrNull
		{
			get
			{
				if (view.SelectedItems.Count != 1) return default(T);
				ListViewItem item = view.SelectedItems[0];
				return ((Item)item.Tag).t;
			}
		}
	}
}
