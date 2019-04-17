import cv2
import dataset
import numpy as np
img = dataset.dataset_x[0]
img = np.array(img).astype(int).reshape((48,48))
cv2.imwrite('test.png',img)

