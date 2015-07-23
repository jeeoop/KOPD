# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:15:07 2015

@author: Ken Ouyang
"""

import os
for dirname,dirnames,filenames in os.walk('/home/ken/Desktop/backup/'):
    #for subdirname in dirnames:
        #print (os.path.join(dirname,subdirname))
    for filename in filenames:
        print(os.path.join(dirname,filename))

list1 = []
for dirname,dirnames,filenames in os.walk('/home/ken/Desktop/backup/'):
    for subdirname in dirnames:
        list1.append(os.path.join(dirname,subdirname))

import os, time,exifread
for dirname,dirnames,filenames in os.walk('/home/ken/Desktop/backup/'):
    for filename in filenames:
        filenamepath = (os.path.join(dirname,filename))
        print filenamepath\
        ,time.ctime(os.path.getctime(filenamepath))\
        ,round(os.stat(filenamepath).st_size/1024.0,2)




import os, time,exifread
for dirname,dirnames,filenames in os.walk('/home/ken/Desktop/backup/'):
    for filename in filenames:
        filenamepath = (os.path.join(dirname,filename))
        if os.stat(filenamepath).st_size/1024.0 > 1200:
            print filenamepath\
            ,time.ctime(os.path.getctime(filenamepath))\
            ,round(os.stat(filenamepath).st_size/1024.0,2)



import exifread, shutil
with open('/home/ken/Desktop/backup/recup_dir.60/f24090317.jpg', 'rb') as photo:
    tags = exifread.process_file(photo)
tags['EXIF DateTimeOriginal']
str(tags['Image Make'])

str(tags['EXIF DateTimeOriginal']).replace(':','').replace(' ', '')


def dtft(indt):
    from datetime import datetime
    return datetime.strptime(indt, '%Y-%m-%d').date()


import os, exifread, subprocess
for dirname,dirnames,filenames in os.walk('/home/ken/Desktop/backup/'):
    for filename in filenames:
        filenamepath = (os.path.join(dirname,filename))
        if filenamepath.split('.')[-1] == 'jpg':
            if os.stat(filenamepath).st_size/1024.0 > 600:
                try:
                    with open(filenamepath, 'rb') as photo:
                        tags = exifread.process_file(photo)
                        exifdat = str(tags['EXIF DateTimeOriginal'])[:10].replace(':','-')
                        timestamp = str(tags['EXIF DateTimeOriginal']).replace(':','').replace(' ', '')
                        device = str(tags['Image Model'])
                        newfolder = exifdat[:7].replace('-','')
                        if device == 'Canon EOS REBEL T3i':
                            newfilename = 'canon' + timestamp + '.jpg'
                            newpath = '/home/ken/backup/photo/'+newfolder + '/'
                            erchk1 = subprocess.call('mkdir -p ' + newpath, shell=True)
                            shutil.copy(filenamepath, newpath+newfilename)
                        elif device == 'SGH-T989':
                            newfilename = 'SGHT' + timestamp + '.jpg'
                            newpath = '/home/ken/backup/photo/'+newfolder + '/'
                            erchk1 = subprocess.call('mkdir -p ' + newpath + newfilename, shell=True)
                            shutil.copy(filenamepath, newpath+newfilename)                            
                        else:
                            newfilename = 'File' + timestamp + '.jpg'
                            newpath = '/home/ken/backup/other/'+newfolder + '/'
                            erchk1 = subprocess.call('mkdir -p ' + newpath + newfilename, shell=True)
                            shutil.copy(filenamepath, newpath+newfilename)
                except:
                    shutil.copy(filenamepath, '/home/ken/backup/noexif/')
            else:
                shutil.copy(filenamepath, '/home/ken/backup/smalljpg/')
        else:
            shutil.copy(filenamepath, '/home/ken/backup/notjpg/')






['Canon EOS REBEL T3i', 'SGH-T989']



import os, exifread
dv22 = []
for dirname,dirnames,filenames in os.walk('/home/ken/Desktop/backup/'):
    for filename in filenames:
        filenamepath = (os.path.join(dirname,filename))
        if filenamepath.split('.')[-1] == 'jpg':
            if os.stat(filenamepath).st_size/1024.0 > 800:
                try:
                    with open(filenamepath, 'rb') as photo:
                        tags = exifread.process_file(photo)
                        exifdat = str(tags['EXIF DateTimeOriginal'])[:10].replace(':','-')
                        device = str(tags['Image Make'])
                        dv2 = str(tags['Image Software'])
                        dv22.append(dv2)                        
                        #if device.lower() == 'ipad':
                        #    print exifdat, 'ipad'
                        #elif device.lower() == 'samsung':
                        #    print exifdat, 'samsung'
                        #elif device.lower() == '':
                        #    print exifdat, 'apple'
                except:
                    pass
            else:
                pass
        else:
            pass

testlist = list(set(dv22))
['T989UVMC6', 'T989UVKID']

tags
tags['Model']








dv22 = []
for dirname,dirnames,filenames in os.walk('/home/ken/Desktop/backup/'):
    for filename in filenames:
        filenamepath = (os.path.join(dirname,filename))
        if filenamepath.split('.')[-1] == 'jpg':
            if os.stat(filenamepath).st_size/1024.0 > 800:
                try:
                    with open(filenamepath, 'rb') as photo:
                        tags = exifread.process_file(photo)
                        exifdat = str(tags['EXIF DateTimeOriginal'])[:10].replace(':','-')
                        device = str(tags['Image Make'])
                        dv2 = str(tags['Image Model'])
                        dv22.append(dv2)                        
                        #if device.lower() == 'ipad':
                        #    print exifdat, 'ipad'
                        #elif device.lower() == 'samsung':
                        #    print exifdat, 'samsung'
                        #elif device.lower() == '':
                        #    print exifdat, 'apple'
                except:
                    pass
            else:
                pass
        else:
            pass














