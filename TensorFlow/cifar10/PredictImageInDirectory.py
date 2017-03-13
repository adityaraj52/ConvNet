from Helper import Utils
from array import *
from settings import *
import random
from Helper import *
from os import listdir
from cifar10_eval_single_directory import PredictImage


class evalaute_single_image():
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


image_input_directory = global_path_to_test_data


dirs = os.listdir(image_input_directory)
# dirs.sort(key=lambda f: int(filter(str.isdigit, f)))
dirs = sorted(dirs,key=lambda x: int(os.path.splitext(x)[0]))

with open("test.txt", "w") as myfile:
    myfile.write("")

for item in dirs:
    if(".jpg" in item):
        print(item)
        with open("test.txt", "a") as myfile:
            myfile.write(item[0:len(item)-4] + ",")
        print(item)
        predict = evalaute_single_image(image_input_directory, item)
        predict.create_binary_file()
        p = PredictImage("")
        p.evaluate()
