import pandas as pd
import numpy as np
"""
0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral
"""



def getTrainData():
    """
    :return: x and y dataset
    """
    data = pd.read_csv("./data/fer2013.csv")
    #data = data[0:5000]
    data = data.loc[data.Usage == "Training"]
    print(data)
    dataset_x = data.loc[:, "pixels"].str.split(" ").values.tolist()
    dataset_y = data.loc[:, "emotion"].values.tolist()
    return  np.array(dataset_x).astype(int) , np.array(dataset_y).astype(int)

def getTest():
    data = pd.read_csv("./data/fer2013.csv")
    data = data.loc[data.Usage != "Training"]
    dataset_x = data.loc[:, "pixels"].str.split(" ").values.tolist()
    dataset_y = data.loc[:, "emotion"].values.tolist()
    return np.array(dataset_x).astype(int), np.array(dataset_y).astype(int)

