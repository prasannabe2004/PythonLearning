#!/usr/bin/python

import os
import sys
import fileinfo

f = fileinfo.FileInfo("C:\Users\Public\Music\Sample Music\Sleep\ Away.mp3")
#print f
#print f.__getitem__("name")
f.__setitem__("Genre",31)        
#print f

mp3File = fileinfo.MP3FileInfo()

#print mp3File
mp3File["name"] = "C:\Users\Public\Music\Sample Music\Sleep\ Away.mp3"
#print mp3File.tagDataMap

#modifying class attribute

class counter:
    count = 0
    def __init__(self):
        self.__class__.count +=1
        
a = counter()
b = counter()

#print b.count
#print counter.count

#Hack for access private functions in python
#print mp3File._MP3FileInfo__parse("C:\Users\Public\Music\Sample Music\Sleep\ Away.mp3")

def FilterFilesByExtn(directory, fileExtList):
    "get list of file info objects for files of particular extensions"
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    print fileList
    fileList = [os.path.join(directory, f) for f in fileList if os.path.splitext(f)[1] in fileExtList]
    return fileList

filelist = FilterFilesByExtn("C:\Users\Public\Music\Sample Music", [".txt"])





