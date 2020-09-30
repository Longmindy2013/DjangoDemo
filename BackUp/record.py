# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/2/29 5:05 下午
"""

"""
web框架主要包含：路由系统、业务处理逻辑、数据库与模板耦合 - Static（HTML/CSS/JS等静态文件）与ORM数据库。

Django直接使用WSGI通信协议，并实现大部分web相关的内容

MVC/MTV：
    1. MVC - Model View Controller，是模型、视图、控制器的缩写。一种软件工程典范，用业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，
             在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。
             简单点说，就是将代码分散到不同的文件中，把不同类型的文件又放到不同目录下的一种做法。
             
             模型 model：定义数据库相关的内容，一般放在models.py文件中
             视图 view：定义HTML等静态网页文件相关，包含HTML/JS/CSS
             控制器 controller：定义业务逻辑相关，主要代码
    
    2. MTV - Django中view不再与HTML相关，变成主业务逻辑了，相当于控制器。
             HTML被放在Templates中，称作模板T，这样MVC就变成MTV了，本质是一样的。
    
"""

"""
步骤：
    1. 建立文件夹，pycharm自动生成
    2. 创建APP
       在每个Django项目中可以包含多个APP，相当于一个大型项目中的分系统、子模块、功能部件等等，相互之间比较独立，但也可以有联系。所有的APP共享项目资源。
       命令：python3 manage.py startapp login -- 创建一个叫做login的APP，django自动生成"login"文件夹及一系列文件
       
"""