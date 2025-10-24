from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QPushButton

from app.Controllers.LanguageController import LanguageController


class Header(QFrame):

    def __init__(self):
        super().__init__()

        self.project_tittle = ''
        self.setProperty("qclass", "header_bg")
        self.setProperty("qround", "2")
        self.language_controller = LanguageController()
        self.current_language = self.language_controller.get_current_language()

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setContentsMargins(2, 2, 2, 2)
        self.setLayout(self.layout)
        self.setContentsMargins(2, 2, 2, 2)

        self.tittle_bg_frame = QFrame()
        self.tittle_bg_frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.tittle_bg_frame.setProperty("qclass", "tittle_bg")
        self.tittle_bg_frame.setProperty("qround", "2")
        self.tittle_bg_frame_layout = QVBoxLayout()
        self.tittle_bg_frame.setLayout(self.tittle_bg_frame_layout)

        self.layout.addWidget(self.tittle_bg_frame)

        self.title_label = QLabel("VITOWO")
        self.title_label.setFont(QFont("Nunito", 13))
        self.title_label.setProperty("qclass", "text-gray")
        self.tittle_bg_frame_layout.addWidget(self.title_label)

        self.view_button = QPushButton()
        self.view_button.setProperty("qclass", "just_text")
        self.view_button.setText(
            self.language_controller.translate(self.current_language, 'header.view_button')
        )
        self.layout.addWidget(self.view_button)

        self.settings_button = QPushButton()
        self.settings_button.setProperty("qclass", "just_text")
        self.settings_button.setText(
            self.language_controller.translate(self.current_language, 'header.settings_button')
        )
        self.layout.addWidget(self.settings_button)

    def set_project_tittle(self, tittle: str):
        self.project_tittle = tittle

    def update_content(self):
        pass