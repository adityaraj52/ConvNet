#!/usr/bin/python
# Execute this with python 2.7
import csv
from PIL import Image
import os, sys

test_array = []

def labelData(path, originDir, destDir):
	dirs = os.listdir( path+originDir )
	i = 0
	count_cat = 0
	count_dog = 0

	for item in dirs:
		file = path+originDir+item
		name = file[len(path+originDir):len(path+originDir)+3]
		if os.path.isfile(file):
			if("cat" in name):
				count_cat = count_cat + 1;
				test_array.append({'': i, 'filename': item, 'label': '0'});
			if("dog" in name):
				count_dog = count_dog + 1;
				test_array.append({'': i, 'filename': item, 'label': '1'});
		else:
			print("Cant read");
		i = i+1;
	print(count_dog)
	print(count_cat)
	writeCSV(destDir)	


def writeCSV(destDir):
	fieldnames = ['', 'filename', 'label']
	test_file = open(destDir,'wb')
	csvwriter = csv.DictWriter(test_file, delimiter=',', fieldnames=fieldnames)
	#csvwriter.writerow(dict((fn,fn) for fn in fieldnames))

	for row in test_array:
	     csvwriter.writerow(row)
	test_file.close()


path = "../../DataSets/"
originDir = 'train1/'
destDir = '../../DataSets/training_label.csv'
labelData(path, originDir, destDir)

