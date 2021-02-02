import math
import random

def sigmoid(x):
    return 1.0/(1.0+math.exp(-x))
def sc(x,a):
    return math.log(x,a)#后面那个是底数
print(sc(128,2))

print(math.sin(math.pi/2))

print(math.pow(3, 4))#3的几次方

print(int(math.log(math.exp(2),math.e)))#int是可以取整
t=math.fabs(-5)
print(int(t))
p=math.ceil(6.5)#与[x]相反
print(p)
g=math.degrees(math.pi)#弧度转度
print(g)
f=math.erf(1)#误差函数
print(f)
print(random.random())#random无参数

