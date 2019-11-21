# -*- coding:utf-8 -*-

import pytesseract as pt
import requests
from PIL import Image
import os

# url = "https://china-testing.github.io/images/python_lib_ocr_en.png"
save_floder = './ocr_txt'

images_list = os.listdir('./ocr_img')
for item in images_list:
	file_path = os.path.join('./ocr_img', item)
	img = Image.open(file_path)
	text = pt.image_to_string(img)
	with open(os.path.join(save_floder, item+'.txt'), 'w', encoding='utf-8') as wf:
		wf.write(text)

exit()
img = Image.open('./ocr_img.jpg')
# print(img)
text = pt.image_to_string(img)
# print(text)

with open('ocr.txt', 'w', encoding='utf-8') as f:
	f.write(text)

print('OK')