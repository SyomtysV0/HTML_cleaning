import os

full_file_list = []

os.chdir('vites')
try:
    os.chdir(os.listdir()[1])
except NotADirectoryError:
    os.chdir(os.listdir()[0])

for root, dirs, files in os.walk("."):
    for filename in files:
        full_file_list.append(root[1:]+'/'+filename)
for i in full_file_list:
    if i[-4:] == 'html':
        print(i)