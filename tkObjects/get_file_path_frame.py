import tkinter as tk
from tkinter import filedialog


class GetFilePathFrame(tk.Frame):
    def __init__(self, parent, button_text="Выбрать файл"):
        super().__init__(parent)

        self.selected_files = None

        self.get_files_button = GetFilesButton(self, button_text)
        self.path_label = PathLabel(self)

        self.get_files_button.pack()
        self.path_label.pack(fill=tk.X)

    def get_selected_file(self):
        if self.selected_files:
            return self.selected_files[0]

    def get_selected_files(self):
        return self.selected_files

    def clear_selected_files(self):
        self.selected_files = None
        self.path_label.update_label()


class GetFilesButton(tk.Button):
    def __init__(self, parent: GetFilePathFrame, button_text):
        super().__init__(parent, text=button_text, command=self.on_click)
        self.parent = parent

    def on_click(self):
        self.parent.selected_files = filedialog.askopenfilenames()
        self.parent.path_label.update_label()


class PathLabel(tk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Не выбрано")
        self.parent = parent

    def update_label(self):
        if self.parent.selected_files:
            self.config(text=", \n".join(self.parent.selected_files))

        else:
            self.config(text="Не выбрано")
