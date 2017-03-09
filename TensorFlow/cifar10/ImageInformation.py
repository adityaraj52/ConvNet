from Helper import *
from PIL import Image
import csv
import random
import pickle

# Set global variables
from settings import *


# TODO(Sören): Pickle file should also be saved in data_directory


class ImageInformation(object):

    def __init__(self, data_path, result_path, dataset_name):
        """Name of dataset folder;
        path for the data directory;
        filenames for names of files;
        sizes for height and weight of the files"""
        self.dataset_name = dataset_name
        self.filenames = None
        self.images = None
        self.labels = None
        self.data_path = data_path
        self.result_path = result_path
        self.sizes = None
        self.dict = {}

    def get_file_names(self, testing=False):
        """Gets all filenames from the path variable and saves it within filenames."""
        filenames = deque()

        names = os.listdir(self.data_path)
        size = len(names)

        if testing:
            size = 10

        for i in range(0, size):
            if names[i].endswith('.jpg'):
                filenames.append(names[i][:-4])
            else:
                continue

        filenames = ListUtils().deque_to_numpy_array(filenames)
        # Shuffle the filenames
        random.shuffle(filenames)

        return filenames

    def get_dimensions(self):
        """Get the dimensions (width and height) of all images and save the
        result within sizes."""

        sizes = np.zeros(shape=(len(self.filenames), 4))

        for i in range(0, self.filenames.size):

            path_to_file = self.data_path + '/' + self.filenames[i] + '.jpg'

            size_in_bytes = os.stat(path_to_file).st_size

            im = Image.open(path_to_file)
            sizes[i, 0] = im.height
            sizes[i, 1] = im.width
            sizes[i, 2] = im.width/im.height
            sizes[i, 3] = size_in_bytes

        return sizes

    def get_labels(self):
        """Get the labels of the files. Marked as 0 if cat and as 1 if dog."""

        filenames = self.filenames
        labels = np.zeros(shape=(len(filenames), 1))

        for i in range(0, len(filenames)):
            if filenames[i].startswith('cat'):
                labels[i] = 0
            elif filenames[i].startswith('dog'):
                labels[i] = 1

        return labels

    def write_data_to_csv_file(self):
        """Write the data to a .csv file"""

        filename = self.result_path + '/' + self.dataset_name + Utils.get_current_date() + '.csv'

        with open(filename, 'w') as csvfile:
            fieldnames = ['index','filename', 'label', 'height', 'width', 'ratio', 'size']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for i in range(len(self.filenames)):
                writer.writerow({'index': i+1,
                                 'filename': self.filenames[i],
                                 'label': self.labels[i, 0],
                                 'height': self.sizes[i, 0],
                                 'width': self.sizes[i, 1],
                                 'ratio': self.sizes[i, 2].round(4),
                                 'size': self.sizes[i, 3]})

    def create_dictionary(self):
        """Create a dictionary which shall be pickled later."""

        data_as_dict = {'data': self.images,
                        'labels': self.labels,
                        'filenames': self.filenames,
                        'heigth': self.sizes[:, 0],
                        'width': self.sizes[:, 1],
                        'ratio': self.sizes[:, 2],
                        'size': self.sizes[:, 3]}

        return data_as_dict

    def pickle_information(self):

        with open(self.result_path + '/' + self.dataset_name + Utils.get_current_date() + '.pickle', 'wb') as f:
            pickle.dump(self.dict, f, pickle.HIGHEST_PROTOCOL)

    def plot_information(self):
        """Plot the information."""
        pass

    def get_information(self, testing=False):
        """Get all important information from the data."""

        # Get necessary information
        self.filenames = self.get_file_names(testing)
        self.sizes = self.get_dimensions()
        self.labels = self.get_labels()
        self.dict = self.create_dictionary()

        # Save the information
        self.save_information()

    def save_information(self):

        self.write_data_to_csv_file()
        self.pickle_information()


def main():
    """Get the image information of the original data"""

    """Get information about the original train data."""
    # Get the directory
    name = 'train1'
    data_directory = global_path_to_original_train_data
    result_directory = global_path_to_other_results

    # Get connected information
    data = ImageInformation(data_directory, result_directory, name)
    data.get_information()

    # Display status information
    print(name + ' is done.')

    """Get information about the original test data."""
    # Get the directory
    name = 'test1'
    data_directory = global_path_to_original_test_data
    result_directory = global_path_to_other_results

    # Get connected information
    data = ImageInformation(data_directory, result_directory, name)
    data.get_information(data_directory)

    # Display status information
    print(name + ' is done.')

if __name__ == "__main__":
    main()

