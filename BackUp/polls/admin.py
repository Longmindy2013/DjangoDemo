from django.contrib import admin
from .models import Question


# Register your models here.
admin.site.register(Question)  # 在admin中注册内容并将polls模型加入站点内，接受站点的管理
