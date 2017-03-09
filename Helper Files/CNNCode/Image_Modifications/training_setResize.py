#!/usr/bin/python
from PIL import Image
import os, sys

def resize(path, originDir, destDir, dimensionX, dimensionY):
	dirs = os.listdir( path+originDir )
	print(dirs)
	for item in dirs:
	    if os.path.isfile(path+originDir+item):
	        im = Image.open(path+originDir+item)
	        f, e = os.path.splitext(path+originDir+item)
	        imResize = im.resize((dimensionX,dimensionY), Image.ANTIALIAS)
	        imResize.save(path + destDir + f[len(path+originDir):]	+ '_resized.jpg', 'JPEG', quality=100)
	        print(imResize)
	    else:
	    	print("could not resize")

path = "../../KaggleCompetition/Resources/DataSets/"
originDir = 'train1/'
destDir = 'train2/'
resize(path, originDir, destDir, 32, 32)
