import sounddevice as sd
import numpy as np
import time

from buffer.CaptainHook import CaptainHook

class MicrophoneCore:

    def __init__(self,
                 app_buffer: CaptainHook | None = None
                 ):

        self.app_buffer = app_buffer
        self.running = False

        pass

    def start(self):

        self.running = True

        duration = 0.1
        while self.running:
            audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='float32')
            sd.wait()
            rms = np.sqrt(np.mean(np.square(audio)))
            db = 20 * np.log10(rms + 1e-6)
            self.app_buffer.set_mic_db(db)
            time.sleep(0.05)
            print(db)

    def stop(self):
        self.running = False