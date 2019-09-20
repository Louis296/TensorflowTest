import tensorflow as tf
import os

#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

greeting = tf.constant('Hello Google Tensorflow!')
sess = tf.compat.v1.Session()
result = sess.run(greeting)
print(result)
sess.close()
