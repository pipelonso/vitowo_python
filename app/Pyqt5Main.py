from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame
import sys

from app.Controllers.LanguageController import LanguageController
from app.Controllers.SettingsController import SettingsController
from app.Views.Components.Header import Header
from app.themes.ThemeLoader import ThemeLoader
from buffer.CaptainHook import CaptainHook


class VitowoApp:

    def __init__(self,
                 buffer: CaptainHook = None,
                 launcher = None
                 ):

        self.launcher = launcher
        self.app = QApplication.instance() or QApplication(sys.argv)
        self.buffer = buffer

        self.language_controller = LanguageController()

        self.theme_loader = ThemeLoader()
        self.settings_controller = SettingsController()

        self.window = QWidget()
        self.window.setWindowTitle("Vitowo")
        self.window.resize(1000, 600)

        self.layout = QVBoxLayout(self.window)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.window.setLayout(self.layout)

        self.main_frame = QFrame()
        self.main_frame.setContentsMargins(1, 1, 1, 1)
        self.layout.addWidget(self.main_frame)
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(1, 1, 1, 1)
        self.main_frame.setLayout(self.main_layout)

        self.header = Header()
        self.main_layout.addWidget(self.header)
        self.main_layout.setAlignment(Qt.AlignTop)

        self.setup_start_process()

    def run(self):
        self.window.show()
        self.app.exec_()

    def setup_start_process(self):
        self.settings_controller.create_file_if_not_exists()
        theme = self.settings_controller.get_value("theme")
        theme_sheet = self.theme_loader.get_theme_structure(theme)
        self.app.setStyleSheet(theme_sheet)

        font_id = QFontDatabase.addApplicationFont("resources/fonts/nunito/static/Nunito-Regular.ttf")

        if font_id == -1:
            print("❌ Could not load default font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.app.setFont(QFont(font_family, 10))

        pass

    def check_mic(self):
        db = self.buffer.mic_db
        pass