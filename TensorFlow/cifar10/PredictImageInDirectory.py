from Helper import Utils
from array import *
from settings import *
from Helper import *
import pickle
from cifar10_eval_single_directory import PredictImage


class Evaluate_single_image():

    def __init__(self, p_input_directory, p_item):

        self.input_directory = p_input_directory
        self.output_directory = global_path_to_cifar10predictSingleImageBatch
        self.item_name = p_item
        self.output_file_name = "test_batch"

    def create_binary_file(self):
        data = array('B')
        for i in range(1, 128):
            data.append(0)
            image = Utils.load_image(os.path.join(
                self.input_directory, self.item_name))
            image = array('B', image)
            data += image
        output_file = open(self.output_directory +
                           self.output_file_name + '.bin', 'wb')
        data.tofile(output_file)
        output_file.close()

    def get_item_names(self):

        information = global_path_to_other_results + '/train12017-02-02-18:18:34.pickle'

        with open(information, 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            data = pickle.load(f)

        test_images = data['filenames'][20000:]

        return test_images

def main():

    # Predict images in a directory
    # image_input_directory = global_path_to_test_data
    #
    # dirs = os.listdir(image_input_directory)
    # # dirs.sort(key=lambda f: int(filter(str.isdigit, f)))
    # dirs = sorted(dirs,key=lambda x: int(os.path.splitext(x)[0]))
    #
    # with open("test.txt", "w") as myfile:
    #     myfile.write("")
    #
    # for item in dirs:
    #     if(".jpg" in item):
    #         print(item)
    #         with open("test.txt", "a") as myfile:
    #             myfile.write(item[0:len(item)-4] + ",")
    #         print(item)
    #         predict = Evaluate_single_image(image_input_directory, item)
    #         predict.create_binary_file()
    #         p = PredictImage("")
    #         p.evaluate()


    image_input_directory = global_path_to_train_data

    # dirs = os.listdir(image_input_directory)
    # # dirs.sort(key=lambda f: int(filter(str.isdigit, f)))
    # dirs = sorted(dirs,key=lambda x: int(os.path.splitext(x)[0]))

    evaluator = Evaluate_single_image("", "")
    test_images = evaluator.get_item_names()

    with open("test.txt", "w") as myfile:
        myfile.write("")

    for item in test_images:

        item = item + '.jpg'

        # im = Image.open(image_input_directory + '/' + item)
        # im.show()

        with open("test.txt", "a") as myfile:
            myfile.write(item[0:len(item)-4] + ",")

        predict = Evaluate_single_image(image_input_directory, item)
        predict.create_binary_file()
        p = PredictImage("")
        p.evaluate()



if __name__ == '__main__':
    main()


