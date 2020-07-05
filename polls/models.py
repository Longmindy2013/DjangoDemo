import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
"""
模型本质上是数据库表的布局，再附加一些元数据。

Django通过自定义python类的形式来定义具体的模型，每个模型的物理存在方式就是一个python的类class，每个模型代表数据库中的一张表，每个类的实例代表数据表中的一行数据，
类中的每个变量代表数据表中的一列字段。

Django通过模型将python代码和数据库操作操作结合起来，实现对SQL查询语言的封装。

Django通过ORM对数据库进行操作，奉行代码优先的理念，将python程序员和数据库管理员进行分工解耦。

"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 具体的Field实例
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# 每一个Choice选择都关联到一个Question，由python的类来实现，不接触任何SQL语句。
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 外键，Django支持通用的数据关系：一对一，多对一和多对多
    choice_text = models.CharField(max_length=200)  # 文本描述，一些Field类必须提供某些特定的参数，如这条中的max_length，为了数据结构和数据验证功能
    votes = models.IntegerField(default=0)  # 选项投票数

    def __str__(self):
        return self.choice_text
