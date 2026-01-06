from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap
import cv2
from tracker_core.opencv.CameraSource import CameraSource as BackendCameraSource

class CameraSource(QFrame):

    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.devices = []

        self.image_renderer = QLabel()
        self.image_renderer.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_renderer)
        
        self.text_status = QLabel()
        self.text_status.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.text_status)

        self.camera : BackendCameraSource | None = None
                
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def set_devices(self, devices: list[str]):
        self.devices = devices

    def start_video(self, device_index : int = 0):

        if len(self.devices) == 0:
            self.text_status.setText("No devices found")
            return
        self.camera = BackendCameraSource(device_index)

        if self.camera.start():
            self.timer.start(30) # ~30 FPS
        else:
            print("Failed to open camera")

    def stop_video(self):
        self.timer.stop()
        self.camera.stop()

    def update_frame(self):
        ret, frame = self.camera.get_frame()
        if ret:            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            
            self.image_renderer.setPixmap(QPixmap.fromImage(q_img))

