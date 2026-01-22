# utils/faceutils.py

import cv2
import numpy as np
import mediapipe as mp;

def background_blur(image):
    """
    Args:
        image: frame captured by camera

    Returns:
        The image with a blurred background
    """
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    with mp_selfie_segmentation.SelfieSegmentation(
            model_selection=1) as selfie_segmentation:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = selfie_segmentation.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mask = cv2.ximgproc.jointBilateralFilter(np.uint8(results.segmentation_mask),
                                                 image,
                                                 15, 5, 5)
        condition = np.stack(
            (results.segmentation_mask,) * 3, axis=-1) > 0.1

        output_image = np.where(condition, image, mask)

    return output_image
