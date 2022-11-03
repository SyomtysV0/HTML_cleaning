import re
import os

print('------------------')
print('-----original-----')
print('print name_comp')
name_comp = input()
print('print url_comp')
url_comp = input()
print('------------------')
print('-------new--------')
print('print name_comp_new')
name_comp_new = input()
print('print url_comp_new')
url_comp_new = input()
print('------------------')
full_file_list = []
for root, dirs, files in os.walk("."):
    for filename in files:
        full_file_list.append(root+'/'+filename)

for i in full_file_list:
    if i[-4:] == 'html':
        with open(i,'r') as file:
            html = file.read()
        html = html.replace(name_comp, name_comp_new)
        html = html.replace(name_comp.replace(' ',''), name_comp_new)
        html = html.replace(name_comp.replace(' ','').capitalize(), name_comp_new)
        html = html.replace(name_comp.upper(), name_comp_new)
        html = html.replace(name_comp.lower(), name_comp_new)
        html = html.replace(name_comp.capitalize(), name_comp_new)
        html = html.replace(name_comp.title(), name_comp_new)

        html = html.replace(url_comp, url_comp_new)
        html = html.replace(url_comp.upper(), url_comp_new)
        html = html.replace(url_comp.lower(), url_comp_new)
        html = html.replace(url_comp.capitalize(), url_comp_new)
        html = html.replace(url_comp.title(), url_comp_new)
        with open(i,'w') as file1:
            file1.write(html)