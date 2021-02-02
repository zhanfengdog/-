import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

# 真实函数
def real_func(x):
    return np.sin(2*np.pi*x)

# 拟合函数
def fit_func(p, x):
    f = np.poly1d(p)  # polyid是多项式函数，p决定了多项式的次数
    return f(x)

# 误差函数
def residuals_func(p, y, x):
    ret = fit_func(p,x) - y
    return ret

np.random.seed(0)   # 随机数种子
x = np.linspace(0,2,20)
x_points = np.linspace(0,2,100)

y0 = real_func(x)
y1 = [np.random.normal(0, 0.5) + y for y in y0] # 制造噪音
n = 9

p_init = np.random.randn(n) # 随机生成多项式参数
plsq = leastsq(residuals_func, p_init, args=(y0, x)) #最小二乘法黑箱计算，参数为（误差函数，误差函数的参数，样本点）
print(plsq)
plt.plot(x_points, real_func(x_points),c='r',label='real')
plt.plot(x_points,fit_func(plsq[0], x_points),c='b',label='fit')
plt.plot(x, y1,'bo', label='with noise')
plt.legend(loc='best')  # 如果画图中有加lable，记得加上plt.legend(loc='best')
plt.show()