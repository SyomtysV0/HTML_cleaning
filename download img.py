import os
import random
import re
from random import choice
from string import ascii_uppercase
import requests
import PIL
from PIL import Image
from PIL import ImageFilter

prename = ''.join(choice(ascii_uppercase) for i in range(random.randint(3, 8)))

os.chdir('vites')
os.chdir(os.listdir()[1])
os.mkdir(prename + 'img')
os.mkdir(prename + 'css')

url_for_donload = str(os.getcwd()).split('/')[len(str(os.getcwd()).split('/'))-1]


def ReplaseUrl(ReplaceUrl, HrefFile):
    if HrefFile[0:2] == '//':
        HrefFile = 'https:' + HrefFile
    elif HrefFile[0:4] == 'http':
        pass
    else:
        if HrefFile[0:6] == '../../':
            HrefFile = ReplaceUrl + HrefFile[6:]
        elif HrefFile[0:4] == '././':
            HrefFile = ReplaceUrl + HrefFile[4:]
        elif HrefFile[0:3] == '../':
            HrefFile = ReplaceUrl + HrefFile[3:]
        elif HrefFile[0:1] == '/':
            HrefFile = ReplaceUrl + HrefFile[1:]
        elif HrefFile[0:1] == ' ':
            HrefFile = ReplaceUrl + HrefFile[1:]
        elif HrefFile[0:2] == './':
            HrefFile = ReplaceUrl + HrefFile[2:]
        elif HrefFile[0:3] == '/-/':
            HrefFile = ReplaceUrl + HrefFile[3:]
        else:
            HrefFile = ReplaceUrl + HrefFile
    return HrefFile

css_num = 1
image_num = 1
def SaveUrl(url_for_donload, urls, html_new):
    global image_num, css_num
    for n in range(len(urls)):
        urls1234 = str(urls[n])
        urls1234 = urls1234[4:].split(')')[0] if urls1234[:4] == 'url(' else urls1234
        if urls1234[-1:] == '\'':
            urls1234 = str(urls1234.split('\'')[1])
        if urls1234[-1:] == '"':
            urls1234 = str(urls1234.split('"')[1])
        urls1234 = urls1234.replace(' ', '')
        urls1234 = urls1234.replace('\\', '')
        urls1234Old = urls1234
        urls1234 = urls1234.split('?')[0]
        if urls1234[-3:].lower() == 'jpg' or urls1234[-3:].lower() == 'png' or urls1234[-3:].lower() == 'gif' or urls1234[-3:].lower() == 'peg' or urls1234[-3:].lower() == 'css':
            if urls1234Old[:4] != (prename + 'img/')[:4]:
                urls12345 = ReplaseUrl(url_for_donload, urls1234)
                try:
                    if urls12345[-3:].lower() == 'css':
                        css = prename +'_style_' + str(css_num) + '.' + urls12345[-3:]
                        html_new = html_new.replace(urls1234Old, prename +'css/' + css)
                        print(urls12345)
                        r = requests.get(urls12345, verify=False)
                        r = requests.get(urls12345)
                        with open(prename +'css/'+css, 'wb') as outfile:
                            outfile.write(r.content)
                        print('download - [ ' + css + ' - ' + str(r.status_code) + ' ]')
                        css_num += 1
                    else:
                        img = prename + 'image_' + str(image_num) + '.' + urls12345.split('.')[-1]
                        imgway = prename + 'img/' + img
                        html_new = html_new.replace(urls1234Old, imgway)
                        try:
                            r = requests.get(urls12345, timeout=4)
                            with open(imgway, 'wb') as outfile:
                                outfile.write(r.content)
                            if urls12345[-3:].lower() != 'png':
                                try:
                                    im = Image.open(imgway)
                                    if im.mode != 'RGB':
                                        im = im.convert('RGB')
                                    im = im.filter(ImageFilter.EDGE_ENHANCE)
                                    im = im.filter(ImageFilter.GaussianBlur(radius=1))
                                    im = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                                    im.save(imgway)
                                except TypeError:
                                    print('dont save')
                                except PIL.UnidentifiedImageError:
                                    print('dont save')
                            image_num += 1
                            print('download - ' + img)
                        except requests.exceptions.ConnectionError:
                            print('stat hueta')
                        except requests.exceptions.ReadTimeout:
                            print('time hueta')
                except requests.exceptions.ConnectionError:
                    print('stat hueta')
        else:
            # html_new = html_new.replace(urls1234Old, '/')
            print('replace "/"')

    return html_new



with open('index.html', 'r') as file:
    html_new = file.read()

url_img = re.findall(r"(url[(][\s\S]*?[\)])", html_new, flags=re.M)
html_new = SaveUrl(url_for_donload, url_img, html_new)

data_src = re.findall(r"(data-src=?\S+[\"|\'])", html_new, flags=re.M)
html_new = SaveUrl(url_for_donload, data_src, html_new)

data_image = re.findall(r"(data-image=\S+[\"|\'])", html_new, flags=re.M)
html_new = SaveUrl(url_for_donload, data_image, html_new)

imagesurl = re.findall(r"(src=\S+[\"|\'])", html_new, flags=re.M)
html_new = SaveUrl(url_for_donload, imagesurl, html_new)

data_dce_background_image_url = re.findall(r"(data-dce-background-image-url=\S+[\"|'])", html_new, flags=re.M)
html_new = SaveUrl(url_for_donload, data_dce_background_image_url, html_new)

imagesurl = re.findall(r"(href=\"\S+[\"|\'])", html_new[:html_new.find('<body')], flags=re.M)
html_new = SaveUrl(url_for_donload, imagesurl, html_new)

with open('index.html', 'w') as file1:
    file.write(html_new)