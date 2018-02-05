#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import neighbors
from get_data import ImgData

import pickle
import numpy as np
from PIL import Image
import os

train = None

def get_guess(guess_obj_name="guess.bin", n_neighbors=15):
    file_list = os.listdir('./')

    if guess_obj_name in file_list:
        with open(guess_obj_name, "rb") as f:
            train = pickle.load(f)
    else:
        train = train_guess_obj()
        with open(guess_obj_name, "wb")as f:
            pickle.dump(train, f)
    return train


def train_guess_obj(n_neighbors=15):
    imgdata = ImgData()
    imgdata.get_all()
    lable, data = imgdata.label, imgdata.data

    nn = neighbors.KNeighborsClassifier(n_neighbors)
    nn.fit(data, lable)
    return nn

if __name__ == "__main__":
    nn = get_guess()
    img = Image.open("../trainData/num/0_1.png")
    img_array = np.array(img)
    img_array = np.where(img_array > 200, 1, 0)
    img_array_one_line = img_array.reshape((1, -1))[0]
    tar = nn.predict([img_array_one_line])
    print(tar)


