# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/10/14 4:06 下午
"""
import os
from django.core.mail import EmailMultiAlternatives


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


if __name__ == '__main__':
	subject = '测试邮件'
	from_email = '1624683462@qq.com'
	to_email = '1624683462@qq.com'
	text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
	html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
