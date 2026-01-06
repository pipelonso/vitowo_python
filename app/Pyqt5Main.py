from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QHBoxLayout, QSplitter, QSizePolicy
import sys

from app.Controllers.LanguageController import LanguageController
from app.Controllers.SettingsController import SettingsController
from app.Views.Components.Header import Header
from app.Views.Components.Vitowo2dCompositor import Vitowo2dCompositor
from app.Views.Components.Vitowo2dViewport import Vitowo2dViewport
from app.Views.Components.VitowoViewport import VitowoViewport
from app.themes.ThemeLoader import ThemeLoader
from buffer.CaptainHook import CaptainHook
from app.Views.Components.CameraSource import CameraSource
from tracker_core.opencv.CameraSource import CameraSource as BackendCameraSource


class VitowoApp:

    def __init__(self,
                 buffer: CaptainHook = None,
                 launcher = None
                 ):

        self.backend_camera_source = BackendCameraSource()

        self.camera_devices = self.backend_camera_source.list_devices()

        self.launcher = launcher
        self.app = QApplication.instance() or QApplication(sys.argv)
        self.buffer = buffer

        self.language_controller = LanguageController()
        self.current_language = self.language_controller.get_current_language()

        if self.current_language not in self.language_controller.get_language_list():
            raise Exception("Language configuration failed to load, not found language: " + self.current_language)

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
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.workspace_general_frame_layout = QHBoxLayout()
        self.main_layout.addLayout(self.workspace_general_frame_layout)

        self.workspace_splitter = QSplitter()
        self.workspace_splitter.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.workspace_general_frame_layout.addWidget(self.workspace_splitter)

        left_workspace_frame = QFrame()
        self.left_workspace_frame_layout = QVBoxLayout()
        self.left_workspace_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        left_workspace_frame.setLayout(self.left_workspace_frame_layout)
        left_workspace_frame.setProperty("qclass", "header_bg")
        left_workspace_frame.setProperty("qround", "2")
        self.workspace_splitter.addWidget(left_workspace_frame)

        self.base_camera_source = CameraSource()
        self.left_workspace_frame_layout.addWidget(self.base_camera_source)

        middle_workspace_frame = QFrame()
        self.middle_workspace_frame_layout = QVBoxLayout()
        self.middle_workspace_frame_layout.setContentsMargins(2, 2, 2, 2)
        self.middle_workspace_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        middle_workspace_frame.setLayout(self.middle_workspace_frame_layout)
        middle_workspace_frame.setProperty("qround", "2")
        middle_workspace_frame.setProperty("qclass", "header_bg")
        self.workspace_splitter.addWidget(middle_workspace_frame)

        right_workspace_frame = QFrame()
        self.right_workspace_frame_layout = QVBoxLayout()
        self.right_workspace_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        right_workspace_frame.setLayout(self.right_workspace_frame_layout)
        right_workspace_frame.setProperty("qround", "2")
        right_workspace_frame.setProperty("qclass", "header_bg")
        self.workspace_splitter.addWidget(right_workspace_frame)

        self.middle_splitter = QSplitter(Qt.Orientation.Vertical)
        self.middle_workspace_frame_layout.addWidget(self.middle_splitter)

        self.vitowo_compositor = Vitowo2dCompositor()


        self.middle_splitter.addWidget(self.vitowo_compositor)

        self.timeline_frame = QFrame()
        self.timeline_frame.setProperty("qround", "2")
        self.timeline_frame.setProperty("qclass", "header_bg")
        self.timeline_frame_layout = QVBoxLayout()
        self.timeline_frame.setLayout(self.timeline_frame_layout)

        self.middle_splitter.addWidget(self.timeline_frame)

        self.setup_start_process()
        self.base_camera_source.start_video()

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
        print(db)
        pass