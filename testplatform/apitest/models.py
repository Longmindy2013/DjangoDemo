from django.db import models

# Create your models here.


class login(models.Model):
	pass


class tucao(models.Model):
	user = models.CharField(max_length=16, null=True)
	text = models.CharField(max_length=1024, null=True)
	ctime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text + str(self.ctime)
