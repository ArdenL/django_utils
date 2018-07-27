# django_utils
Some utils for django project
___
## col.py
Collecting models of django, and extract to docx
**Tips:It is used with django shell**
Third-party package:
* python-docx: pip install python-docx
https://python-docx.readthedocs.io/en/latest/index.html

`col.run(path='', settings='settings', file=None, models='models', table='table')`
>* path: A folder contains what has registered app, in a general way it's your root
path: 包含所有app的文件夹目录，默认在根目录下，可为空
>* file: this param is a string and is be used to creat file and rename docx when this program be finished, it is 'project_name.docx' in the general case
file: 生成docx的文件名，需要包含后缀，默认生成的为该项目名
>* settings: a path of settings.py
settings: 注册app的settings文件位置，默认在根目录下，如有变动，则可以用相对路径，用点分割

>The param: models&table you need't care, because those will be removed when program finished
models: 存放所有app以及其中的model
table: 存放表结构，数据内容为json

```
> python manage.py shell
In: import col
In: col.run()
```
___
## watermark.py
Setting watermark for your image with you wanna string or image
Tips: Taking it must with the folder `./fonts`
Third-party package:
* PIL: pip install pillow (pillow-v5.3.x)

`watermark.img_watermark_text(path, text, pos='RB', font=r'msyh.ttc', size=14, color='#afafaf', opacity=0.5, left=0.1, top=0.1, save_as=False)`
>* path: Original image absolute path
>* text: Setting watermark with you wanna string
>* pos:  Appoint string position in your image
>>be allowed: 'LT','RT','T','R','B','L','M','LB','RB'
>> Detail you can see code
>* font:
>>Be allowed:arial.ttf,msyh.ttc: 微软雅黑，simhei.ttf: 黑体，simsun.ttc: 宋体，simkai.ttf: 楷体，STXIHEI.TTF: 华文细黑，tahoma.ttf,verdana.ttf, and you can take another font with you addition to `fonts`
>* size: Default font size
>* color: It's can be a describe(GhostWhite), hex-code(#F8F8FF) or RGB-code((248,248,255))
>* opacity: As this name
>* left[top]: Related distance with original image
>* save_as: All has processed image will be saved original name, if you want to save asfdcef other name, you can setting it

`img_watermark_logo(source_img, appoint_img, pos='RB', opacity=.5, left=0.1, top=0.1, save_as=False)`
>* source_img: Original image absolute path
>* appoint_img: Appoint image absolute path
>* pos, opacity, left, top, save_as: As those as above describe

```
In: import watermark
In: s, a = 'watermark_example/back.jpg','watermark_example/back_200.jpg'
In: watermark.img_watermark_text(s, 'watermark', save_as='new_text')
Out: 'watermark_example/new_text.jpg'
```
![new_text.jpg](watermark_example/new_text.jpg)
```
In: watermark.img_watermark_logo(s, a)
Out: 'watermark_example/new_img.jpg'
```
![new_img.jpg](watermark_example/new_img.jpg)
___
## data.py
Did you had trouble for when you created a Django project but you didn't had data to test you project?
Now, it will never be your trouble!
**Tips:It is used with django shell**
`create_data(model, force=[], i=1)`
>* model: Model object of installed applications
>* force: General case, the field will be excluded if it can be nullable or have default value，this is a list of fields name of model, field won't be excluded if it in this list
>* i: Creating data times

```
In: from data import create_data
In: from apps.models import my_model
In: create_data(my_model)
```
You can check your data base after you done above command.
The data had created!
You needn't to care foreign-key, of course if your fields need a foreign-key but it hadn't created then this way will automatical creat it once.
