from keras.models import Sequential
from keras.layers import Dense

model=Sequential()
model.add(Dense(units=256,input_dim=784,
                 kernel_initializer='normal',
                 activation='relu'))
model.add(Dense(units=10, kernel_initializer='normal',
                 activation='softmax'))
print(model.summary())
#损失函数，优化器，评估模型的方式
model.compile(loss='categorical_crossentropy',
              optimizer='adam',metrics=['accuracy'])
train_history =model.fit(x=x_Train_normalize,
                          y=y_Train_OneHot,validation_split=0.2,
                          epochs=10,batch_size=200,verpose=2)















