import tensorflow as tf
import numpy as np
import time

starttime = time.time()
print(tf.math.add(1, 2))
print(tf.math.add([1, 2], [3, 4]))
print(tf.math.square(5))
print(tf.math.reduce_sum([1, 2, 3]))

# Operator overloading is also supported
print(tf.math.square(2) + tf.math.square(3))


myMatrix = np.array([(2, 3, 4), (2, 3, 4), (2, 3, 4)], dtype='int32')
myMatrix2 = np.array([(1, 1, 1), (1, 1, 1), (1, 1, 1)], dtype='int32')

print(myMatrix)
print(myMatrix2)

myMatrix = tf.constant(myMatrix)
myMatrix2 = tf.constant(myMatrix2)
matrix_product = tf.matmul(myMatrix, myMatrix2)
matrix_sum = tf.add(myMatrix, myMatrix2)
matrix_3 = np.array([(2, 7, 2), (1, 4, 2), (9, 0, 2)], dtype='float32')
print(matrix_3)

# with tf.Session() as sess:
#   result1 = sess.run(matrix_product)
#   result2 = sess.run(matrix_sum)


def time_matmul(x):
    start = time.time()
    for loop in range(10):
        tf.linalg.matmul(x, x)

    result = time.time()-start

    print("10 loops: {:0.2f}ms".format(1000*result))


# Force execution on CPU
print("On CPU:")
with tf.device("CPU:0"):
    x = tf.random.uniform([1000, 1000])
    assert x.device.endswith("CPU:0")
    time_matmul(x)

# Force execution on GPU #0 if available
if tf.config.list_physical_devices("GPU"):
    print("On GPU:")
    # Or GPU:1 for the 2nd GPU, GPU:2 for the 3rd etc.
    with tf.device("GPU:0"):
        x = tf.random.uniform([1000, 1000])
        assert x.device.endswith("GPU:0")
        time_matmul(x)


# print (result1)
# print (result2)
myruntime = time.time()-starttime
print(myruntime)
print("Runtime: {:0.2f}ms".format(1000*myruntime))
