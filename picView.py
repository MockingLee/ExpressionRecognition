import cv2
from keras.utils import np_utils

import dataset
import numpy as np
import keras
img , label = dataset.getTest()
img = img[10]
label = label[10]
img = np.array(img).astype(int).reshape((48,48))
cv2.imwrite('new.jpg',img)

model = keras.models.load_model(filepath="./Model.299-0.6065.hdf5")
img = img.reshape(1, 48 , 48 ,1)
label = np_utils.to_categorical(label, 7)
score = model.predict(img)
print(score)