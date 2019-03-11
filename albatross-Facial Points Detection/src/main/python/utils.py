import cv2


def showImage(img, name='image'):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def markCirclesInline(img, mat):
    i = 1
    print("Drawing " + str(len(mat)) + " circles in image " + str(img))
    for val in mat:
        org = (val.item(0), val.item(1))
        cv2.circle(img, org, 5, (255, 255, 255), 1)
        cv2.putText(img, str(i), org, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255), 1)
        i = i + 1


def exportPoints(mat, fileName):
    with open(fileName, "w") as file:
        cc = 1
        for val in mat:
            file.write(str(val.item(0)) + " " + str(val.item(1)) + "\n")
            cc += 1
