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
        #res.append(cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2))


    # cv2.imshow("Faces found", image)
    # cv2.waitKey(0)
    return np.array(res)

# if __name__ == '__main__':
#     face = getFace("TestPic/fear.jpg" , "haarcascade_frontalface_default.xml")
#     print(face[0].shape)
#     print(cv2.imshow("face" , face[0]))
#     cv2.waitKey(0)



