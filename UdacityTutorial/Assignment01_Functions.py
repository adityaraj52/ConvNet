from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
from IPython.display import display, Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle

# %matplotlib inLine
global last_percent_reported
global subdirectory

def set_global_variables(a, b):
  """ TODO: check what is a better solution. """

  global last_percent_reported
  global subdirectory

  last_percent_reported = a
  subdirectory = b


def download_progress_hook(count, blockSize, totalSize):
  """A hook to report the progress of a download. This is mostly intended for users with
  slow internet connections. Reports every 1% change in download progress.
  """

  global last_percent_reported
  # last_percent_reported = None
  percent = int(count * blockSize * 100 / totalSize)

  if last_percent_reported != percent:
    if percent % 5 == 0:
      sys.stdout.write("%s%%" % percent)
      sys.stdout.flush()
    else:
      sys.stdout.write(".")
      sys.stdout.flush()
      
    last_percent_reported = percent
        
def maybe_download(filename, expected_bytes, url, force=False):
  """Download a file if not present, and make sure it's the right size."""
  
  global subdirectory

  directory_of_file = subdirectory + filename

  if force or not os.path.exists(directory_of_file):
    print('Attempting to download:', filename) 
    filename, _ = urlretrieve(url + filename, './data/' + filename, reporthook=download_progress_hook)
    print('\nDownload Complete!')
  statinfo = os.stat(directory_of_file)
  if statinfo.st_size == expected_bytes:
    print('Found and verified', filename)
  else:
    raise Exception(
      'Failed to verify ' + filename + '. Can you get to it with a browser?')
  return filename

def maybe_extract(filename, num_classes, force=False):
  """ Extract downloaded data if not happened already. """

  global subdirectory

  root = os.path.splitext(os.path.splitext(filename)[0])[0]  # remove .tar.gz

  if os.path.isdir(subdirectory + root) and not force:
    # You may override by setting force=True.
    print('%s already present - Skipping extraction of %s.' % (root, filename))
  else:
    print('Extracting data for %s. This may take a while. Please wait.' % root)
    tar = tarfile.open(subdirectory + filename)
    sys.stdout.flush()
    tar.extractall(path=subdirectory)
    tar.close()
  data_folders = [
    os.path.join(subdirectory + root, d) for d in sorted(os.listdir(subdirectory + root))
    if os.path.isdir(os.path.join(subdirectory + root, d))]
  if len(data_folders) != num_classes:
    raise Exception(
      'Expected %d folders, one per class. Found %d instead.' % (
        num_classes, len(data_folders)))
  return data_folders

def load_letter(folder, min_num_images, image_size, pixel_depth):
  """Load the data for a single letter label."""

  image_files = os.listdir(folder)
  dataset = np.ndarray(shape=(len(image_files), image_size, image_size),
                         dtype=np.float32)
  print(folder)
  num_images = 0
  for image in image_files:
    image_file = os.path.join(folder, image)
    try:
      image_data = (ndimage.imread(image_file).astype(float) - 
                    pixel_depth / 2) / pixel_depth
      if image_data.shape != (image_size, image_size):
        raise Exception('Unexpected image shape: %s' % str(image_data.shape))
      dataset[num_images, :, :] = image_data
      num_images = num_images + 1
    except IOError as e:
      print('Could not read:', image_file, ':', e, '- it\'s ok, skipping.')
    
  dataset = dataset[0:num_images, :, :]
  if num_images < min_num_images:
    raise Exception('Many fewer images than expected: %d < %d' %
                    (num_images, min_num_images))
    
  print('Full dataset tensor:', dataset.shape)
  print('Mean:', np.mean(dataset))
  print('Standard deviation:', np.std(dataset))
  return dataset
  

def maybe_pickle(data_folders, min_num_images_per_class, image_size, pixel_depth, force=False):
  """ Create pickle-files for each subdirectory of a given data_folder and save them within 
  the folder. """

  dataset_names = []
  for folder in data_folders:
    set_filename = folder + '.pickle'
    dataset_names.append(set_filename)
    if os.path.exists(set_filename) and not force:
      # You may override by setting force=True.
      print('%s already present - Skipping pickling.' % set_filename)
    else:
      print('Pickling %s.' % set_filename)
      dataset = load_letter(folder, min_num_images_per_class, image_size, pixel_depth)
      try:
        with open(set_filename, 'wb') as f:
          pickle.dump(dataset, f, pickle.HIGHEST_PROTOCOL)
      except Exception as e:
        print('Unable to save data to', set_filename, ':', e)
  
  return dataset_names


def make_arrays(nb_rows, img_size):
  """ """

  if nb_rows:
    dataset = np.ndarray((nb_rows, img_size, img_size), dtype=np.float32)
    labels = np.ndarray(nb_rows, dtype=np.int32)
  else:
    dataset, labels = None, None
  return dataset, labels


def merge_datasets(pickle_files, train_size, image_size, valid_size=0):
  """ Merges pickle-files. """

  num_classes = len(pickle_files)
  valid_dataset, valid_labels = make_arrays(valid_size, image_size)
  train_dataset, train_labels = make_arrays(train_size, image_size)
  vsize_per_class = valid_size // num_classes
  tsize_per_class = train_size // num_classes
    
  start_v, start_t = 0, 0
  end_v, end_t = vsize_per_class, tsize_per_class
  end_l = vsize_per_class+tsize_per_class
  for label, pickle_file in enumerate(pickle_files):       
    try:
      with open(pickle_file, 'rb') as f:
        letter_set = pickle.load(f)
        # let's shuffle the letters to have random validation and training set
        np.random.shuffle(letter_set)
        if valid_dataset is not None:
          valid_letter = letter_set[:vsize_per_class, :, :]
          valid_dataset[start_v:end_v, :, :] = valid_letter
          valid_labels[start_v:end_v] = label
          start_v += vsize_per_class
          end_v += vsize_per_class
                    
        train_letter = letter_set[vsize_per_class:end_l, :, :]
        train_dataset[start_t:end_t, :, :] = train_letter
        train_labels[start_t:end_t] = label
        start_t += tsize_per_class
        end_t += tsize_per_class
    except Exception as e:
      print('Unable to process data from', pickle_file, ':', e)
      raise

  return valid_dataset, valid_labels, train_dataset, train_labels


def randomize(dataset, labels):
  """ """

  permutation = np.random.permutation(labels.shape[0])
  shuffled_dataset = dataset[permutation,:,:]
  shuffled_labels = labels[permutation]
  return shuffled_dataset, shuffled_labels

def data_to_pickle(file, train_dataset, train_labels, valid_dataset,valid_labels,
    test_dataset, test_labels, force=False):
  """ Combine all pickle-files to one large pickle if that has not already happened."""

  if not os.path.isfile(file) or force:
    try:
      f = open(file, 'wb')
      save = {
        'train_dataset': train_dataset,
        'train_labels': train_labels,
        'valid_dataset': valid_dataset,
        'valid_labels': valid_labels,
        'test_dataset': test_dataset,
        'test_labels': test_labels,
        }
      pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
      f.close()
    except Exception as e:
      print('Unable to save data to', file, ':', e)
      raise
  else:
    print('Pickle is already done.')


# def main():

#   # Variable initialization
#   global last_percent_reported
#   global subdirectory

#   # Variable declaration
#   url = 'http://commondatastorage.googleapis.com/books1000/'
#   last_percent_reported = None
#   subdirectory = './data/'
  
#   # Download the data set.
#   train_filename = maybe_download('notMNIST_large.tar.gz', 247336696, url)
#   test_filename = maybe_download('notMNIST_small.tar.gz', 8458043, url)

#   num_classes = 10          # Number of folders
#   np.random.seed(133)       # Makes the random numbers predictable

#   # Extract the downloaded .gz-files.
#   train_folders = maybe_extract("notMNIST_large.tar.gz", num_classes)
#   test_folders = maybe_extract("notMNIST_small.tar.gz", num_classes)

#   # # TODO
#   # # Display images
#   # # Image(filename='./notMNIST_small/A/MDEtMDEtMDAudHRm.png')
#   # # local_file = FileLink("/notMNIST_small/A/MDEtMDEtMDAudHRm.png")
#   # # display(local_file)

#   image_size = 28           # Pixel width and height.
#   pixel_depth = 255.0       # Number of levels per pixel.

#   # 
#   train_datasets = maybe_pickle(train_folders, 45000, image_size, pixel_depth)
#   test_datasets = maybe_pickle(test_folders, 1800, image_size, pixel_depth)

#   # Define framework data.
#   train_size = 200000
#   valid_size = 10000
#   test_size = 10000

#   # Merge the small pickle files of training and testing data to one large each. 
#   valid_dataset, valid_labels, train_dataset, train_labels = merge_datasets(
#     train_datasets, train_size, image_size, valid_size)
#   _, _, test_dataset, test_labels = merge_datasets(test_datasets, test_size, image_size)

#   # Print basic information about the data.
#   print('Training:', train_dataset.shape, train_labels.shape)
#   print('Validation:', valid_dataset.shape, valid_labels.shape)
#   print('Testing:', test_dataset.shape, test_labels.shape)

#   # Randomize the data for getting better results.
#   train_dataset, train_labels = randomize(train_dataset, train_labels)
#   test_dataset, test_labels = randomize(test_dataset, test_labels)
#   valid_dataset, valid_labels = randomize(valid_dataset, valid_labels)

#   pickle_file = subdirectory + 'notMNIST.pickle'  # Pickle target file.

#   data_to_pickle(pickle_file, train_dataset, train_labels, valid_dataset,valid_labels,
#     test_dataset, test_labels)

#   statinfo = os.stat(pickle_file)
#   print('Compressed pickle size:', statinfo.st_size)

#   # Load pickle file
#   # images = pickle.load(open(pickle_file,"rb"))

#   # # logreg = LogisticRegression()
#   # # logreg.fit(images, images.test_dataset)

# if __name__=='__main__':
#   main()