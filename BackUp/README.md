# DjangoDemo
&emsp;&emsp;本repo主要是针对 [刘江的博客教程](https://www.liujiangblog.com/course/django/88?c=1961) 对Django进行系统性、深入性
的学习，在此进行记录。

## 常用指令
> migrations是Django保存模型修改记录的文件，并保存在磁盘上。对应的就是0001_initial.py。

- python3 manage.py check 
    - 检查项目中的错误，并不实际进行迁移或者链接数据库的操作
    
- python3 manage.py migrate 
    - migrate命令对所有还未实施的迁移记录进行操作，本质上就是将你对模型的修改体现到数据库中具体的表上面。
    - django通过一张叫做django_migrations的表，记录并跟踪已经实施的migrate动作，通过对比获得哪些migrations尚未提交。
    - migrations允许随时修改你的模型，不需要删除或者新建数据库或者数据表，在不丢失数据的同时，实时动态更新数据库。
    - 修改模型时的操作步骤：
        1. 在model.py中修改模型
        2. 运行python3 manage.py makemigrations 为改动创建迁移记录
        3. 运行python3 manage.py migrate 将操作同步到数据库
        > 此处第二三步分开主要是考虑到版本控制系统的存在，避免丢失中间过程。

- python3 manage.py shell
    - 此处调用manage.py参数能够将DJANGO_SETTINGS_MODULE环境变量导入，可以按照settings.py中的设置，配置好python shell环境。