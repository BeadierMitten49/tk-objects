import tkinter as tk
from tkinter import ttk
from typing import Callable, Type, Union


class ButtonsList(tk.Frame):
    """
    A flexible vertical container for buttons and additional UI elements in Tkinter.

    The `ButtonsList` class simplifies the creation of structured button panels,
    settings menus, or grouped action lists. It supports not only regular buttons,
    but also special items like titles, spacers, and horizontal dividers.

    Example structure:
        buttons = [
            ("__title__", "Main Actions"),
            ("Button 1", lambda: print("Clicked 1")),
            ("Button 2", lambda: print("Clicked 2")),
            ("__line__", {"height": 2, "color": "#888"}),
            ("Button 3", lambda: print("Clicked 3")),
            ("__space__", 10),
            ("__title__", "Other"),
            ("Exit", lambda: root.destroy),
        ]

    Special commands:
        • "__title__" — adds a bold text label (section title)
        • "__space__" — adds a vertical spacer
        • "__line__" — adds a horizontal separator line
        • any other string — creates a button with that text

    Args:
        parent (tk.Widget): The parent widget (e.g. `tk.Tk` or `tk.Frame`).
        buttons (list[tuple[str, Union[Callable, int, str, dict, None]]]):
            A list of tuples defining the UI structure.
            Each tuple consists of (text_or_special_tag, command_or_value).
        button_type (Type[ttk.Button] | Type[tk.Button], optional):
            The button class used to create button widgets.
            Defaults to `tk.Button`.
        **kwargs: Additional keyword arguments passed to each created button.
    """

    def __init__(
        self,
        parent,
        buttons: list[tuple[str, Union[Callable, int, str, None]]],
        button_type: Type[ttk.Button] | Type[tk.Button] = None,
        **kwargs
    ):
        super().__init__(parent)
        self.buttons = buttons
        self.button_type = button_type or tk.Button
        self.button_kwargs = kwargs

        # Special command mappings
        self.additional_commands = {
            "__space__": self._space,
            "__title__": self._title,
            "__line__": self._line,
        }

    # === Widget creation ===
    def _create_widget(self, text, command):
        """Creates a widget (button or special element) depending on the provided type."""
        if callable(command):
            return self.button_type(self, text=text, command=command, **self.button_kwargs)
        elif text in self.additional_commands:
            return self.additional_commands[text](command)
        else:
            print(f"[⚠️] Invalid command for '{text}': {command!r}")
            return self.button_type(self, text=text, state="disabled", **self.button_kwargs)

    # === Special elements ===
    def _space(self, height: int):
        """Adds vertical space between elements."""
        frame = tk.Frame(self, height=height)
        frame.pack_propagate(False)
        return frame

    def _title(self, text: str):
        """Creates a section title label."""
        return tk.Label(self, text=text, font=("Segoe UI", 12, "bold"))

    def _line(self, options: Union[int, dict, None] = None):
        """
        Adds a horizontal divider line.

        Args:
            options (int | dict | None):
                - int: Line thickness in pixels.
                - dict: Optional parameters {"height": int, "color": str}.
                - None: Uses default thin light-gray line.
        """
        if isinstance(options, int):
            height, color = options, "#d0d0d0"
        elif isinstance(options, dict):
            height = options.get("height", 1)
            color = options.get("color", "#d0d0d0")
        else:
            height, color = 1, "#d0d0d0"

        frame = tk.Frame(self, height=height, bg=color)
        frame.pack_propagate(False)
        return frame

    # === Layout ===
    def pack_buttons(self):
        """Creates and packs all widgets vertically inside the frame."""
        for text, command in self.buttons:
            widget = self._create_widget(text, command)
            if widget is None:
                continue

            if text == "__space__":
                widget.pack(fill=tk.X, pady=(widget["height"], 0))
            elif text == "__title__":
                widget.pack(fill=tk.X, pady=(10, 5))
            elif text == "__line__":
                widget.pack(fill=tk.X, pady=5)
            else:
                widget.pack(fill=tk.X, pady=2)

    def pack(self, *args, **kwargs):
        """Overrides pack() to automatically generate and pack the widgets."""
        super().pack(*args, **kwargs)
        self.pack_buttons()