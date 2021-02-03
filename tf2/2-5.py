import tensorflow as tf
import numpy as np
input_xs = np.random.rand(1000)
input_ys = 3 * input_xs + 0.217
weight = tf.Variable(l.,dtype=tf.float32, name="weight")
bias = tf.Variable(l., dtype=tf.float32, name="bias")

def model(xs):

    logits = tf.multiply(xs, weight)+ bias

    return logits

for xs, ys in zip(input_xs, input_ys):
    xs = np.reshape(xs,[1])

    ys = np.reshape(ys,[1])

    with tf.GradientTape() as tape:
        _loss = tf.reduce_mean(tf.powl(model(xs)- ys), 2)/(2 * 1000）
    grads = tape.gradient(_loss,[weight, bias])

    opt.apply_gradients(zip(grads,[weight, bias]))
    print('Training loss is :',_loss.numpy())
print(weight)

print(bias)