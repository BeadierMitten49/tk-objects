import tkinter as tk
from .flow_frame import FlowFrame


# ──────────────────────────────────────────────────────────────
class DataFlowFrame(FlowFrame):
    """FlowFrame для объектов с названием и метаданными, с кнопкой удаления"""
    def __init__(self, master, item_width=200, item_height=40, columns=3, **kwargs):
        super().__init__(master, item_width, item_height, columns, **kwargs)
        self.data_objects = []  # хранит словари {"text": ..., "meta": ..., "frame": ...}

    def add_data(self, text, meta):
        """Добавляет один объект с текстом и метаданными"""
        container = tk.Frame(self.inner, width=self.item_width, height=self.item_height, bg="#e0e0e0")
        container.pack_propagate(False)

        # Кнопка удалить слева
        btn_remove = tk.Button(container, text="✖", width=1, height=1, fg="red", bd=0, command=lambda: self.remove_data(container))
        btn_remove.pack(side="left", padx=2, pady=2)

        # Лейбл с текстом
        lbl = tk.Label(container, text=text, anchor="w", bg="#e0e0e0")
        lbl.pack(side="left", fill="both", expand=True, padx=2)

        self.widgets.append(container)
        self.data_objects.append({"text": text, "meta": meta, "frame": container})
        self._reposition_widgets()
        return container

    def add_multiple(self, items):
        """Добавляет массив объектов, каждый как (text, meta)"""
        for text, meta in items:
            self.add_data(text, meta)

    def remove_data(self, container):
        """Удаляет объект и его данные"""
        for obj in self.data_objects:
            if obj["frame"] == container:
                self.data_objects.remove(obj)
                break
        if container in self.widgets:
            self.widgets.remove(container)
            container.destroy()
        self._reposition_widgets()

    def get_all_texts(self):
        """Возвращает список всех текстов"""
        return [obj["text"] for obj in self.data_objects]

    def get_all_meta(self):
        """Возвращает список всех метаданных"""
        return [obj["meta"] for obj in self.data_objects]
