from settings import *
from Helper import Utils
import pickle
from PIL import Image


class Test(object):

    def __init__(self):
        pass

    def date(self):

        now = Utils().get_current_date()
        print(now)

    def visualize_images(self):

        image_information = global_path_to_other_results + '/train12017-02-02-18:18:34.pickle'

        with open(image_information, 'rb') as f:
            data = pickle.load(f)

        filenames = data['filenames']

        path = global_path_to_original_train_data

        for i in range(0, 150):
            path_to_file = path + '/' + filenames[i] + '.jpg'
            if os.path.exists(path_to_file):
                im = Image.open(path_to_file)
                im.show()
                print(path_to_file)

def main():

    test = Test()
    test.visualize_images()


if __name__ == "__main__":
    main()

