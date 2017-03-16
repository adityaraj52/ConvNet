from PIL import Image

# Set global variables
from settings import *

class Resizer(object):

    def __init__(self, origin_dir, dest_dir, dimension_x, dimension_y):
        self.origin_dir = origin_dir
        self.dest_dir = dest_dir
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y


    def resize_image(self):
        """Resize all images within a given folder."""

        ################################################
        # For Mac we need to delete deafult 'DS_Store' file
        deletefile = os.path.join(self.origin_dir, ".DS_Store")
        if(os.path.isfile(deletefile)):
            os.remove(deletefile)

        dirs = os.listdir(self.origin_dir)
        for item in dirs:

            filename = os.path.join(self.origin_dir, item)

            if os.path.isfile(filename):

                print(filename)

                im = Image.open(filename)
                f, e = os.path.splitext(filename)

                im_resize = im.resize((self.dimension_x, self.dimension_y), Image.ANTIALIAS)
                im_resize.save(self.dest_dir + f[len(self.origin_dir):] + '.jpg', 'JPEG', quality=100)

            else:
                print("could not resize")


def main():

    # #Resize train data
    # Utils.check_directory(global_path_to_original_train_data)
    # origin_dir = global_path_to_original_train_data
    # dest_dir = global_path_to_train_data
    # dimension_x = dimension_y = 32

    # resizer = Resizer(origin_dir, dest_dir, dimension_x, dimension_y)
    # resizer.resize_image()

    # # Resize test data
    # Utils.check_directory(global_path_to_original_test_data)
    # origin_dir = global_path_to_original_test_data
    # dest_dir = global_path_to_test_data
    # dimension_x = dimension_y = 32

    # resizer = Resizer(origin_dir, dest_dir, dimension_x, dimension_y)
    # resizer.resize_image()

    # Resize random images data
    Utils.check_directory(global_path_to_original_random_images)
    origin_dir = global_path_to_original_random_images
    dest_dir = global_path_to_random_images
    dimension_x = dimension_y = 32

    resizer = Resizer(origin_dir, dest_dir, dimension_x, dimension_y)
    resizer.resize_image()

if __name__ == "__main__":
    main()

