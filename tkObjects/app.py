import tkinter as tk


class App(tk.Tk):
    def __init__(self, width, height, title=None, **kwargs):
        super().__init__(**kwargs)
        self.title(title)

        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)

        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
