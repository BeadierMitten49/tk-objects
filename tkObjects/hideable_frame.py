import tkinter as tk


class HideableFrame(tk.Frame):
    def show(self):
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.pack_forget()