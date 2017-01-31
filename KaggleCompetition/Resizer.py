from Helper import *
from PIL import Image

# TODO(Sören): Pickle file should be accessed from data_directory
# TODO(Sören): Do resizing only if forced. If files are already there it can be skipped.


class Resizer(object):

    def __init__(self, directory):
        """Name of dataset folder;
        Path to directory containing the data;
        Variable for the list of filenames"""
        self.directory = directory
        self.data_directory = Utils.get_path()
        self.filenames = None

    def get_filenames(self, filename):
        """Get the filenames from the previous pickled information."""

        data = Utils.unpickle_data(filename)
        self.filenames = data['filenames']

    def resize_images(self, source, destination, size=(32, 32)):
        """Resize images within data_directory to a given size."""

        destination = self.data_directory + destination + '/'

        if not os.path.exists(destination):
            os.makedirs(destination)

        for i in self.filenames:
            file = i + '.jpg'
            file_path = self.data_directory + source + '/' + file

            if os.path.exists(file_path):
                img = Image.open(file_path)
                img = img.resize(size)
                img.save(destination + file)

    def get_images(self):
        """Convert images to numpy array and return the resulting array."""

        # TODO(Sören): Remove after testing.
        self.filenames = self.filenames[0:10]

        images = np.zeros(shape=(len(self.filenames), 3072))

        for i in range(0, self.filenames.size):
            path_to_file = os.path.join(self.path, self.filenames[i] + '.jpg')
            image = Utils.load_image(path_to_file)
            images[i] = image

        return images


def main():
    """Resize the original data."""

    data_directory = os.getcwd()

    # Resize the original training images.
    name = 'train1'
    resizer = Resizer(data_directory)
    resizer.get_filenames(name + '.pickle')
    resizer.resize_images(name, 'train3')

    # Display status information
    print(name + ' is done.')

    # Resize the original training images.
    name = 'test1'
    resizer = Resizer(data_directory)
    resizer.get_filenames(name + '.pickle')
    resizer.resize_images(name, 'test3')

    # Display status information
    print(name + ' is done.')

    # test_data_information.get_images()

    # TODO(Sören Schleibaum)
    # - Plot images


if __name__ == "__main__":
    main()

