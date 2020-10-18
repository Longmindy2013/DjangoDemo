# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/10/16 11:02 上午
"""
import os

# 远端接收数据的服务器
Params = {
	"server": "192.168.0.300",
	"port": 3000,
	"url": '/assets/report/',
	"request_timeout": 30,
}

# 日志文件配置
PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')

