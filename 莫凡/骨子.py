
from random import randint
class Die:
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
        
    def roll(self):
        return randint(1, self.num_sides)

from plotly.graph_objs import Bar,Layout
from plotly import offline

#from die import Die
die=Die()
results=[]
for roll_num in range(100):
    result=die.roll()
    results.append(result) 
    
    
frequencies=[]
for value in range(1, die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
x_values=list(range(1, die.num_sides+1))
data=[Bar(x=x_values,y=frequencies)]  

x_axis_config={'title':'结果'}
y_axis_config={'title':'结果的频率'} 
my_layout=Layout(title='郑一个',
                 xaxis=x_axis_config,yaxis=y_axis_config)  
offline.plot({'data':data,'layout':my_layout},filename='d6.html')   
#print(results) 
#print(frequencies)   
    