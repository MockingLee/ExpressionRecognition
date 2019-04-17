from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import Adadelta
from keras.utils import np_utils
from keras.regularizers import l2 #, activity_l2
import keras
from dataset import getData
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
import numpy
from dataset import getTest

model = keras.models.load_model(filepath="./Model.275-0.3455.hdf5")

X , y = getTest()

X = X.reshape(X.shape[0] , 48 , 48 ,1)
print(X.shape)
print(y.shape)
y = np_utils.to_categorical(y, 7)
score = model.evaluate(X , y)
print(score)