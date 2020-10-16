# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/10/16 10:39 上午
"""

import json
import time
import urllib.parse
import urllib.request
from core import info_collection
from conf import settings


class ArgvHandler(object):

	def __init__(self, args):
		self.args = args
		self.parse_args()

	def parse_args(self):
		""" 分析参数，如果有指定参数的方法，则执行该功能，若没有则打印说明 """
		if len(self.args) > 1 and hasattr(self, self.args[1]):
			func = getattr(self, self.args[1])
			func()
		else:
			return self.help_msg()

	@staticmethod
	def help_msg():
		"""
		帮助说明
		:return:
		"""
		msg = '''
			参数名               功能
			collect_data        测试收集硬件信息的功能
			report_data         收集硬件信息并汇报
	    '''
		print(msg)

	@staticmethod
	def collect_data():
		""" 收集硬件信息，用于测试 """
