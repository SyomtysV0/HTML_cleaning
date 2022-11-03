import os
import random
import re
from random import choice
from string import ascii_uppercase
import PIL
from PIL import Image
from PIL import ImageFilter
import requests

trash = []
def pass1():
    pass
prename = ''.join(choice(ascii_uppercase) for i in range(random.randint(3, 8)))
log_mod = 1
os.chdir('vites')
try:
    os.chdir(os.listdir()[1])
except NotADirectoryError:
    os.chdir(os.listdir()[0])
os.mkdir(prename + 'img')
os.mkdir(prename + 'css')

with open('index.html', 'r') as file:
    html_new = file.read()

html_new = html_new.replace('\\','')
urls1 = re.findall(r"'(http\S*)'", html_new, flags=re.M)
urls2 = re.findall(r'"(http\S*)"', html_new, flags=re.M)
urls3 = re.findall(r"\((http\S*)\)", html_new, flags=re.M)
urls1 = urls1 + urls2 + urls3

print(urls1)
css_num = 1
image_num = 1
for url in urls1:
    url = url.split('?')[0]
    if url[-4:].lower() == '.jpg' or url[-4:].lower() == '.png' or url[-4:].lower() == '.gif' or url[-5:].lower() == '.jpeg' or url[-4:].lower() == '.css' or url[-4:].lower() == '.svg':
        # print(url[:4] + '---' + (prename + 'img/')[:4])
        print(url)
        if url[:4] != (prename + 'img/')[:4]:
            try:
                if url[-3:].lower() == 'css':
                    css = prename + '_style_' + str(css_num) + '.' + url[-3:]
                    css_way = prename + 'css/' + css
                    print('download - [ ' + css_way + ' ]')
                    r = requests.get(url, timeout=4)
                    with open(css_way, 'wb') as outfile0:
                        outfile0.write(r.content)
                    html_new = html_new.replace(url, prename + 'css/' + css)
                    css_num += 1
                else:
                    img = prename + 'image_' + str(image_num) + '.' + url.split('.')[-1]
                    imgway = prename + 'img/' + img
                    print('download - [ ' + imgway + ' ]')
                    html_new = html_new.replace(url, imgway)
                    r = requests.get(url, timeout=4)
                    with open(imgway, 'wb') as outfile1:
                        outfile1.write(r.content)
                    image_num += 1
            except requests.exceptions.ConnectionError:
                print('stat hueta')
                trash.append(url)
            except requests.exceptions.ReadTimeout:
                print('time hueta')
                trash.append(url)
            except AttributeError:
                print('AttributeError: hueta')
                trash.append(url)
            except requests.exceptions.InvalidURL:
                print('requests.exceptions.InvalidURL: hueta')
                trash.append(url)
            except requests.exceptions.ConnectionError:
                print('stat hueta')
                trash.append(url)
    else:
        trash.append(url)
        print('replace "/"')

for trash_element in trash:
    html_new = html_new.replace(trash_element, '/')

with open('index.html', 'w') as file1:
    file1.write(html_new)