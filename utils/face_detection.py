# utils/face_detection.py
import cv2
import mediapipe as mp
def face_detect(image):
    """
    Args:
        image: frame captured by camera

    Returns:
        The number of faces
    """
    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(
            model_selection=0, min_detection_confidence=0.5) as face_detection:
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)
        if results.detections:
            return len(results.detections)
