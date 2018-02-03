#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
import random


def rndtxt():
    txt_list = []
    # 大写字母
    txt_list.extend([i for i in range(65, 90)])
    # 小写字母
    txt_list.extend([i for i in range(97, 123)])
    # 数字
    txt_list.extend([i for i in range(48, 57)])
    return chr(random.choice(txt_list))


# def rndbgcolor():
#     # 背景颜色
#     # return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#     pass

def rndtxtcolor2():
    # 字体颜色
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def code():
    weight = 240
    hight = 60
    image = Image.new('RGB', (weight, hight), (255, 255, 255))
    font = ImageFont.truetype('msyh.ttc', 36)
    draw = ImageDraw.Draw(image)

    # 填充背景颜色
    for x in range(weight):
        for y in range(hight):
            # draw.point((x, y), fill=rndbgcolor())
            draw.point((x, y))
    # 生成随机验证码
    for t in range(4):
        draw.text((60 * t + 10, 10), rndtxt(), font=font, fill=rndtxtcolor2())

    image.show()
    image.save('test.jpg')


code()
