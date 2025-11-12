import tkinter as tk
from tkinter import filedialog, ttk
from .data_flow_frame import DataFlowFrame


class FilesSelector(tk.Frame):
    """Универсальный объект для выбора файлов с лимитом"""
    def __init__(self, master, canvas_width=400, canvas_height=100, file_limit=None, **kwargs):
        super().__init__(master, **kwargs)
        self.file_limit = file_limit  # Максимальное количество файлов
        self.select_button = ttk.Button(self, text="Выбрать файлы", command=self.open_file_dialog)
        self.selected_files_frame = DataFlowFrame(
            self,
            canvas_width=canvas_width,
            canvas_height=canvas_height,
            item_width=150,
            item_height=30,
            columns=3
        )

        self.select_button.pack(pady=5)
        self.selected_files_frame.pack(padx=5, pady=5)

    def open_file_dialog(self):
        """Открывает стандартный диалог выбора файлов"""
        files = filedialog.askopenfilenames(title="Выберите файлы")
        # Применяем лимит
        if self.file_limit is not None:
            remaining = self.file_limit - len(self.selected_files_frame.get_all_meta())
            files = files[:remaining]
            if remaining <= 0:
                return

        items = [(f.split("/")[-1], f) for f in files]  # Название файла + полный путь
        self.selected_files_frame.add_multiple(items)

    def get_selected_files(self):
        """Возвращает полный список выбранных файлов (пути)"""
        return self.selected_files_frame.get_all_meta()

    def get_selected_file_names(self):
        """Возвращает список только названий файлов"""
        return self.selected_files_frame.get_all_texts()

    def clear_all(self):
        """Очищает все выбранные файлы"""
        for widget in self.selected_files_frame.get_widgets():
            self.selected_files_frame.remove_widget(widget)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Universal File Selector Example")
    root.geometry("1000x1000")

    file_selector = FileSelector(root, height=20, width=100, file_limit=3)
    file_selector.pack()

    def show_files():
        print("Selected file names:", file_selector.get_selected_file_names())
        print("Selected full paths:", file_selector.get_selected_files())

    ttk.Button(root, text="Show Selected Files", command=show_files).pack(pady=5)

    root.mainloop()
