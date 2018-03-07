#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np


# 对数据进行处理, 只保留0, 1
def surround_line_in_num(img: np.array):
    col_index = []
    row_index = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] == 0:
                col_index.append(i)
                row_index.append(j)
    return col_index, row_index
# surround_line_in_num(xxx)


# TODO: 增加处理, 当像素周围只有2x2时, 认为它是噪音, 这一步应该在统计出连续值之后做, 只对有疑问的点进行计算, 大面积连续的值不考虑该问题
def remove_noise(img):
    return img


# 获取一个数组中连续的值的索引
def search(lis, broke_num=3):
    lis = list(set(lis))
    lis.sort()
    s_list = [lis[0]-1] + lis
    e_list = lis + [float('inf')]
    se = list(map(lambda x: x[1] - x[0], zip(s_list, e_list)))
    # 将坐标装入队列
    ss = []
    k = 0
    s = 0
    e = 0
    for i in range(len(se)):
        if se[i] == 1:
            if e < i:
                e = i
        else:
            if e != 0:
                # 直接转换至e_list坐标, 获取图片内部坐标
                ss.append((e_list[s], e_list[e]))
            k += 1
            s, e = i, 0

    if len(ss) == broke_num:
        return ss, ""
    elif len(ss) > broke_num:
        return ss[:broke_num], "有多余的长度列表 为: {}".format(ss)
    else:
        return ss, "解析失败!!! 没有获取到期望的分割点!!"


def save_splited_img(split_list, img):
    img_list = []
    for i in split_list:
        temp = img.crop(i)
        img_list.append(temp)
    return img_list


def split(img, split_num=4):
    """

    :param img: 图像对象
    :type img: Image
    :param split_num: 图片中的字符个数
    :type split_num: int
    :return: split point list
    :rtype: list(tuple(left: int, up: int, right: int, down: int)), Error
    """
    # 将传入的img对象处理为灰度图像, 并且只保留0, 1
    limg = img.convert("L")
    limg_array = np.array(limg)
    # 大于200 是因为有的颜色太浅了, 比如: 浅黄色
    array_zero_one = np.where(limg_array > 200, 1, 0)
    # np.savetxt('num.txt', array_zero_one, fmt="%d")
    _, row_indx = surround_line_in_num(array_zero_one)
    split_list, error = search(row_indx, split_num)
    left_up_right_down_tuple_list = []
    if not error:
        col_split_num = 2
        # save_splited_img(split_list, img_array=limg_array)
        for i in split_list:
            temp_array = array_zero_one[:, i[0]:i[1]]
            col_index, _ = surround_line_in_num(temp_array)
            col_split_list, error = search(col_index, col_split_num)
            l, r = i
            u, d = col_split_list[0]
            left_up_right_down_tuple_list.append((l, u, r, d))
        return left_up_right_down_tuple_list, None
    else:
        print(error)
        return None, "计算失败!!"

def spilt_img(img, split_num=1):
    img = img.convert("L")
    img_array = np.array(img)
    lurd_list, error = split(img, split_num)
    if not error:
        bimg_array = np.where(img_array > 200, 255, 0)
        # try:
        #     bimg = Image.fromarray(bimg_array)  # pillow == 4.3.0 需要指定模式才行, 但是指定的模式基本上都不能正常展示...
        #     # 最接近的模式是  "I"
        # except:
        bimg = img
        return save_splited_img(lurd_list, bimg), ""
    else:
        print(error)
        return "", error

if __name__ == "__main__":
    # img = Image.open('result.jpg')
    img = Image.open('show.png')

    # 直接将图片置为灰度模式, 以便于 Image.fromarray 获取
    img = img.convert("L")
    img_array = np.array(img)
    lurd_list, error = split(img, 1)
    if not error:
        bimg_array = np.where(img_array > 200, 255, 0)
        try:
            bimg = Image.fromarray(bimg_array) # pillow == 4.3.0 需要指定模式才行, 但是指定的模式基本上都不能正常展示...
            # 最接近的模式是  "I"
        except:
            bimg = img
        save_splited_img(lurd_list, bimg)
    else:
        print(error)