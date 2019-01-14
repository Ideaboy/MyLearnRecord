#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018年12月26日10:42:06
# py - win32 回顾统治

import win32api
import win32con
import win32gui
import os


if __name__ == "__main__":
    # win32api.MessageBox(win32con.NULL, "First pywin32.窗口", "Hello pywin32~!", win32con.MB_OK)
    name = r"C:\Program Files\OpenVPN\bin\openvpn-gui.exe".replace("\\", "//")
    # os.startfile(name)
    # wdname = "learn_"
    wdname = "OpenVPN - User Authentication"
    # wdname = "OpenVpn Connection(kaopuyun)"
    # 1490, 1060 双击
    # win32api.SetCursorPos()
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN\
    #                      )
    # 找到窗口句柄
    handle = win32gui.FindWindow(0, wdname)
    # 返回 x,y,w,h
    handleDetail = win32gui.GetWindowRect(handle)
    print(handleDetail)
    mouseXY = (handleDetail[0], handleDetail[1])
    # 鼠标移位
    win32api.SetCursorPos(mouseXY)
    #   700, 625  , dx = 100~ , dy=50 用户名位置差
    win32api.SetCursorPos((handleDetail[0]+100, handleDetail[1]+50))
    #   700 , 650~670 , dx=100, dy=70
    win32api.SetCursorPos((handleDetail[0]+100, handleDetail[1]+70))
