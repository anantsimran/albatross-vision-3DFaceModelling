import dlib
import numpy as np


predictorPath= 'resources/shapePredictor.dat'

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictorPath)

def get_landmarks(im): #makeSure that there is only one face in the image
    rects = detector(im, 1)
    return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])
