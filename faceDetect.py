import cv2
import numpy as np

def getFace(path,xml_path):
    faceCascade = cv2.CascadeClassifier(xml_path)
    image = cv2.imread(path)
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    res = []
    for (x, y, w, h) in faces:
        res.append(image[y:y+h, x:x+w])
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2) #6

    cv2.imwrite("")

    return np.array(res)

if __name__ == '__main__':
    getFace("TestPic/Surprise.jpg" , "haarcascade_frontalface_default.xml")




