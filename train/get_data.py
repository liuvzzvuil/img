#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import os
import sys
import numpy as np
import traceback

class ImgData:
    def __init__(self):
        self.data = None
        self.label = None

    def get_data(self, file_name):
        try:
            img = Image.open(file_name)
            img_array = np.array(img)
            img_array = np.where(img_array > 200, 1, 0)
            img_array_one_line = img_array.reshape((1, -1))[0]
            return list(img_array_one_line), None
        except:
            error = traceback.format_exc()
            return None, error

    def get_all(self):
        data_path = "../trainData/num"
        file_list = os.listdir(data_path)
        self.data = []
        self.label = []
        for file_name in file_list:
            self.label.append(file_name.split("_")[0])
            data, error = self.get_data(data_path+'/'+file_name)
            if not error:
                self.data.append(data)
            else:
                print(error)
                raise Exception

if __name__ == "__main__":
    imgData = ImgData()
    imgData.get_all()
