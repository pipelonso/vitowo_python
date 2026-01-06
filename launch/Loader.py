from typing import Tuple

from PySide6.QtWidgets import QPushButton

from buffer.CaptainHook import CaptainHook

app_buffer : CaptainHook | None = None

icon_list_buttons: list[Tuple[str, QPushButton]] = []