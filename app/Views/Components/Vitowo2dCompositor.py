from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton, QSizePolicy
from PySide6.QtWidgets import QFrame

from app.Views.Components.Vitowo2dViewport import Vitowo2dViewport
from app.Helpers import IconThemeLoader
from launch import Loader


class Vitowo2dCompositor(QFrame):

    def __init__(self):
        super().__init__()
        self.setProperty('qround', "2")
        self.setProperty('qclass', "BG_1")
        self.setContentsMargins(1, 1, 1, 1)
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.viewport_2d : Vitowo2dViewport = Vitowo2dViewport()
        self.viewport_2d.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.viewport_2d.setProperty('qround', "2")
        paths = self.viewport_2d.svg_parser.svg_to_q_painter_paths("./Presets/svg/R.svg")
        self.viewport_2d.add_path_item(paths)

        tools_frame = QFrame()
        tools_frame.setProperty('qround', "2")
        tools_frame.setProperty('qclass', "BG_1")
        tools_frame.setContentsMargins(1, 1, 1, 1)
        tools_frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.tools_frame_layout = QVBoxLayout()
        self.tools_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        tools_frame.setLayout(self.tools_frame_layout)

        self.tools_scroll = QScrollArea()
        self.tools_scroll.setContentsMargins(0, 0, 0, 0)
        self.tools_scroll.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.tools_scroll.setWidgetResizable(True)
        self.tools_scroll.setWidget(tools_frame)

        self.layout.addWidget(self.tools_scroll)
        self.layout.addWidget(self.viewport_2d)

        add_button = QPushButton()
        add_button.setProperty('theme_colors', ("#000733", "#EBEDFF"))
        add_button.setMinimumWidth(30)
        add_button.setMinimumHeight(30)
        add_button.setMaximumHeight(30)
        self.tools_frame_layout.addWidget(add_button)
        IconThemeLoader.register_icon_button(
            "resources/icons/svg/plus-circle.svg" ,
            add_button
        )

        add_button = QPushButton()
        add_button.setProperty('theme_colors', ("#000733", "#EBEDFF"))
        add_button.setMinimumWidth(30)
        add_button.setMinimumHeight(30)
        add_button.setMaximumHeight(30)
        self.tools_frame_layout.addWidget(add_button)
        IconThemeLoader.register_icon_button(
            "resources/icons/svg/cursor-fill.svg",
            add_button
        )

        IconThemeLoader.render_icon_buttons()
