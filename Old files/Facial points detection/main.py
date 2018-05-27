import cv2
import faceFeatureDetection
import basicFunctions

img= cv2.imread('testPhotos/celebs/selena.jpg',cv2.IMREAD_COLOR)
mat=faceFeatureDetection.get_landmarks(img)
basicFunctions.drawCircles(img,mat)
basicFunctions.exportPoints(mat)
img=cv2.resize(img,None,fx=0.8,fy=0.8,interpolation=cv2.INTER_CUBIC)
basicFunctions.showImage(img,'features')
