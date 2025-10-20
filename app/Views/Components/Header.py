from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy

from app.Controllers.LanguageController import LanguageController


class Header(QFrame):

    def __init__(self):
        super().__init__()

        self.project_tittle = ''
        self.setProperty("qclass", "header_bg")
        self.setProperty("qround", "2")
        self.language_controller = LanguageController()
        current_language = self.language_controller.get_current_language()

        print(current_language)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignLeft)
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
        self.title_label.setFont(QFont("Nunito", 15))
        self.title_label.setProperty("qclass", "text-gray")
        self.tittle_bg_frame_layout.addWidget(self.title_label)


    def set_project_tittle(self, tittle: str):
        self.project_tittle = tittle

    def update_content(self):
        pass