import numpy as np
import matplotlib as plt
import matplotlib.pyplot as ply
import pandas as pd
from keras.utils import np_utils
from s1 import plot_image
from s602 import plot_images_labels_prediction
np.random.seed(10)
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense

(x_train_image,y_train_label),\
(x_test_image,y_test_label)=mnist.load_data()
#print('train data=',len(x_train_image))
#print('test data=',len(x_test_image))
#print('x_train_image:',x_train_image.shape)
#print('y_train_label:',y_train_label.shape)
#plot_image(x_train_image[0])
#plot_images_labels_prediction(x_train_image,y_train_label,
                            #  [],0,10)
#print('x_test_image:',x_test_image.shape)
#print('y_test_label:',y_test_label.shape)
#plot_images_labels_prediction(x_test_image,y_test_label,[],0,10)
x_Train=x_train_image.reshape(60000,784).astype('float32')
x_Test=x_test_image.reshape(10000,784).astype('float32')
#print('x_train:',x_Train.shape)
#print('x_test:',x_Test.shape)
#print(x_train_image[0]) 数字代表深浅
x_Train_normalize=x_Train/255
x_Test_normalize=x_Test/255
#print(x_Train_normalize)
#print(x_Test_normalize)

#print(y_train_label[0:5])
y_TrainOneHot=np_utils.to_categorical(y_train_label)
y_TestOneHot=np_utils.to_categorical(y_test_label)
#print(y_TrainOneHot[0:5])


model=Sequential()
model.add(Dense(units=256,input_dim=784,
                 kernel_initializer='normal',
                 activation='relu'))
model.add(Dense(units=10, kernel_initializer='normal',
                 activation='softmax'))
#print(model.summary())
#损失函数，优化器，评估模型的方式
model.compile(loss='categorical_crossentropy',
              optimizer='adam',metrics=['accuracy'])
train_history=model.fit(x=x_Train_normalize,
                          y=y_TrainOneHot,validation_split=0.2,
                          epochs=10,batch_size=200,verbose=2)

def show_train_history(train_history,train,validation):
    ply.plot(train_history.history[train])
    ply.plot(train_history.history[validation])
    ply.title('Train history')
    ply.ylabel(train)
    ply.xlabel('Epoch')
    ply.legend(['train','validation'], loc='upper left')
    ply.show()

#show_train_history(train_history,'accuracy','val_accuracy')
#show_train_history(train_history, 'loss', 'val_loss')
score=model.evaluate(x_Test_normalize,y_TestOneHot)

#print('accuracy=',score[1])#显示准确率
prediction=model.predict_classes(x_Test)#进行预测
#print(prediction)
#plot_images_labels_prediction(x_test_image,y_test_label,
 #                             prediction,idx=340)
pd.crosstab(y_test_label,prediction,
            rownames=['label'],colnames=['prediction'])
df=pd.DataFrame({'label':y_test_label,'predict':prediction})
print(df[0:2])
tgg=df[(df.label==5)&(df.predict==3)]#真实是5，测试是3
print(tgg)