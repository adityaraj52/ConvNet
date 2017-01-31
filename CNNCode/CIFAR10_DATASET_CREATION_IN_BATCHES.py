'''
	To convert Given set of images in batches for TensorFlow Input using CIFAR10 Format
	For more see: http://www.cs.toronto.edu/~kriz/cifar.html
	For More see: https://www.tensorflow.org/tutorials/deep_cnn/
	
	How to Use:
	
	To Use this Instantiate an object of Class imagePickling giving the arguments:
		@p (str) 	input_dir = Directory from which we want to create the training batch
	  	@p (str) 	output_dir = Directory from which we want to output the training batch
	  	@p (str) 	filename = Name of the file after the training batch is created
	  	@p (int32) 	lowerLimit = Lower Limit for reading the data from the training set 
	  	@p (int32) 	upperLimit = Lower Limit for reading the data from the training set 
	  	@p (int32)	batchLabel = Each batch gets a label in incrementing fashion. 
	  							 Example: First batch gets batchLabel 1
  										  Second batch gets batchLabel 2
  										  and so on...
'''
from PIL import Image
import pickle as cPickle
import os, sys, getopt
from scipy.misc import imread
import csv

class imagePickling:

	def __init__(self, p_input_directory, p_output_directory, p_filename, p_ll, p_ul, p_batchLabel ):
		self.m_input_directory = p_input_directory;
		self.m_output_directory = p_output_directory;
		self.m_output_filename = p_filename;
		self.m_lowerLimit = p_ll;
		self.m_upperLimit = p_ul;
		self.m_batchLabel = p_batchLabel;
	
	def m_pickle(self, file):
		return (cPickle.dump(file, open(self.m_output_directory+self.m_output_filename, "wb")))
	
	def m_unpickle(self, file):	
		fo = open(file, 'rb')
		dict = cPickle.load(fo)
		fo.close()
		return dict
	
	def m_image2array(self):
		dirs = os.listdir( self.m_input_directory )
		temp = []
		label = []
		for item in self.m_getFileNames():
			if( (item.endswith('.jpg')) or (item.endswith('.png')) or (item.endswith('.jpeg')) ) :
				img = imread(self.m_input_directory+item, flatten=True)
				img = img.astype('double')
				temp.append(img)
				if("cat" in item):
					label.append(0)
				elif("dog" in item):
					label.append(1)
				else:
					print("Incorrect Label")
			else:
				print("Can not read file... Possibly incorrect file encountered");
				sys.exit(2);
		return temp, label
	
	def m_getFileNames(self):	
		return ((os.listdir(self.m_input_directory))[self.m_lowerLimit:self.m_upperLimit])
	
	def m_createDictionary(self):
		l_imageArray, l_labelArray = self.m_image2array();
		return {'data': l_imageArray, 'labels': l_labelArray, 'batch_label': self.m_batchLabel, 'filenames':self.m_getFileNames()}
	
	def __runSession__(self):
		self.m_pickle(self.m_createDictionary())

def main():
	input_dir = '/Users/adityaraj/Documents/NeuralNetworkKaggleCompetition/DataSets/train1/'
	output_dir = '/Users/adityaraj/Documents/NeuralNetworkKaggleCompetition/DataSets/'
	lowerLimit = 0
	upperLimit = 10
	range = upperLimit - lowerLimit
	num_train_batches = 5
	num_test_batches = 1
	i = 0
	image_size = 28

	if(not( (os.path.exists(input_dir)) or (os.path.exists(data_dir)) )):
		print("wrong path input")
		sys.exit(2)

	while i<num_train_batches:
		filename = "data_batch_"+str(i+1)
		batchLabel = "training batch " + str(i) + " of " + str(num_train_batches);
		i += 1
		x = imagePickling(input_dir, output_dir, filename, lowerLimit, upperLimit, batchLabel);
		x.__runSession__()
		y = x.m_unpickle(output_dir + filename)
		print("\nFor file ", i)
		print ("\nKeys are \n", y.keys())
		print ("\nLabels are \n", y['labels'])
		print ("\nBatch Labels are \n", y['batch_label'])
		lowerLimit = upperLimit;
		upperLimit += range
	i = 0 
	
	while i<num_test_batches:
		filename = "test_batch_"+str(i)
		batchLabel = "testing batch " + str(i) + " of " + str(num_train_batches);
		i += 1
		x = imagePickling(input_dir, output_dir, filename, lowerLimit, upperLimit, batchLabel);
		x.__runSession__()
		y = x.m_unpickle(output_dir + filename)
		print ("Keys are ", y.keys())
		print ("\nLabels are ", y['labels'])
		print ("\nBatch Labels are ", y['batch_label'])
		lowerLimit = upperLimit;
		upperLimit += range

	list = ['cat', 'dog']
	batches_meta = {'num_cases_per_batch':range, 'label_names': list, 'num_vis':image_size*image_size*3}
	cPickle.dump(batches_meta, open(output_dir+"batches_meta", "wb"))


if __name__ == "__main__":
	main()
