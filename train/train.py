#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./")
from sklearn import neighbors
from img.train.get_data import ImgData
import traceback
import pickle
import numpy as np
import os

train = None


def get_guess(guess_obj_name="guess.bin", n_neighbors=15):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    guess_obj_name = "{}{}{}".format(project_dir, os.path.sep, guess_obj_name)
    try:
        with open(guess_obj_name, "rb") as f:
            train = pickle.load(f)
    except:
        print(project_dir, "dddd")
        print(guess_obj_name)
        # train = train_guess_obj()
        #with open(guess_obj_name, "wb")as f:
            # pickle.dump(train, f)
    return train


def train_guess_obj(n_neighbors=15):
    imgdata = ImgData()
    imgdata.get_all()
    lable, data = imgdata.label, imgdata.data

    nn = neighbors.KNeighborsClassifier(n_neighbors)
    nn.fit(data, lable)
    return nn


def guess(img):
    try:
        img = img.resize((20, 20))
        img_array = np.array(img)
        img_array = np.where(img_array > 200, 1, 0)
        img_array_one_line = img_array.reshape((1, -1))[0]
        nn = get_guess()
        guess_num = nn.predict([list(img_array_one_line)])
        return list(guess_num), ""
    except:
        error = traceback.format_exc()
        return "", error

if __name__ == "__main__":
    from PIL import Image
    nn = get_guess()
    # img = Image.open("../trainData/num/0_1.png")
    # img_array = np.array(img)
    # img_array = np.where(img_array > 200, 1, 0)
    # img_array_one_line = img_array.reshape((1, -1))[0]
    # tar = nn.predict([img_array_one_line])
    # print(tar)
