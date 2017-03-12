from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from Helper import *
from datetime import datetime
import math
import time
import numpy as np
import tensorflow as tf
import cifar10

# Set global variables
from settings import *


class PredictImage():
    def __init__(self, name):

        self.width = 32
        self.height = 32
        self.eval_dir = global_path_to_cifar10_eval_single_directory
        self.eval_data = 'test'
        self.checkpoint_dir = global_path_to_cifar10train100k
        self.eval_interval_secs = 60 * 5
        self.num_examples = 1
        self.run_once = True
        self.batch_size = 1

    def eval_once(self, saver, summary_writer, top_k_op, summary_op, logits):
        """Run Eval once.

        Args:
          saver: Saver.
          summary_writer: Summary writer.
          top_k_op: Top K op.
          summary_op: Summary op.
        """
        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(self.checkpoint_dir)
            if ckpt and ckpt.model_checkpoint_path:
                # Restores from checkpoint
                saver.restore(sess, ckpt.model_checkpoint_path)
                # Assuming model_checkpoint_path looks something like:
                #   /my-favorite-path/cifar10_train/model.ckpt-0,
                # extract global_step from it.
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
            else:
                print('No checkpoint file found')
                return

            # Start the queue runners.
            coord = tf.train.Coordinator()
            try:
                threads = []
                for qr in tf.get_collection(tf.GraphKeys.QUEUE_RUNNERS):
                    threads.extend(qr.create_threads(sess, coord=coord, daemon=True,
                                                     start=True))

                num_iter = int(math.ceil(self.num_examples / self.batch_size))
                true_count = 0  # Counts the number of correct predictions.
                total_sample_count = num_iter * self.batch_size
                step = 0
                while step < num_iter and not coord.should_stop():
                    # predictions = sess.run([top_k_op])
                    # true_count += np.sum(predictions)
                    # step += 1

                    predictions = sess.run([top_k_op])
                    
                    print(sess.run([logits[0]]))
                    # print(sess.run([tf.shape(logits)]))
                    # print(sess.run(tf.argmax(logits[0], 0)))
                    
                    classification = sess.run(tf.argmax(logits[0], 0))
                    cifar10classes = ["0", "1"]

                    f = open(global_path_to_cifar10eval+'workfile', 'w')
                    with open("test.txt", "a") as myfile:
                        myfile.write(cifar10classes[classification])
                        myfile.write("\n")

                    print(cifar10classes[classification])

                    true_count += np.sum(predictions)
                    step += 1

                # Compute precision @ 1.
                precision = true_count / total_sample_count
                print('%s: precision @ 1 = %.3f' % (datetime.now(), precision))

                summary = tf.Summary()
                summary.ParseFromString(sess.run(summary_op))
                summary.value.add(tag='Precision @ 1', simple_value=precision)
                summary_writer.add_summary(summary, global_step)
            except Exception as e:  # pylint: disable=broad-except
                coord.request_stop(e)

            coord.request_stop()
            coord.join(threads, stop_grace_period_secs=10)

    def evaluate(self):
        """Eval CIFAR-10 for a number of steps."""
        with tf.Graph().as_default() as g:
            # Get images and labels for CIFAR-10.
            self.eval_data == 'test'
            images, labels = cifar10.inputs(eval_data=self.eval_data)

            # Build a Graph that computes the logits predictions from the
            # inference model.
            logits = cifar10.inference(images)

            # Calculate predictions.
            top_k_op = tf.nn.in_top_k(logits, labels, 1)

            # Restore the moving average version of the learned variables for eval.
            variable_averages = tf.train.ExponentialMovingAverage(
                cifar10.MOVING_AVERAGE_DECAY)
            variables_to_restore = variable_averages.variables_to_restore()
            saver = tf.train.Saver(variables_to_restore)

            # Build the summary operation based on the TF collection of Summaries.
            summary_op = tf.merge_all_summaries()

            summary_writer = tf.train.SummaryWriter(self.eval_dir, g)

            while True:
                self.eval_once(saver, summary_writer, top_k_op, summary_op, logits)
                if self.run_once:
                    break
                # time.sleep(self.eval_interval_secs)
