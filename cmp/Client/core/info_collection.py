# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/10/16 10:45 上午
"""
import sys
import platform


class InfoCollection(object):

	def collect(self):
		""" 收集平台信息，判断当前所在平台，根据平台的不同使用不同的方法 """
		try:
			func = getattr(self, platform.system().lower())
			info_data = func()
			formatted_data = self.build_report_data(info_data)
			return formatted_data
		except AttributeError:
			sys.exit("不支持当前系统：[%s]".format(platform.system()))

	@staticmethod
	def linux():
		from plugins.collect_linux_info import collect
		return collect

	@staticmethod
	def windows():
		from plugins.collect_windows_info import Win32Info
		return Win32Info().collect()

	@staticmethod
	def build_report_data(data):
		pass
		return data
