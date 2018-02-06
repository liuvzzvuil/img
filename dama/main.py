#!/usr/bin/env python
# -*- coding: utf-8 -*-

from img.dama.img_type import IMAGE_TYPE
from img.img_deal.split_img import spilt_img
from img.train import train


class Dama:
    def __init__(self):
        pass

    def guess(self, img, img_type):
        guess_ = train.guess
        if img_type in IMAGE_TYPE:
            lii, error = spilt_img(img, IMAGE_TYPE[img_type])
            if not error:
                result_list = list(map(guess_, lii))
                result = []
                for i in result_list:
                    if not i[1]:
                        result.extend(i[0])
                    else:
                        return "", i[1]
            else:
                return "", error
            return result, ""

if __name__ == "__main__":
    from PIL import Image
    dama = Dama()
    img = Image.open("result.jpg")
    print(dama.guess(img, 'num_4'))
