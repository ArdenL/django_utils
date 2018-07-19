from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import math
import os

def img_compress(path, sizes=[(200, 200), (160, 160), (100, 100), (42, 42)]):
    sizes.sort(key=lambda x: x[0], reverse=True)
    img = Image.open(path)
    img_dir, img_name = os.path.split(path)
    name, suffix = os.path.splitext(img_name)
    save_list = []
    for size in sizes:
        img.thumbnail(size, Image.ANTIALIAS)
        new_path = os.path.join(img_dir, name + '_%d' % size[0] + suffix)
        img.save(new_path)
        save_list.append(new_path)
    return save_list

'''
path: img path
text: watermark text
pos:
    be allowed:
        'LT': left top
        'RT': right top
        'T': middle top
        'R': right middle
        'B': bottom middle
        'L': left middle
        'M': middle
        'LB': left bottom
        'RB': right bottom(DEFAULT)
font: font file
    arial.ttf:
    msyh.ttc: 微软雅黑
    simhei.ttf: 黑体
    simsun.ttc: 宋体
    simkai.ttf: 楷体
    STXIHEI.TTF: 华文细黑
    tahoma.ttf:
    verdana.ttf:
font_width: a font's width
color: watermark text color
left: The left distance percent
top: The top distance percent
'''
def img_watermark_text(path, text, pos='RB', font=r'msyh.ttc', size=14, color='#afafaf', opacity=0.5, left=0.1, top=0.1, save_as=False):
    img_dir, img_name = os.path.split(path)
    name, suffix = os.path.splitext(img_name)
    new_path = os.path.join(img_dir, save_as + suffix)

    base_img = Image.open(path)
    watermark_layer = Image.new('RGBA', base_img.size)  # 创建水印层
    font = ImageFont.truetype(os.path.join('fonts', font), size=len(text) * size)  # 设置字体
    draw = ImageDraw.Draw(watermark_layer, 'RGBA')
    draw.text(get_pos(base_img.size, font.getsize(text), pos, left, top), text, font=font, fill=color)
    # watermark = watermark_layer.rotate(23, Image.BICUBIC)  # 旋转
    alpha = watermark_layer.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark_layer.putalpha(alpha)
    Image.composite(watermark_layer, base_img, watermark_layer).save(new_path if save_as else path)
    return new_path if save_as else True


"""
source_img: Original image absolute path
appoint_img: Appoint image absolute path
pos: Setting appoint image position where on original image, it's a tuple contain 2 params: (x, y)
opacity: Opacity percent
"""
def img_watermark_logo(source_img, appoint_img, pos='RB', opacity=.5, left=0.1, top=0.1, save_as=False):
    img_dir, img_name = os.path.split(source_img)  # save as: file_watermark
    name, suffix = os.path.splitext(img_name)
    new_path = os.path.join(img_dir, save_as + suffix)

    src_img = Image.open(source_img)
    app_img = Image.open(appoint_img)
    temp_img = Image.new('RGBA', src_img.size)
    temp_img.paste(app_img.convert('RGBA'), get_pos(src_img.size, app_img.size, pos, left, top))
    alpha = temp_img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    temp_img.putalpha(alpha)

    Image.composite(temp_img, src_img, temp_img).save(new_path if save_as else source_img)
    return new_path if save_as else True

"""
relative scale
src_size: Source image size
pos: Target position
appoint_size: Appointing object width, the object can be a image or a string that been processed
"""
def get_pos(src_size, appoint_size, pos='RB', left=0.1, top=0.1):
    src_w, src_h = src_size
    api_w, api_h = appoint_size

    pos_all = {
        'LT': lambda: (src_w * left, src_h * top),  # left top
        'RT': lambda: (src_w - api_w - src_w * left, src_h * top),  # right top

        'T': lambda: ((src_w - api_w) * 0.5, src_h * top),  # middle top
        'R': lambda: (src_w - api_w - src_w * left, (src_h - api_h) * 0.5),  # right middle
        'B': lambda: ((src_w - api_w) * 0.5, src_h - api_h - src_h * top),  # bottom middle
        'L': lambda: (src_w * left, (src_h - api_h) * 0.5),  # left middle
        'M': lambda: ((src_w - api_w) * 0.5, (src_h - api_h) * 0.5),  # middle

        'LB': lambda: (src_w * left, src_h - api_h - src_h * top),  # left bottom
        'RB': lambda: (src_w - api_w - src_w * left, src_h - api_h - src_h * top),  # right bottom
    }
    res_pos = [math.floor(x) for x in pos_all[pos.upper()]()]
    return res_pos
