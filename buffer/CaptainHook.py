class CaptainHook:

    def __init__(self):
        self.mic_db = 0

    def set_mic_db(self, value: float):
        self.mic_db = value

    def get_mic_db(self):
        return self.mic_db

