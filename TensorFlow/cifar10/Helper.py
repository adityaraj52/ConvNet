from collections import deque
import numpy as np
import os
from PIL import Image
import pickle
import datetime


###################################################################################
class ListUtils(object):

    @staticmethod
    def deque_to_ndarray(deque):

        deque_length = len(deque)

        result = np.ndarray(shape=(deque_length, 1))

        for i in range(0, deque_length):
            result[i] = deque.pop()

        return result

    @staticmethod
    def deque_to_numpy_array(deque):

        result = np.array(deque)

        return result

    @staticmethod
    def display_deque(deque):
        for i in deque:
            print(i)


###################################################################################
class Utils():

    @staticmethod
    def get_path(data=''):

        current_directory = os.getcwd()
        data_directory = current_directory + '/Resources/DataSets/' + data

        return data_directory

    @staticmethod
    def get_parent_directory():

        current_directory = os.getcwd()
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

        return parent_directory

    @staticmethod
    def load_image(infilename):
        """Grap the image and convert it to the needed structure."""

        data = Image.open(infilename)
        image = np.asarray(data, dtype="uint8")

        # Reformat the image so that using a for loop
        # would go over col, x, y.
        image = image.ravel('F').tolist()

        return image

    @staticmethod
    def unpickle_data(filename):

        with open(filename, 'rb') as f:
            data = pickle.load(f)

        return data

    @staticmethod
    def create_directory(directory):
        """Creates directory if it is not already there."""
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def check_directory(directory):
        """Raises an exception if directory is not there. This might
        be helpful if it is the input directory for data and
        necessary for the following executions."""

        message = 'Necessary directory was not found. Please check your ' \
                  'path.'

        if not os.path.exists(directory):
            raise SystemExit(message)

    @staticmethod
    def get_current_date():
        """Returns a string which holds a manipulated from of the
        current date and time."""

        now = datetime.datetime.now()

        # Prettify the string
        now = str(now).replace(' ', '-')
        now = now[:-7]

        return now

    # @staticmethod
    # def display_image(path_to_image):


