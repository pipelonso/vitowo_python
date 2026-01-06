import cv2

class CameraSource:
    def __init__(self, device_index=0):
        self.device_index = device_index
        self.cap = None

    @staticmethod
    def list_devices(max_check=10):
        """
        Scans for available camera devices.
        :param max_check: Maximum number of indices to check.
        :return: List of available camera indices.
        """

        available_devices = []
        for i in range(max_check):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available_devices.append(i)
                cap.release()
        return available_devices

    def set_device_index(self, index):
        self.device_index = index

    def start(self):
        """
        Opens the camera.
        :return: True if successful, False otherwise.
        """
        self.cap = cv2.VideoCapture(self.device_index)
        return self.cap.isOpened()

    def stop(self):
        """
        Releases the camera.
        """
        if self.cap:
            self.cap.release()
            self.cap = None

    def get_frame(self):
        """
        Reads a frame from the camera.
        :return: (success, frame)
        """
        if self.cap and self.cap.isOpened():
            return self.cap.read()
        return False, None

    def is_opened(self):
        """
        Checks if the camera is currently open.
        :return: True if open, False otherwise.
        """
        return self.cap is not None and self.cap.isOpened()
