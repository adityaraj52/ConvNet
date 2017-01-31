# Dogs vs. Cats competition

This repository contains code on which the submissions to the competition 'Dogs vs. Cats' hosted by Kaggle are based. The competition is available under [this page](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition). 
The project is part of the course 'Neural nets with statistical learning' of the [TU Clausthal](http://www.tu-clausthal.de/). To fulfil the task a neural network is used.
The language mainly used to complete the task is [Python 3](https://docs.python.org/3/).

## Folder structure

* Communication 
  * Contains all communication to Mrs. Pazouki.

* Image Manipulation
  * Work on preprocessing images before inserting them into a neural net.
  * Run the image Processing methods using follwoing commands on terminal or command line:
    * Prerequisites: Python
    * Install Python
    * Run: from Terminal(Linux Systems) or CommandPrompt(Windows)
    * python Image_manipulation_Methods.py
    
* Information
  * Useful links, such as tutorials and code examples, are stored within here.

* Kaggle Competition
  * The actual code for submits to the competition is based here.

* Simple Neural Network Example
  * A small example of a neural network is based here. It is based on [this code](http://iamtrask.github.io/2015/07/12/basic-python-network/).

* Udacity Tutorial
  * This code and documents are used to understand how neural networks are able to deal with images. It is based on [this code](https://www.udacity.com/course/deep-learning--ud730).
  * The source code files are of three types: **.ipynb**, **.py**, **.html**. 
    * **.ipynb** is the source file for a [Jupyter notebook]{http://jupyter.org/}.
    * **.py** contains modules and pure Python code.
    * **.html** is a html version of a Jupyter notebook which is accessible without installing Jupyter or Python at all.  

* Resources
  * This folder holds all the training files and Tensorflow files required for checkpointing and evaluation
    The folder has to be arranged in the following structure

    * This folder will hold all the Batchfiles generated from Training data sets and also the training data summary
    Useful for evaluation purposes
        * ConvNet/Resources
                            /BatchFiles
                            /EvaluationFiles

    * This folder will hold the raw images of training data sets.

        * Note: This data has to be converted into Cifar10 data format using the function Cifar10CreateData.py in 
        ConvNet/Resources/TensorFlowFiles/Cifar10 directory.
                          
        * ConvNet/Resources/TrainingDataSets/train23

