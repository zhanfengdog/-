import tensorflow as tf
matrix1=tf.constant([[3,3]])
matrix2=tf.constant([[2],[2]])
product=tf.matmul(matrix1,matrix2)
tf.compat.v1.disable_eager_execution()
sess=tf.compat.v1.Session()
result=sess.run(product)
print(result)



#import tensorflow as tf
#tf.compat.v1.disable_eager_execution()
#hello=tf.constant('hello lyd,wokyl')
#sess=tf.compat.v1.Session()
#print(sess.run(hello))