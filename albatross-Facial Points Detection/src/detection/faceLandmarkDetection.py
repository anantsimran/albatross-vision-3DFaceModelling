import dlib
import numpy as np
import config

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(config.PREDICTOR_DAT_PATH)


def getLandmarks(im):
    """
    Currently only detects face from the first face it detects
    :param im: Image that contains the face
    :return:
    """
    faces = detector(im, 1)
    return np.matrix([[p.x, p.y] for p in predictor(im, faces[0]).parts()])
