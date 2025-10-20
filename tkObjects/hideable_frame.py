import tkinter as tk


class HidebleFrame(tk.Frame):
    def show(self):
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.pack_forget()