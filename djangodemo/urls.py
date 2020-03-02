"""djangodemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views


"""
主路由文件

路由是浏览器输入url，在Django服务器响应url的转发中心。路由都写在urls文件中，它将浏览器输入的url映射到相应的业务处理逻辑，即视图。
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index)  # 重点是路由表达式和后面的视图函数
]
