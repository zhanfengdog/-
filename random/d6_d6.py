
from random import randint
class Die:
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
        
    def roll(self):
        return randint(1, self.num_sides)

from plotly.graph_objs import Bar,Layout
from plotly import offline

#from die import Die
die_1=Die()
die_2=Die()
results=[]
for roll_num in range(100):
    result=die_1.roll()+die_2.roll()
    results.append(result) 
    
    
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
x_values=list(range(2, max_result+1))
data=[Bar(x=x_values,y=frequencies)]  

x_axis_config={'title':'结果','dtick':1}
y_axis_config={'title':'结果的频率'} 
my_layout=Layout(title='郑2个',
                 xaxis=x_axis_config,yaxis=y_axis_config)  
offline.plot({'data':data,'layout':my_layout},filename='d6_d6.html')   
#print(results) 
#print(frequencies)   
    