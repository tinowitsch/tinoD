import tensorflow as tf
import numpy as np

print(tf.math.add(1, 2))
print(tf.math.add([1, 2], [3, 4]))
print(tf.math.square(5))
print(tf.math.reduce_sum([1, 2, 3]))

# Operator overloading is also supported
print(tf.math.square(2) + tf.math.square(3))


myMatrix = np.array([(2,3,4),(2,3,4),(2,3,4)],dtype = 'int32')
myMatrix2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype = 'int32')

print (myMatrix)
print (myMatrix2)

myMatrix = tf.constant(myMatrix)
myMatrix2 = tf.constant(myMatrix2)
matrix_product = tf.matmul(myMatrix, myMatrix2)
matrix_sum = tf.add(myMatrix,myMatrix2)
matrix_3 = np.array([(2,7,2),(1,4,2),(9,0,2)],dtype = 'float32')
print (matrix_3)

with tf.Session() as sess:
   result1 = sess.run(matrix_product)
   result2 = sess.run(matrix_sum)

print (result1)
print (result2)
