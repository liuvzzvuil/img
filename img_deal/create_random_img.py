#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw


def rndtxt(only='chr'):
    txt_list = []
    if only == "chr":
        # 大写字母
        txt_list.extend([i for i in range(65, 90)])
        # 小写字母
        txt_list.extend([i for i in range(97, 123)])
    else:
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
    font = ImageFont.truetype('../fontType/msyh.TTF', 36)
    draw = ImageDraw.Draw(image)

    # 填充背景颜色
    for x in range(weight):
        for y in range(hight):
            draw.point((x, y))
    # 生成随机验证码
    for t in range(4):
        draw.text((60 * t + 10, 10), rndtxt(), font=font, fill=rndtxtcolor2())

    image.show()
    # image.save('test.jpg')
from img_deal.split_img import spilt_img
import random
def create_sig_img(text):
    txt_list = []
    txt_list.extend([i for i in range(65, 90)])
    # 小写字母
    txt_list.extend([i for i in range(97, 123)])
    # 数字
    # txt_list.extend([i for i in range(48, 57)])
    weigh_back = 60
    hight_back = 60
    weigh_txt = 60
    hight_txt = 60
    # 直接使用 L模式, 降低空间占用
    # img = Image.new('RGBA', (weigh_back, hight_back), (255, 255, 255))
    # txt = Image.new('RGBA', (weigh_txt, hight_txt), (255, 255, 255))
    img = Image.new('L', (weigh_back, hight_back), 255)
    txt = Image.new('L', (weigh_txt, hight_txt), 255)
    font = ImageFont.truetype('../fontTYpe/msyh.TTF', 40)
    draw = ImageDraw.Draw(txt)

    # draw.text((5, 5), text, font=font, fill=(125, 125, 125), align='center')
    draw.text((5, 5), text, font=font, fill=125, align='center')
    rotate_angle = 80
    rotate_num = random.randint(-rotate_angle, rotate_angle)
    txt = txt.rotate(rotate_num, Image.BICUBIC)

    return Image.composite(txt, img, txt)


if __name__ == "__main__":
    txt_list = []
    # txt_list.extend([chr(i) for i in range(65, 91)])
    # 小写字母
    # txt_list.extend([chr(i) for i in range(97, 123)])
    txt_list.extend([chr(i) for i in range(48, 58)])
    # for i in txt_list:
    #     print(i)
    # txt_list.append(chr(57))
    split_num = 1
    for txt in txt_list:
        for i in range(200):
            img = create_sig_img(txt)
            img_list, error = spilt_img(img, split_num)
            if not error:
                img = img_list[0]
                img.resize((20, 20)).save("trainData/num/{}_{}.png".format(txt, i))
            else:
                print(error)
