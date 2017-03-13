from Helper import Utils
from array import *
from settings import global_path_to_cifar10batches
from settings import global_path_to_test_data
from settings import *
import random
from Helper import *
from os import listdir
from Predict_cifar_images import Predicter

class evalaute_single_image():
    def __init__(self, p_input_directory, p_item):

        self.input_directory = p_input_directory
        self.output_directory = global_path_to_cifar10batches
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

class predict_files():
    
    def __init__(self):
        pass

    ###################################################################################
    # For predicting images in a directory. Here we are predicting from test directory
    # Feel free to modify input directory
    ###################################################################################

    def evaluate_directory_of_images(self):
        
        #Provide the input directory here:
        image_input_directory = global_path_to_test_data
        
        dirs = os.listdir(image_input_directory)
        dirs = sorted(dirs,key=lambda x: int(os.path.splitext(x)[0]))
        save_to_file = "../../Resources/EvaluateImageResults/test_images.txt"

        with open(save_to_file, "w") as myfile:
            myfile.write("")

        for item in dirs:
            if(".jpg" in item):
                
                with open(save_to_file, "a") as myfile:
                    myfile.write(item[0:len(item)-4] + ",")
                
                predict = evalaute_single_image(image_input_directory, item)
                predict.create_binary_file()
                p = Predicter(save_to_file)
                p.evaluate()
    
    ################################################################################
    # For predicting a single image
    ################################################################################
    
    def evaluate_single_image(self):
        #Provide the image input directory here:
        image_input_directory = ""
        image_name = ""
        

        predict = evalaute_single_image(image_input_directory, image_name)
        predict.create_binary_file()
        p = Predicter("abc")
        p.evaluate()
    
    ################################################################################
    # For predicting test_batch.bin which is last 20% evaluation images from pickle 
    # file
    ################################################################################

    def evaluate_test_batch_image(self):
        image_input_directory = global_path_to_train_data
        evaluator = evalaute_single_image("", "")
        test_images = evaluator.get_item_names()
        save_to_file = "../../Resources/EvaluateImageResults/test_batch.txt"

        with open(save_to_file, "w") as myfile:
            myfile.write("")

        for item in test_images:
                item = item + '_resized' + '.jpg'
                
                if "cat" in item:
                    class_name = 0
                elif "dog" in item:
                    class_name = 1
                else:
                    class_name = 2

                with open(save_to_file, "a") as myfile:
                    myfile.write(item[0:len(item)-4] + "," + str(class_name) + ',')
                
                predict = evalaute_single_image(image_input_directory, item)
                predict.create_binary_file()
                p = Predicter(save_to_file)
                p.evaluate()

################################################################################
# main function
################################################################################

def main():
    predict_file = predict_files();

    predict_file.evaluate_directory_of_images();
    #predict_file.evaluate_test_batch_image();

if __name__ == '__main__':
    main()