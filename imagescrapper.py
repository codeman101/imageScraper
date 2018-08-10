#!/usr/bin/python3

from urllib.request import urlretrieve# for get them pics
from urllib.request import urlopen
import os # for dir work
import shutil # to move pics to certain folder
# get needed info
again = True
while again:
    dir = input('what is the name of the folder you want the pictures to go into?\n')
    link = input('give me the link of the main page\n')
    print('ok working on it!')
    obj = urlopen(link)
    bytes = obj.read()
    text = bytes.decode('utf8')
    ptr = 0
    jnum = '1' #jpg count number
    while text.find('href', ptr) != -1:
        ptr = text.find('href', ptr)
        ptr+=6
        if text.find('.jpg', ptr) < text.find('"', ptr) and text.find('.jpg', ptr) != -1:
            ptrjpg = text.find('"', ptr)
        else:
            ptr = text.find('"', ptr)
            continue
        link = text[ptr:ptrjpg]
        urlretrieve(link, jnum + '.jpg')
        jnum = int(jnum)
        jnum += 1
        jnum = str(jnum)
    cwd = os.getcwd()

    os.mkdir(dir)
    dest = cwd +  '/' + dir
    print(dest)
    files = os.listdir(cwd)

    for f in files: # for loop to move all pics to the dir
        if (f.endswith('.jpg')):
            shutil.move(f, dest)
    print('done!\n')
    answer  = input('Do you want to get another collection of pictures?[y/n]\n')
    if answer == 'y':
        print('ok program will restart')
    else:
        print('ok program will end')
        again = False
