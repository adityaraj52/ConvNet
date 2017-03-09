import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Stopped at minute 20
# https://www.youtube.com/watch?v=BhpvH5DuVu8&index=3&list=PLSPWNkAMSvv5DKeSVDbEbUKSsK4Z-GgiP

class Sentdex(object):

    def __init__(self):

        mnist = input_data.read_data_sets('/tmp/data/', one_hot=True)

        self.n_nodes_hl1 = 500
        self.n_nodes_hl2 = 500
        self.n_nodes_hl3 = 500

        self.n_classes = 10

        self.x = tf.placeholder('float', [None, 784])
        self.y = tf.placeholder('float')


    def neural_network_model(self, data):

        hidden_1_layer = {'weights':tf.Variable(tf.random_normal([784, self.n_nodes_hl1])),
                          'biases':tf.Variable(tf.random_normal(self.n_nodes_hl1))}


def main():



    # test = Sentdex()
    # test.mnist()

    matrix1 = tf.constant([[2., 3.]])
    x1 = tf.constant(2)
    y = tf.argmax(x1, 1)

    with tf.Session() as sess:
        print(sess.run(y[0]))


if __name__ == '__main__':
    main()

