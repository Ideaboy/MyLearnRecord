#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 快速过一遍 css 与 selenium 爬虫
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.get("http://www.skycn.com/soft/liulanqi.html")
page_info = browser.find_element_by_css_selector(
    "body > div.container > div.row.main-row.mt10 > div.lay-790.fr > div.main-list-con > div > div.page-num > a:nth-child(12)").text
print(page_info)
