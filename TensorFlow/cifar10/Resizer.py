from PIL import Image
from settings import *

class Resizer(object):

    def __init__(self, originDir, destDir, dimensionX, dimensionY):
        self.originDir = originDir
        self.destDir = destDir
        self.dimensionX = dimensionX
        self.dimensionY = dimensionY


    def resize_image(self):
        """Resize all images within a given folder."""

        dirs = os.listdir(self.originDir)
        for item in dirs:

            filename = os.path.join(self.originDir, item)

            if os.path.isfile(filename):

                im = Image.open(filename)
                f, e = os.path.splitext(filename)

                im_resize = im.resize((self.dimensionX, self.dimensionY), Image.ANTIALIAS)
                im_resize.save(self.destDir + f[len(self.originDir):] + '.jpg', 'JPEG', quality=100)

            else:
                print("could not resize")


def main():

    # # Resize train data
    origin_dir = global_path_to_original_train_data
    dest_dir = global_path_to_train_data
    dimension_x = dimension_y = 32

    resizer = Resizer(origin_dir, dest_dir, dimension_x, dimension_y)
    resizer.resize_image()

    # Resize test data
    origin_dir = global_path_to_original_test_data
    dest_dir = global_path_to_test_data
    dimension_x = dimension_y = 32

    resizer = Resizer(origin_dir, dest_dir, dimension_x, dimension_y)
    resizer.resize_image()

if __name__ == "__main__":
    main()

