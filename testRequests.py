#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json


if __name__ == "__main__":
    URL = "https://www.baidu.com"
    r = requests.get(URL)
    print(r.text)

