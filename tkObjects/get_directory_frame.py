import tkinter as tk
from tkinter import filedialog


class GetDirectoryFrame(tk.Frame):
    def __init__(self, parent, button_text="Выбрать файл"):
        super().__init__(parent)

        self.selected_dir = None

        self.get_files_button = GetFilesButton(self, button_text)
        self.path_label = PathLabel(self)

        self.get_files_button.pack()
        self.path_label.pack(fill=tk.X)

    def get_selected_dir(self):
        if self.selected_dir:
            return self.selected_dir

    def clear_selected_dir(self):
        self.selected_dir = None
        self.path_label.update_label()


class GetFilesButton(tk.Button):
    def __init__(self, parent: GetDirectoryFrame, button_text):
        super().__init__(parent, text=button_text, command=self.on_click)
        self.parent = parent

    def on_click(self):
        self.parent.selected_dir = filedialog.askdirectory()
        self.parent.path_label.update_label()


class PathLabel(tk.Label):
    def __init__(self, parent: GetDirectoryFrame):
        super().__init__(parent, text="Не выбрано")
        self.parent = parent

    def update_label(self):
        print(self.parent.selected_dir)
        if self.parent.selected_dir:
            self.config(text=self.parent.selected_dir)

        else:
            self.config(text="Не выбрано")
