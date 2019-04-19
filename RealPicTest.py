import cv2
import keras
pic = cv2.imread("./happy.jpg")
pic = cv2.resize(pic , (48,48))

gray = cv2.