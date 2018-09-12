#!/usr/bin/python3

from urllib.request import urlretrieve# for getting pictures
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
        ptrjpg=0
        if (text.find('.jpg', ptr) < text.find("'", ptr) or text.find('.jpg', ptr) < text.find("'", ptr)):
            ptr1 = text.find('.jpg', ptr)
            ptr2 = text.find('"', ptr)
            ptr3 = text.find("'", ptr)
            if (ptr2-ptr1) <= 5 and (ptr1-ptr2) <=5:
                ptrjpg = text.find('"', ptr)
            elif (ptr3-ptr1) <= 5 and (ptr1-ptr3) <= 5:
                ptrjpg = text.find("'", ptr)
            else:
                ptr-=1
                if text[ptr] == '"':
                    ptr+=1
                    ptr = text.find('"', ptr)
                    continue
                elif text[ptr] == "'":
                    ptr += 1
                    ptr = text.find("'", ptr)
                    continue
                else: # end of the page was hit
                    break
        else:
            ptr += 10
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
    if len(os.listdir(dest)) == 0:
         print('I did not download anything because the images are of a different '
               'file type than I was programmed for try changing jpg to jpeg in my code')
         os.rmdir(dest)
    else:
        print('done!\n')
    answer  = input('Do you want to get another collection of pictures?[y/n]\n')
    if answer == 'y':
        print('ok program will restart')
    else:
        print('ok program will end')
        again = False
