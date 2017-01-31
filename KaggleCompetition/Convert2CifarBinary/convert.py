import os
from PIL import Image
from array import *
import random
import tarfile


def conver_to_binary(p_flag,
                     p_input_directory,
                     p_output_directory,
                     p_num_batches,
                     p_upper_limit_for_batches):

    data = array('B')
    m_input_directory_files = os.listdir(p_input_directory)
    random.shuffle(m_input_directory_files)
    p_lower_limit = 0
    p_range = p_upper_limit_for_batches


    for i in range(p_num_batches):

        if (p_flag == 0):
            outputfilename = "data_batch_" + str(i+1)

        elif (p_flag == 1):
            outputfilename = "test_batch"

#         if p_flag == 0:
#             outputfilename = "training_batch_" + str(i + 1)
#
#         elif p_flag == 1:
#             outputfilename = "testing_batch"

        for item in m_input_directory_files[p_lower_limit: p_upper_limit_for_batches]:
            if item.endswith('.jpg'):

                # grab the image
                im = Image.open(os.path.join(p_input_directory, item))
                pix = im.load()

                # print(os.path.join(p_input_directory, item))

                # store the class name from look at path
                if ("cat" in item):
                    class_name = 0
                elif ("dog" in item):
                    class_name = 1
                else:
                    print("Incorrect Label")

                # get image into byte array#
                # create array of bytes to hold stuff
                # first append the class_name byte

                data.append(class_name)

                # then write the rows
                # Extract RGB from pixels and append

                for color in range(0, 3):
                    for x in range(0, 32):
                        for y in range(0, 32):
                            data.append(pix[x, y][color])
                            print(type(pix[x, y][color]))

                output_file = open(p_output_directory + outputfilename + ".bin", 'wb')
                data.tofile(output_file)
                output_file.close()

                ############################################
                # Increase lower limit on every iteration#
                ############################################
        p_lower_limit = p_upper_limit_for_batches
        p_upper_limit_for_batches += p_range
        print("Created a batch from ",p_lower_limit," to ", p_upper_limit_for_batches)


############################################
# Default Input and output directory for the project  #
############################################

input_dir = "../Resources/DataSets/train2"
output_dir = "../Resources/BatchFiles/cifar-10-batches-bin/"


############################################
# Create a directory if it does not exist  #
############################################
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

############################################
# Constants for taking number of batches for training 
# and maximum number of elements in a batch
############################################

num_batch = 5
p_upper_limit_for_batches = 1000

############################################
# Create Training Batches #
############################################
conver_to_binary(0, input_dir, output_dir, num_batch, p_upper_limit_for_batches)


############################################
# Create Testing Batches #
############################################
conver_to_binary(1, input_dir, output_dir, 1, p_upper_limit_for_batches)

############################################
# Create Tar File File of the directory #
############################################
with open(output_dir + "batches_meta.txt", 'w+') as the_file:
    the_file.write('cat\ndog')

with tarfile.open(output_dir + '../cifar-10-binary.tar.gz', mode='w:gz') as archive:
    archive.add('../Resources/BatchFiles/cifar-10-batches-py/', recursive=True)

