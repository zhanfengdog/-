from random import choice
class Randomwalk:
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
        
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance
            
            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance
    
    
    
            if x_step==0 and y_step==0:
                continue
            
            x=self.x_values[-1]+x_step
            y=self.y_values[-1]+y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
import matplotlib.pyplot as plt
#from random_walk import Randomwalk
while True:
    #创建一个Random的实例
    rw=Randomwalk(50_000)
    rw=Randomwalk()
    rw.fill_walk()
    
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(10,6),dpi=128)
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
               edgecolors='none',s=1)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
               edgecolors='none',s=15)
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    ax.scatter(rw.x_values,rw.y_values,s=15)
    
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running=input('Make anther walk?(y/n):')
    if keep_running=='n':
        break
    




            
            
            
            
            