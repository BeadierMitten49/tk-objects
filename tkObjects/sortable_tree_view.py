from tkinter import ttk


class SortableTreeview(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self._sort_column = None
        self._sort_reverse = None
        self._column_texts = {}

    def heading(self, column, option=None, **kw):
        if isinstance(option, str):
            return super().heading(column, option)

        text = kw.get("text")
        if text:
            self._column_texts[column] = text
            kw["command"] = lambda c=column: self.sort_by_column(c)

        return super().heading(column, **kw)

    def sort_by_column(self, col):
        data = [(self.set(item, col), item) for item in self.get_children('')]

        # Попробуем привести к числам (если получится)
        try:
            data = [(float(val), item) for val, item in data]
        except ValueError:
            pass

        # Определяем направление сортировки
        if self._sort_column == col:
            # Повторное нажатие — поменять направление
            reverse = not self._sort_reverse
        else:
            # Первое нажатие по колонке — сортировка по убыванию
            reverse = True

        data.sort(reverse=reverse)

        for index, (_, item) in enumerate(data):
            self.move(item, '', index)

        self._sort_column = col
        self._sort_reverse = reverse

        self._update_column_headers()

    def _update_column_headers(self):
        for col in self["columns"]:
            base = self._column_texts.get(col, col)
            arrow = ""
            if col == self._sort_column:
                arrow = " 🔻" if self._sort_reverse else " 🔺"
            super().heading(col, text=base + arrow)

