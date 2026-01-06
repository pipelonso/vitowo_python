from PySide6.QtGui import QPixmap, QColor, QIcon, Qt, QPainter
from PySide6.QtWidgets import QPushButton

from app.Controllers.SettingsController import SettingsController
from launch import Loader

def tint_pixmap(pixmap: QPixmap, color: QColor) -> QPixmap:
    """Aplica un tinte de color a un pixmap."""
    tinted = QPixmap(pixmap.size())
    tinted.fill(Qt.GlobalColor.transparent)

    painter = QPainter(tinted)
    painter.drawPixmap(0, 0, pixmap)
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(tinted.rect(), color)
    painter.end()

    return tinted


def render_icon_buttons(icon_path: str = None, button: QPushButton = None):

    theme = SettingsController().get_value("theme")

    icon_buttons = Loader.icon_list_buttons

    if icon_buttons is not None and button is not None:
        icon_buttons = [(icon_path, button)]

    for path_str, but in icon_buttons:
        if not isinstance(but, QPushButton) or not isinstance(path_str, str):
            continue

        pixmap = QPixmap(path_str)

        theme_colors = but.property("theme_colors")
        if theme_colors and isinstance(theme_colors, (tuple, list)) and len(theme_colors) == 2:
            color_hex = theme_colors[1] if theme == 'dark' else theme_colors[0]
            color = QColor(color_hex)
            pixmap = tint_pixmap(pixmap, color)

        but.setIcon(QIcon(pixmap))


def register_icon_button(icon_path: str, button: QPushButton):
    Loader.icon_list_buttons.append((icon_path, button))