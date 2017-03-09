import tensorflow as tf

filename_queue = tf.train.string_input_producer(["../../DataSets/training_label.csv"])
print(filename_queue)

reader = tf.TextLineReader()
value = reader.read(filename_queue)

print(value)

# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
record_default = [[4], [2], [2]]

col1, col2, col3 = tf.decode_csv(value, record_defaults=record_default)


with tf.Session() as sess:
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)

  for i in range(1200):
    # Retrieve a single instance:
    example, label = sess.run([col3])

  coord.request_stop()
  coord.join(threads)