import cv2
from detection import faceLandmarkDetection
import utils

img = cv2.imread('testPhotos/celebs/selena.jpg', cv2.IMREAD_COLOR)
landmarks = faceLandmarkDetection.getLandmarks(img)

utils.markCirclesInline(img, landmarks)

utils.exportPoints(landmarks, "points.txt")

img = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
utils.showImage(img, 'features')
