# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/10/14 4:06 下午
"""
import os
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


def send_email(email, code):

	from django.core.mail import EmailMultiAlternatives

	subject = '来自www.liujiangblog.com的注册确认邮件'

	text_content = '''
	感谢注册www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python、Django和机器学习技术的分享！
	如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！
	'''
	html_content = '''
	<p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.liujiangblog.com</a>
	这里是刘江的博客和教程站点，专注于Python、Django和机器学习技术的分享！</p>
	<p>请点击站点链接完成注册确认！</p>
	<p>此链接有效期为{}天！</p>
	'''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

	msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()


if __name__ == '__main__':
	# subject = '测试邮件'
	# from_email = '1624683462@qq.com'
	# to_email = '1624683462@qq.com'
	# text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
	# html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
	# msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	# msg.attach_alternative(html_content, "text/html")
	# msg.send()
	pass
