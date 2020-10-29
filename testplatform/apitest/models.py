from django.db import models

# Create your models here.


class User(models.Model):

	gender = (
		('male', '男'),
		('female', '女')
	)

	name = models.CharField(max_length=16, unique=True)
	password = models.CharField(max_length=256)
	email = models.EmailField(unique=True)
	sex = models.CharField(max_length=16, choices=gender, default='男')
	ctime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-ctime"]
		verbose_name = '用户'
		verbose_name_plural = '用户'


class tucao(models.Model):
	user = models.CharField(max_length=16, null=True)
	text = models.CharField(max_length=1024, null=True)
	ctime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text + str(self.ctime)


class home_link(models.Model):
	link_name = models.CharField(max_length=50, null=True, help_text='超链接名称')
	link_content = models.CharField(max_length=1024, null=True, help_text='超链接内容')

	def __str__(self):
		return self.link_name


class project(models.Model):
	project_name = models.CharField(max_length=1000, null=True, verbose_name='项目名称')
	project_remark = models.CharField(max_length=1000, null=True, verbose_name='项目备注')
	project_build_user = models.CharField(max_length=256, null=True, verbose_name='项目创建者名称')
	project_build_other_user = models.CharField(max_length=256, null=True, verbose_name='项目其他创建者的名称')

	def __str__(self):
		return self.project_name

