import tkinter as tk
from tkinter import ttk


class LoadingWindow(tk.Toplevel):
    def __init__(self, parent=None, title="Загрузка"):
        super().__init__(parent)
        self.title(title)

        self.grab_set()
        self.wm_overrideredirect(True)

        pb2 = ttk.Progressbar(self, orient="horizontal", length=200, mode="indeterminate")
        pb2.pack(pady=20)
        pb2.start(20)

