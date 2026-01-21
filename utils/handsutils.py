# utils/handsutils.py

# Imports
import math
import cv2
import numpy as np
import mediapipe as mp
from . import faceutils
from . import face_detection
from . import fingerutils
from . import zoomutils
import time
last_zoom_time = 0
last_video_toggle = 0
last_dist = None

# Set all status to false
video_status = False
blur_status = False
detect_face_status = False

# Set default Zoom Factor
zoom_factor = 1

# Initialization of mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
"""MediaPipe Hands() """


def mediapipe_gestures(img, cropped_img):
    """
    Args:
        img: current frame
        cropped_img: cropped image for hands detection

    Returns:
        frame with applied effects
    """
    # Crop the image for area specific detection
    cropped_img_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
    # Fetch the results on cropped image
    results = hands.process(cropped_img_rgb)

    # Set global variable values
    global video_status
    global zoom_factor
    global blur_status
    global detect_face_status
    global last_video_toggle
    global last_dist

    # Detect faces
    detect_face = face_detection.face_detect(img)
    if detect_face is None or detect_face != 1:
        detect_face_status = True
    if detect_face == 1:
        detect_face_status = False
    # Create frame with a black img
    stopped_img = np.zeros([100, 100, 3], dtype=np.uint8)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            zoom_arr = []  # coordinates of points on index finger and thumb top
            h, w, c = img.shape
            landmarks = handLms.landmark
            for lm_id, lm in enumerate(landmarks):
                # Convert landmark coordinates to actual image coordinates
                cx, cy = int(lm.x * w), int(lm.y * h)

                # Append the coordinates
                if lm_id == 4 or lm_id == 8:
                    zoom_arr.append((cx, cy))

            
            now = time.time()

            if now - last_video_toggle > 0.8:   # 0.8 sec lock (ANTI FLICKER)
                if fingerutils.is_fist_closed(landmarks):
                    video_status = True     # VIDEO OFF (black)
                    last_video_toggle = now
                else:
                    video_status = False    # VIDEO ON
                    last_video_toggle = now


            # Check if three signal is given
            if fingerutils.three_signal(landmarks):
                blur_status = True

            # Check if two signal is given
            if fingerutils.two_signal(landmarks):
                blur_status = False
            # Check if hand is up and continue the capture
            if fingerutils.two_signal(landmarks) or fingerutils.three_signal(landmarks):
                last_dist = None
                continue

            # Check if fingers are detected fists are closed and hand is up so video is on
            if len(zoom_arr) > 1 and fingerutils.hand_up(landmarks):
                p1, p2 = zoom_arr
                dist = math.hypot(p1[0] - p2[0], p1[1] - p2[1])
                # Zoom in or out
                if 50 <= dist <= 350:
                    if last_dist is None:
                        last_dist = dist
                    else:

                        dist_delta = dist - last_dist
                    
                        if abs(dist_delta) > 4:
                            ZOOM_STEP = 0.025
                            if dist_delta > 0:
                                zoom_factor += ZOOM_STEP   # fingers apart → zoom in
                            else:
                                zoom_factor -= ZOOM_STEP 
                            zoom_factor = max(1.0, min(zoom_factor, 2.0))
                        last_dist = dist
            else:
                # pinch released → reset
                last_dist = None      
    # If the hand was down or there is more than one person in frame
    if video_status is True :
        img = stopped_img

    # If blur is on blur the image
    if blur_status:
        img = faceutils.background_blur(img)

    # Zoom the image according to the needs
    img = zoomutils.zoom_center(img, zoom_factor)

    return img
