import cv2
import keras
import numpy as np


def getPrediction(model , path):
    print(path)
    pic = cv2.imread(path)
    pic = cv2.resize(pic, (48, 48))
    gray = np.array(cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY))
    X = gray
    X = X.reshape(1, 48, 48, 1)
    print(X.shape)
    score = model.predict(X)
    li = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
    return li[np.argmax(score)]


"""
0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral
"""

# if __name__ == '__main__':
#     model = keras.models.load_model(
#         filepath="model_file/Model.299-0.6065.hdf5")
#
#     print(getPrediction(model ,r"C:\Users\18140\Documents\GitHub\ExpressionRecognition\WebService\fileDir\1555753532.5165482_angry.jpg"))