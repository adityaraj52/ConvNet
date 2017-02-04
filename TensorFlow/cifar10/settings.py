import os
from Helper import Utils

'''Be aware that a change of this file might affect several other files.'''

# Data directories
global_path_to_original_train_data = '../../Resources/TrainingDataSets/train1'
global_path_to_original_test_data = '../../Resources/TrainingDataSets/test1'
global_path_to_train_data = '../../Resources/TrainingDataSets/train2'
global_path_to_test_data = '../../Resources/TrainingDataSets/test2'

# Result directories
global_path_to_other_results = '../../Resources/OtherResults'
global_path_to_cifar10data = '../../Resources/TensorFlowFiles/cifar10_data'
global_path_to_cifar10eval = '../../Resources/TensorFlowFiles/cifar10_eval'
global_path_to_cifar10train = '../../Resources/TensorFlowFiles/cifar10_train'
global_path_to_cifar10batches = '../../Resources/TensorFlowFiles/cifar10_data/cifar-10-batches-bin/'

# TODO(Sören Schleibaum): Has to be removed.
global_output_test = '../../Resources/TensorFlowFiles/cifar10_data/test'

# Warn if directories are not there
# TODO

# Create missing directories
Utils.create_directory(global_path_to_other_results)
Utils.create_directory(global_path_to_cifar10batches)
Utils.create_directory(global_path_to_train_data)
Utils.create_directory(global_path_to_test_data)
Utils.check_directory(global_path_to_original_train_data)

# Uncomment to check if the directories exist
# print(os.path.exists(global_path_to_original_train_data))
# print(os.path.exists(global_path_to_original_test_data))
# print(os.path.exists(global_path_to_train_data))
# print(os.path.exists(global_path_to_test_data))
# print(os.path.exists(global_path_to_cifar10data))
# print(os.path.exists(global_path_to_cifar10eval))
# print(os.path.exists(global_path_to_cifar10train))
