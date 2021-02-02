import tensorflow as tf
from sklearn.metrics import confusion_matrix
tf.reset_default_graph()
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
mnist = input_data.read_data_sets("../mnist_data", one_hot=True)
def mnist_train_datasets():
    '''Train image datasets.
        :params train_images: train images data list
        :params train_num: number of train images 
        :params train_labels: train images label list
        :params train_num: number of train images lable
    '''
    train_images = mnist.train.images
    train_labels = mnist.train.labels
    train_data_nums = mnist.train.num_examples 
    train_images_shape = train_images.shape
    train_images_value = train_images[0]
    print("type or image value: {}".format(type(train_images_value)))
    train_value = train_images_value.reshape((28, 28, -1))
    plt.figure()
    plt.imshow(train_value[:,:,0], cmap="Greys_r")
    plt.show()
    train_images_label = train_labels[0]
    
def mnist_test_datasets():
    '''Test image datasets.
        :params test_images: test images data list
        :params test_num: number of test images 
        :params test_labels: test images label list
        :params test_num: number of test images lable
    '''
    test_images = mnist.test.images
    test_labels = mnist.test.labels
    test_data_nums = mnist.test.num_examples
    test_images_shape = test_images.shape
    test_images_value = test_images[0]
    test_images_label = test_labels[0]
    test_value = test_images_value.reshape((28, 28, -1))
    plt.figure()
    plt.imshow(test_value[:,:,0], cmap="Greys_r")
    plt.show()
  
train_label = mnist_train_datasets()
test_label = mnist_test_datasets()
conf_mx = confusion_matrix(train_label, test_label)
plt.figure()
plt.matshow(conf_mx, cmap=plt.cm.gray)
plt.savefig("cofusion_image1.png", format="png")
plt.show() 