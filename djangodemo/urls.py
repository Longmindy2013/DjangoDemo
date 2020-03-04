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
from django.urls import include
from login import views
from polls import views


"""
主路由文件

路由是浏览器输入url，在Django服务器响应url的转发中心。路由都写在urls文件中，它将浏览器输入的url映射到相应的业务处理逻辑，即视图。

include语法相当于多级路由，它将获取到的url地址去除与此项匹配的部分，将剩下的字符串传递给下一级路由urlconf进行判断。

include是一种即插即用的思想。项目根路由根本不关心具体app的路由策略，只管往指定的二级路由进行转发，实现了应用解耦。

app所属的二级路由可根据自己的需要随意编写，不会与其他的app路由发生冲突。app目录可以放置在任何位置，而不用修改路由。

注：除了admin路由外，尽量给每个app设计自己独立的二级路由。

"""

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('index/', views.index)  # 重点是路由表达式和后面的视图函数
]
