import tkinter as tk


class LabelTextField(tk.Frame):
    def __init__(self, parent, label_text="Введи сюда свою срань: "):
        super().__init__(parent)
        label = tk.Label(self, text=label_text)
        self.text_field = TextField(self)

        label.grid(column=0, row=0)
        self.text_field.grid(column=0, row=1)

    def set_text(self, text):
        self.text_field.set_text(text)

    def get_text(self):
        text = self.text_field.get_text()
        if text == "\n":
            return None
        return self.text_field.get_text()

    def clear(self):
        self.text_field.clear()


class TextField(tk.Text):
    def __init__(self, parent):
        super().__init__(parent, width=50, height=5)
        self.parent = parent

    def set_text(self, text):
        self.delete(1.0, tk.END)
        self.insert(tk.END, text)

    def get_text(self):
        return self.get(1.0, tk.END)

    def clear(self):
        self.delete(1.0, tk.END)
