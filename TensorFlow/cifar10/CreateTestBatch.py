from array import *
import random
import tarfile
from Helper import *
import pickle

# Set global variables
from settings import *


class Batch(object):

    def __init__(self, image_information, output_file_name, flag,
                 input_directory, output_directory, num_batches,
                 upper_limit_for_batches):

        self.image_information = image_information
        self.output_file_name = output_file_name
        self.p_flag = flag
        self.p_input_directory = input_directory
        self.p_output_directory = output_directory
        self.p_num_batches = num_batches
        self.p_range = upper_limit_for_batches

    def convert_to_binary(self):

        # TODO(Sören Schleibaum): Name resolving is not solved in a nice way.
        image_information = self.image_information + '/train12017-02-02-18:18:34.pickle'

        with open(image_information, 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            data = pickle.load(f)

        filenames = data['filenames']

        # random.shuffle(m_input_directory_files)
        p_lower_limit = 0
        p_upper_limit_for_batches = self.p_range

        if self.p_flag == 1:
            p_lower_limit = 20000
            p_upper_limit_for_batches = p_lower_limit + self.p_range

        for i in range(self.p_num_batches):

            print('Creating a batch from ', p_lower_limit, ' to ', p_upper_limit_for_batches)
            data = self.create_batches(i, filenames, p_lower_limit, p_upper_limit_for_batches)

            # Write data to file
            output_file = open(self.p_output_directory + self.output_file_name + str(i+1) + '.bin', 'wb')
            data.tofile(output_file)
            output_file.close()

            # Increase lower limit on every iteration
            p_lower_limit = p_upper_limit_for_batches
            p_upper_limit_for_batches += self.p_range

    def create_batches(self, index, filenames, p_lower_limit, p_upper_limit_for_batches):

        '''Reinitialising data array everytime we create a new batch'''
        data = array('B')

        # self.output_file_name += str(index + 1)

        if self.p_flag == 0:
            outputfilename = 'data_batch_' + str(index + 1)
        
        elif self.p_flag == 1:
            outputfilename = 'test_batch'

        for item in filenames[p_lower_limit: p_upper_limit_for_batches]:

            # Get label of the image
            if 'cat' in item:
                class_name = 0
            elif 'dog' in item:
                class_name = 1
            data.append(class_name)

            # Grab the image
            item += '.jpg'
            image = Utils.load_image(os.path.join(self.p_input_directory, item))
            image = array('B', image)
            data += image

        return data


def main():

    image_information = global_path_to_other_results
    output_file_name = 'data_batch_'
    flag = 0
    input_directory = global_path_to_train_data
    output_directory = global_path_to_cifar10batches
    num_batches = 5
    upper_limit_for_batches = 4000
    structure = Batch(image_information,
                        output_file_name,
                        flag,
                        input_directory,
                        output_directory,
                        num_batches,
                        upper_limit_for_batches)

    # Create Training Batches
    #structure.convert_to_binary()


    image_information = global_path_to_other_results
    output_file_name = 'test_batch'
    # Flag 1 means that the lower limit is fixed
    flag = 1
    input_directory = global_path_to_train_data
    output_directory = global_path_to_cifar10batches
    num_batches = 1
    upper_limit_for_batches = 5000
    structure = Batch(image_information,
                        output_file_name,
                        flag,
                        input_directory,
                        output_directory,
                        num_batches,
                        upper_limit_for_batches)

    # Create Test Batches
    structure.convert_to_binary()

    # Create Tar File File of the directory
    with open(output_directory + '/' + 'batches_meta.txt', 'w+') as the_file:
        the_file.write('cat\ndog')

    with tarfile.open(output_directory + '/' + '../cifar-10-binary.tar.gz', mode='w:gz') as archive:
        archive.add(global_path_to_cifar10data + '/', recursive=True)

if __name__ == '__main__':
    main()

