# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([[1, 2], [2, 1], [2, 3], [3, 5],[1, 3], [4, 2], [7, 3], [4, 5],  [11, 3], [8, 7]])
y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])
x_test  = np.array([[1, 4],[2, 2],[2, 5],[5, 3],[1, 5],[4, 1]])

a = np.random.normal()
b = np.random.normal()
c = np.random.normal()
error_list = []

# 拟合函数
def h(x):
    return a*x[0] + b*x[1] + c

rate = 0.001  # 学习率
for i in range(8000):
    sum_a = sum_b = sum_c = 0
    for x, y in zip(x_train, y_train):  # 将全部样本代入求梯度
        sum_a = sum_a + rate*(y - h(x))*x[0]
        sum_b = sum_b + rate*(y - h(x))*x[1]
        sum_c = sum_c + rate*(y - h(x))
    a = a+sum_a
    b = b+sum_b
    c = c+sum_c
    plt.plot([h(xi) for xi in x_test])
    error = 0
    for x, y in zip(x_train, y_train):
        error += 0.5*((h(x) - y)**2)
    error_list.append(error)
    if error<0.000001:  # 当误差小于0.00001 即可停止
        break

#print(error_list)
#print(len(error_list))

#print(a)
#print(b)
#print(c)

result = [h(xi) for xi in x_train]
#print(result)
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(y_train,label='标签')
ax2 = fig.add_subplot(122)
ax2.plot(result,label='预测')
plt.legend()
plt.show()