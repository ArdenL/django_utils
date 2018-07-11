# django_utils
Some utils for django project
Collecting models of django, and extract to docx
Tips:It is used with django shell
***
```
"""
path: 包含所有app的文件夹目录，默认在根目录下，可为空
path: A folder contains what has registered app, in a general way it's your root

file: 生成docx的文件名，需要包含后缀，默认生成的为该项目名
file: this param is a string and is be used to creat file and rename docx when this program be finished, it is 'project_name.docx' in the general case

settings: 注册app的settings文件位置，默认在根目录下，如有变动，则可以用相对路径，用点分割
settings: a path of settings.py

models: 存放所有app以及其中的model
table: 存放表结构，数据内容为json
The param: models&table you need't care, because those will be removed when program finished
"""
import col
col.run(path='', settings='settings', file=None, models='models', table='table')
```
