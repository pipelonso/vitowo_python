from app.UrsinaMain import UrsinaMain
import threading
from tracker_core.MicrophoneCore import MicrophoneCore


class AppLauncher:

    def __init__(self):

        self.microphone_core = MicrophoneCore()

        self.start_thread(self.run_mediapipe)
        self.start_thread(self.run_mic_service)

        self.ursina_app = UrsinaMain()

        pass

    def launch(self):
        pass


    @staticmethod
    def start_thread(callback):
        thread = threading.Thread(target=callback)
        thread.start()

    def run_mediapipe(self):
        print('run mediapipe')
        pass

    def run_mic_service(self):
        self.microphone_core.start()
        pass