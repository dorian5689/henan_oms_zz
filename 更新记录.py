#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/17 0:58
@Auth ： Xq
@File ：更新记录.py
@IDE ：PyCharm
"""
"""
2012-01-17

问题0001:
增加延时2S

问题0002:
增加判断

新功能0001:
飞翔三期储能更新数据库
并能在帆软展示

2024/1/17 0:58
1.
    添加程序卡死  
    捕捉异常暂停30S 重新运行
2.
    时间确定00:08、


2024/1/23 0:58
1.
    更新了异常捕捉
2.
    金燕现场上报,集控不再上报

"""

"""
2024/1/24 0:58
上报后数据保存到本地
桌面添加链接文件夹
方便相关人员查看今日上报数据
不再运行程序切换

"""
"""
2024/2/5 0:58
import sys
import os

# 获取当前脚本的绝对路径
script_path = os.path.abspath(__file__)

# 获取当前脚本的目录路径
script_dir = os.path.dirname(script_path)

# 获取当前脚本的父目录路径
parent_dir = os.path.dirname(script_dir)

# 将父目录添加到sys.path
sys.path.append(parent_dir)

# 现在你可以导入位于父目录下的模块了
print("父目录已添加到sys.path")


"""


