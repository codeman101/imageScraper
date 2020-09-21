#!/usr/bin/python3

# this script downloads the html page of a given link and parses through it looking for href attributes and grabbing the link that follows as
# a substring and then uses urlretrieve module to download the image from the link


from urllib.request import urlretrieve# for getting images
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
    jnum = 1 #jpg count number
    while text.find('href', ptr) != -1:
        ptr = text.find('href', ptr)
        if text[ptr+5] == "'":
            quote_type = "'"
        else: quote_type = '"'
        ptr+=6
        link = text[ptr:text.find(quote_type, ptr)]
        try:
            if "jpg" in link or "jpeg" in link:
                urlretrieve(link, str(jnum) + '.jpg')
            else:
                continue
        except:
            print("link failed to dl and link was "+link)
            continue
        jnum += 1
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
        picspath = "~/Pictures"
        picspath = os.path.expanduser(picspath)
        shutil.move(dir, picspath)
        print('done!\n')
    answer  = input('Do you want to get another collection of pictures?[y/n]\n')
    if answer == 'y':
        print('ok program will restart')
    else:
        print('ok program will end')
        again = False
