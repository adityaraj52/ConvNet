import tensorflow as tf
import pandas as pd
import csv


temparray = []
with open('/Users/adityaraj/Documents/Projects/NeuralNetworkKaggleCompetition/DataSets/training_label.csv') as f:
  reader = csv.reader(f)
  for row in reader:
  	temparray.append(row)
  	print (row)
    # do something here with `row`

tf.decode_csv(temparray, type(temparray), field_delim=',', name=None)