import threading

from buffer.CaptainHook import CaptainHook
from tracker_core.MicrophoneCore import MicrophoneCore
from app.Pyqt5Main import VitowoApp

class AppLauncher:

    def __init__(self,
                 buffer: CaptainHook = None
                 ):

        self.microphone_core = MicrophoneCore(buffer)

        self.start_thread(self.run_mediapipe)
        self.start_thread(self.run_mic_service)

        self.vitowo_app = VitowoApp(buffer)
        self.vitowo_app.run()
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