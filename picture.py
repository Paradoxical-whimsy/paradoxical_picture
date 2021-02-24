#从PIL库导入Image模块
from PIL import Image

#打开图片并赋值给img变量
img = Image.open('cat.jpg')

#将图片转化为灰度图
img_gray = img.convert('L')

#获取图片分割的各个部分
img_left_top = img_gray.crop((0, 0, img.width / 2, img.height / 2))

img_right_top = img_gray.crop((img.width / 2, 0, img.width, img.height / 2))

img_left_bottom = img_gray.crop((0, img.height / 2, img.width / 2, img.height))

img_right_bottom = img_gray.crop((img.width / 2, img.height / 2, img.width, img.height))

#创建空白图片
new_img = Image.new('RGBA', img.size, (255, 255, 255))

#把图片粘贴到新图片上
new_img.paste(img_left_top, (int(img.width / 2), int(img.height / 2)))

new_img.paste(img_right_top, (0, int(img.height / 2)))

new_img.paste(img_left_bottom, (int(img.width / 2), 0))

new_img.paste(img_right_bottom, (0, 0))

#保存图片
new_img.save('pic.png')
