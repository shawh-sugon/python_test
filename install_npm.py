#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# @Time : 2020/9/1 下午1:53
# @Author : shawh
# @Site : 
# @File : install_npm.py
# @Software: PyCharm

import os,sys

cmd_list =[
    "curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -",
    "yum install -y nodejs",
    "npm install -g cnpm --registry=https://registry.npm.taobao.org",
    "npm install",
    "npm run build",
    "npm -v",
]

for cmd in cmd_list:
    res = os.system(cmd)
    if res != 0:
        print(cmd,'失败')
        sys.exit(1)
