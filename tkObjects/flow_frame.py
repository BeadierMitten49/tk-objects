import tkinter as tk
from tkinter import ttk


class FlowFrame(tk.Frame):
    def __init__(self, master,
                 item_width=150,
                 item_height=50,
                 columns=3,
                 canvas_width=100,
                 canvas_height=100,
                 **kwargs):
        super().__init__(master, **kwargs)
        self.item_width = item_width
        self.item_height = item_height
        self.columns = columns
        self.widgets = []

        # Canvas + scrollbars
        self.canvas = tk.Canvas(self, highlightthickness=0, width=canvas_width, height=canvas_height)
        self.v_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)

        self.inner = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner, anchor="nw")

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Bindings
        self.inner.bind("<Configure>", self._on_configure)
        self.canvas.bind("<Configure>", self._on_canvas_resize)
        self.canvas.bind("<Enter>", self._bind_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_mousewheel)
        self.inner.bind("<Enter>", self._bind_mousewheel)
        self.inner.bind("<Leave>", self._unbind_mousewheel)

    # Mousewheel
    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

    def _on_mousewheel(self, event):
        if event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")

    # Layout
    def _on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_resize(self, event):
        available_width = event.width
        new_columns = max(1, available_width // (self.item_width + 10))
        if new_columns != self.columns:
            self.columns = new_columns
            self._reposition_widgets()

    def _reposition_widgets(self):
        for index, widget in enumerate(self.widgets):
            row = index // self.columns
            col = index % self.columns
            widget.grid(row=row, column=col, padx=5, pady=5)
        self.inner.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # Widget management
    def add_widget(self, widget_class, *args, **kwargs):
        container = tk.Frame(self.inner, width=self.item_width, height=self.item_height)
        container.pack_propagate(False)
        widget = widget_class(container, *args, **kwargs)
        widget.pack(fill="both", expand=True)
        self.widgets.append(container)
        self._reposition_widgets()
        return widget

    def remove_widget(self, widget):
        for container in self.widgets:
            if widget.winfo_parent() == str(container):
                self.widgets.remove(container)
                container.destroy()
                break
        self._reposition_widgets()

    def get_widgets(self):
        result = []
        for container in self.widgets:
            children = container.winfo_children()
            if children:
                result.append(children[0])
        return result
