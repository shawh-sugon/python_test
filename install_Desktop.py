#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# @Time : 2020/9/7 上午10:16
# @Author : shawh
# @Site : 
# @File : install_Desktop.py
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
    'yum -y groups install "GNOME Desktop"',
    "systemctl set-default graphical.target"
]

for cmd in cmd_list:
    res = os.system(cmd)
    if res != 0:
        print cmd,'失败'
        sys.exit(1)

str_nei="""[daemon]\nAutomaticLoginEnable=True\nAutomaticLogin=root"""
with open("/etc/gdm/custom.conf",'a') as custom:
    custom.write(str_nei)