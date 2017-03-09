from PIL import Image
import pickle as cPickle
import os, sys, getopt
from scipy.misc import imread
import csv

def m_unpickle(file):	
	fo = open(file, 'rb')
	dict = cPickle.load(fo)
	fo.close()
	return dict

f = m_unpickle('/Users/adityaraj/Downloads/cifar-10-batches-py/test_batch')
print (f.keys())
print(f['batch_label'])

'''
print(type(f['num_cases_per_batch']))
print(type(f['num_vis']))
print(f['num_vis'])
print(type(f['label_names']))

print(f['label_names'])


f = m_unpickle('/Users/adityaraj/Downloads/cifar-10-batches-py/test_batch')
print (f.keys())


print(f['data'])
print(f['labels'])
print(f['batch_label'])
print(f['filenames'])
'''