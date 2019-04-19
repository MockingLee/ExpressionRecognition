import cv2
import keras
import numpy as np
pic = cv2.imread("./40CC25C74C506A4522CDB4610794A6BC.jpg")

pic = cv2.resize(pic, (48,48))

gray = np.array(cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY))

model = keras.models.load_model(filepath="./Model.299-0.6065.hdf5")

X = gray

X = X.reshape(1,48 , 48 ,1)
print(X.shape)

score = model.predict(X)
print(np.argmax(score))

"""
0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral
"""