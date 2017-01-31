###################################################################################
# Docstring information

###################################################################################
# Import statements
from Assignment01_Functions import *

###################################################################################
__author__ = "Sören Schleibaum"
__copyright__ = "Copyright 2016, Sören Schleibaum"

__maintainer__ = "Sören Schleibaum"
__email__ = "sosch56@gmail.com"


# The original code was published on:
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb

def main():

  # Variable initialization
  # global last_percent_reported
  # global subdirectory

  # Variable declaration
  url = 'http://commondatastorage.googleapis.com/books1000/'
  last_percent_reported = None
  subdirectory = './data/'

  set_global_variables(last_percent_reported, subdirectory)
  
  # Download the data set.
  train_filename = maybe_download('notMNIST_large.tar.gz', 247336696, url)
  test_filename = maybe_download('notMNIST_small.tar.gz', 8458043, url)

  num_classes = 10          # Number of folders
  np.random.seed(133)       # Makes the random numbers predictable

  # Extract the downloaded .gz-files.
  train_folders = maybe_extract("notMNIST_large.tar.gz", num_classes)
  test_folders = maybe_extract("notMNIST_small.tar.gz", num_classes)

  # # TODO
  # # Display images
  # # Image(filename='./notMNIST_small/A/MDEtMDEtMDAudHRm.png')
  # # local_file = FileLink("/notMNIST_small/A/MDEtMDEtMDAudHRm.png")
  # # display(local_file)

  image_size = 28           # Pixel width and height.
  pixel_depth = 255.0       # Number of levels per pixel.

  # 
  train_datasets = maybe_pickle(train_folders, 45000, image_size, pixel_depth)
  test_datasets = maybe_pickle(test_folders, 1800, image_size, pixel_depth)

  # Define framework data.
  train_size = 200000
  valid_size = 10000
  test_size = 10000

  # Merge the small pickle files of training and testing data to one large each. 
  valid_dataset, valid_labels, train_dataset, train_labels = merge_datasets(
    train_datasets, train_size, image_size, valid_size)
  _, _, test_dataset, test_labels = merge_datasets(test_datasets, test_size, image_size)

  # Print basic information about the data.
  print('Training:', train_dataset.shape, train_labels.shape)
  print('Validation:', valid_dataset.shape, valid_labels.shape)
  print('Testing:', test_dataset.shape, test_labels.shape)

  # Randomize the data for getting better results.
  train_dataset, train_labels = randomize(train_dataset, train_labels)
  test_dataset, test_labels = randomize(test_dataset, test_labels)
  valid_dataset, valid_labels = randomize(valid_dataset, valid_labels)

  pickle_file = subdirectory + 'notMNIST.pickle'  # Pickle target file.

  data_to_pickle(pickle_file, train_dataset, train_labels, valid_dataset,valid_labels,
    test_dataset, test_labels)

  statinfo = os.stat(pickle_file)
  print('Compressed pickle size:', statinfo.st_size)

  # Load pickle file
  # images = pickle.load(open(pickle_file,"rb"))

  # # logreg = LogisticRegression()
  # # logreg.fit(images, images.test_dataset)

if __name__=='__main__':
  main()