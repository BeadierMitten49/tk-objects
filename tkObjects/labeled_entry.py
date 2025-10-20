import tkinter as tk


class LabelEntryFrame(tk.Frame):
    def __init__(self, parent, label_text, label_width=None, entry_width=None):
        super().__init__(parent)

        label = tk.Label(self, text=label_text, width=label_width)
        self.entry = tk.Entry(self, width=entry_width)

        label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1, sticky=tk.E)

    def get_text(self):
        return self.entry.get()

    def clear_text(self):
        self.entry.delete(0, tk.END)