import re
import os

full_file_list = []
for root, dirs, files in os.walk("."):
    for filename in files:
        full_file_list.append(root+'/'+filename)
for i in full_file_list:
    if i[-4:] == 'html':
        with open(i,'r') as file:
            html = file.read()
        all_href_one = re.findall('href="(.*)"',html)
        all_href_two = re.findall("href='(.*)'",html)
        all_href = all_href_one+all_href_two

        all_src_one = re.findall('src="(.*)"',html)
        all_src_two = re.findall("src='(.*)'", html)
        all_src = all_src_one + all_src_two

        urls1 = re.findall(r"'(http\S*)'", html, flags=re.M)
        urls2 = re.findall(r'"(http\S*)"', html, flags=re.M)
        urls3 = re.findall(r"\((http\S*)\)", html, flags=re.M)
        urls1 = urls1 + urls2 + urls3

        for a in all_href:
            if a[:4] == 'http':
                html = html.replace(a,'/')
                print(a)
        for b in all_src:
            if b[:4] == 'http':
                html = html.replace(b,'/')
                print(b)
        for c in urls1:
            if c[:4] == 'http':
                html = html.replace(c,'/')
                print(c)

        with open(i,'w') as file1:
            file1.write(html)