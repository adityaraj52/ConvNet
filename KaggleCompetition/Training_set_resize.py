#!/usr/bin/python
from PIL import Image
import os


def resize(path, origin_dir, dest_dir, dimension_x, dimension_y):
    dirs = os.listdir(path+origin_dir)
    print(dirs)
    for item in dirs:
        if os.path.isfile(path+origin_dir+item):
            im = Image.open(path+origin_dir+item)
            f, e = os.path.splitext(path+origin_dir+item)
            im_resize = im.resize((dimension_x, dimension_y), Image.ANTIALIAS)
            im_resize.save(path + dest_dir + f[len(path+origin_dir):] + '.jpg', 'JPEG', quality=100)
            print(im_resize)
        else:
            print("Resizing was not possible.")

path = "Resources/DataSets/"
origin_dir = 'train1/'
dest_dir = 'train2/'
resize(path, origin_dir, dest_dir, 32, 32)
