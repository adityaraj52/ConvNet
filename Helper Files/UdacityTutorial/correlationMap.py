# Import statements
from Assignment01_Functions import * 
from IPython.display import display, Image
from skimage.measure import compare_ssim as ssim
import numpy as np
import time											# Measure runtime
import matplotlib.image as mpimg					# Displaying images

def load_data():
	''' Load the data which consists of images. '''

	# Variable declaration
	url = 'http://commondatastorage.googleapis.com/books1000/'
	last_percent_reported = None # Used to display percentage of download process
	subdirectory = './data/'     # Subdirectory where all the data is stored

	# Both overgiven variables are used within Assignment01_Functions as global variables.
	set_global_variables(last_percent_reported, subdirectory)

	pickle_file = subdirectory + 'notMNIST.pickle'  # Pickle target file.

	data = pickle.load(open(pickle_file, 'rb'))

	return(data)


def similarity_of_images(data, size):
	''' Uses ssim of skimage to measure the similarity of different pictures and saves 
	the result in similiarity_matrix. The matrix has the same appearance as a distance 
	matrix. 
	Values are between -1 and 1, where 1 means similar, 0 are there initially.'''

	similarity_matrix = np.zeros(shape = (size, size))

	# Measure time to estimate runtime of program
	start = time.time()

	for i in range(size):
		for j in range(i):
			similarity_matrix[j][i] = ssim(data[j],data[i])

	end = time.time()
	runtime = end - start

	print('Calculation of ssim took ' + str(round(runtime,4)) + ' for ' + str(size) + ' images. \n')

	return similarity_matrix


def get_similar_images(matrix, value):
	''' Return pairs of pictures which are larger than a given value. Seems to work fine for 
	value equals to 0.9, might also work for lower values. '''

	index_of_similar_images = np.where(matrix > value)

	return(index_of_similar_images)


def visualize_similar_images(similar_images, data, number = 3):
	''' Visualize the first three pairs of images to show what similarity means. '''

	print('Displaying the first three pairs of nearly similar images: \n')

	# TODO
	# Title of images does not fit

	for i in range(number):
			fig = plt.figure()
			a=fig.add_subplot(1,2,1)
			imgplot = plt.imshow(data[similar_images[0][i]], cmap = plt.gray())
			a.set_title(similar_images[0][i])
			a=fig.add_subplot(1,2,2)
			imgplot = plt.imshow(data[similar_images[1][i]], cmap = plt.gray())
			a.set_title(similar_images[1][i])
			plt.show()

def remove_duplicates(similar_images, data):

	print(data.shape)

	print(similar_images[0])

	# Is deleting 3 entries in ndarray, not three images
	data = np.delete(data, similar_images[1])

	print(data.shape)

	data = data.reshape(19997, 28, 28)

	print(data.shape)


def main():

	# Get the data
	data = load_data()
	name = 'train_dataset'

	data = data[name]

	print(data.shape)

	# # Set number of values behind comma which is printed out
	# np.set_printoptions(precision = 3)

	# # Calculate similar images
	# similarity_matrix = similarity_of_images(data, 200)

	# # Save result in similarityMap
	# display_name = name[0].upper() + name[1:]
	# similarity_matrix.dump('data/similarityMap' + display_name + '.pickle')

	# # Get similar images from matrix
	# similar_images = get_similar_images(similarity_matrix, 0.9)

	# # Visualize some similar images
	# visualize_similar_images(similar_images, data)

	# TODO
	# Compare the whole test_data
	# Compare the whole training_data
	# Compare the whole test with the whole train_data
	# Remove one of the similar images

	# remove_duplicates(similar_images, data)


if __name__=='__main__':

  main()