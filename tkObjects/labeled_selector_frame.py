import tkinter as tk


class LabeledSelectorFrame(tk.Frame):
    def __init__(self, parent, label_text, options, command=None):
        super().__init__(parent)

        self.label = tk.Label(self, text=label_text)
        self.selector = Selector(self, options, command)

        self.label.grid(row=0, column=0)
        self.selector.grid(row=0, column=1, sticky=tk.E)

    def get_selection(self):
        return self.selector.variable.get()


class Selector(tk.OptionMenu):
    def __init__(self, parent, options, command=None):
        self.command = command
        self.variable = tk.StringVar(value=options[0])
        super().__init__(parent, self.variable, *options, command=self.command)
