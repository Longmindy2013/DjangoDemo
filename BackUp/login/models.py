from django.db import models

# Create your models here.


class UserInfo(models.Model):  # 固定写法
    usr = models.CharField(max_length=32)  # 创建两个字段，最大长度是32，数据类型是char
    pwd = models.CharField(max_length=32)
    # 使用：python3 manage.py makemigrations 创建数据库表
