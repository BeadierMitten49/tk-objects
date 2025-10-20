from .hideable_frame import HidebleFrame
from tkinter import ttk


class LoadingFrame(HidebleFrame):
    def __init__(self, parent):
        super().__init__(parent)

        pb2 = ttk.Progressbar(self, orient="horizontal", length=200, mode="indeterminate")
        pb2.pack(pady=20)
        pb2.start(20)
