import os
import numpy as np
import time

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical

mnist = tf.keras.datasets.mnist

(train_images,train_labels),(test_images,test_labels) = mnist.load_data()
train_images=train_images.astype('float32')/255
test_images=test_images.astype('float32')/255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = tf.keras.models.Sequential()
model.add(layers.LSTM(128,input_shape=train_images.shape[1:]))
model.add(layers.Dense(10,activation='softmax'))

model.compile(optimizer = 'rmsprop',
             loss = 'categorical_crossentropy',
             metrics = ['accuracy'])

print("Start Learning with tensorflow.keras")

start = time.time()

model.fit(train_images,train_labels,epochs=5,batch_size=128)

print("Ran in {} seconds".format(time.time() - start))

test_loss, test_acc = model.evaluate(test_images,test_labels)

print('test_acc:',test_acc)