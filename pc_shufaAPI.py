#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 利用既有网站，文字转换成书法图片

from bs4 import BeautifulSoup
from PIL import Image
import requests
from io import BytesIO

if __name__ == "__main__":
    url = "http://www.diyiziti.com/"
    contect = "白日依山尽，黄河入海流。"
    datas = {
        "FontInfoId": 90,
        "FontSize": 42,
        "FontColor": "#000000",
        "ImageWidth": 570,
        "ImageHeight": 120,
        "ImageBgColor": "#FFFFFF",
        "Content": contect,
        "ActionCategory": 1
    }

    r = requests.post(url, datas)
    # print(r.text)
    soup = BeautifulSoup(r.content, "html.parser")
    imageurl = soup.find('div', attrs="imgResult")
    print(imageurl.img["src"])
    image_url = imageurl.img["src"]
    br = requests.get(image_url)
    image = Image.open(BytesIO(br.content))
    image.save("书法.png")
    with open("shufa.png", "wb") as f:
        f.write(br.content)
