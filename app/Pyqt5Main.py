from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

from buffer.CaptainHook import CaptainHook


class VitowoApp:
    def __init__(self,
                 buffer: CaptainHook = None
                 ):

        self.app = QApplication.instance() or QApplication(sys.argv)
        self.buffer = buffer

        self.window = QWidget()
        self.window.setWindowTitle("Vitowo")
        self.window.resize(600, 400)

        self.layout = QVBoxLayout(self.window)
        self.window.setLayout(self.layout)

        self.mic_val_label = QLabel()
        self.mic_val_label.setText('---')

        self.layout.addWidget(self.mic_val_label)

        self.check_mic_button = QPushButton()
        self.check_mic_button.setText("Check mic")
        self.check_mic_button.clicked.connect(self.check_mic)

        self.layout.addWidget(self.check_mic_button)


    def run(self):
        self.window.show()
        self.app.exec_()

    def check_mic(self):
        db = self.buffer.mic_db
        self.mic_val_label.setText(str(db))
        pass