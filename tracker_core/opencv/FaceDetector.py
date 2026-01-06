import cv2
import mediapipe as mp
import math

class FaceDetector:
    def __init__(self, min_detection_con=0.5, min_tracking_con=0.5):
        self.min_detection_con = min_detection_con
        self.min_tracking_con = min_tracking_con

        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=self.min_detection_con,
            min_tracking_confidence=self.min_tracking_con
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.draw_spec = self.mp_draw.DrawingSpec(thickness=1, circle_radius=1)
        self.results = None

    def process_frame(self, img, draw=True):
        """
        Processes the image to detect face mesh.
        :param img: Image to process (BGR)
        :param draw: Whether to draw landmarks on the image
        :return: Processed image
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.face_mesh.process(img_rgb)

        if self.results.multi_face_landmarks:
            for face_lms in self.results.multi_face_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        image=img,
                        landmark_list=face_lms,
                        connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=self.draw_spec,
                        connection_drawing_spec=self.draw_spec
                    )
        return img

    def get_position(self, img, draw=True):
        """
        Get the bounding box of the face.
        :param img: Image for dimensions
        :param draw: Whether to draw the bounding box
        :return: (x, y, w, h) bounding box or None
        """
        if self.results and self.results.multi_face_landmarks:
            face_lms = self.results.multi_face_landmarks[0]
            h, w, c = img.shape
            x_list = [lm.x for lm in face_lms.landmark]
            y_list = [lm.y for lm in face_lms.landmark]
            
            x_min, x_max = min(x_list), max(x_list)
            y_min, y_max = min(y_list), max(y_list)
            
            bbox = int(x_min * w), int(y_min * h), int((x_max - x_min) * w), int((y_max - y_min) * h)
            
            if draw:
                cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 2)
            
            return bbox
        return None

    def get_expressions(self):
        """
        Get facial expressions/landmarks.
        Currently returns the raw landmarks list.
        :return: List of landmarks or None
        """
        if self.results and self.results.multi_face_landmarks:
            return self.results.multi_face_landmarks[0]
        return None
