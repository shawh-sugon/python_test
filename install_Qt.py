#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# @Time : 2020/9/2 上午9:04
# @Author : shawh
# @Site : 
# @File : install_Qt.py
# @Software: PyCharm
import os,sys


if os.getuid()==0:
	pass
else:
	print "当前用户不是root用户，请用root用户执行脚本。"
	sys.exit(1)
#
# version = raw_input("请输入你想安装的Qt版本(2.7/3.8)：")


cmd_list =[
    "wget http://download.qt.io/official_releases/qt/5.14/5.14.0/qt-opensource-linux-x64-5.14.0.run",
    "yum -y install mesa-libGL-devel mesa-libGLU-devel freeglut-devel",
    "yum install xauth -y",
    "chmod +x qt-opensource-linux-x64-5.14.0.run",
    "./qt-opensource-linux-x64-5.14.0.run",
]

for cmd in cmd_list:
    res = os.system(cmd)
    if res != 0:
        print cmd,'失败'
        sys.exit(1)


