# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:07:10 2020

@author: 19225
"""

names=['a','b','c','d']
scores=[1,2,3,7]
for name,score in zip(names,scores):
    print(score,name)    
    
def add(x,y):#函数
    return(x*y)
print(add(3,5)) 
   
import re
text='maishu:178,tz:168,xh:123456,ai—ren:1234556，5555'
print(re.findall(r'123456',text))#找个数

print(re.findall(r'\d',text))#数字

print(re.findall(r'\D',text))#非数字

print(re.findall(r'\w',text))#非标点符号以外字符

print(re.findall(r'[1-5]',text))#一到五的数字

print(re.findall(r'[ai-ren,1]',text))#找到逗号，1，airen的字母
#[aA-zZ]等于查小写字母
#找出所有的数
print(re.findall(r'\d+',text))
print(re.findall(r'5+',text))#五起头的数
print(re.findall(r'\d{3}',text))#有切的功能，三个数字
 
    
names=['a','b','c','d']
scores=[1,2,3,4]
for name,score in zip(names,scores):
    print(score,name)
    
names=['a','b','c','d']
scores=[1,2,3,5]
for name,score in zip(names,scores):
    print(score,name)    
    
    

class Car:
    def __init__(self,make,model,year,reading):
        self.make=make
        self.model=model
        self.year=year
        self.reading=reading
        
    def full_name(self):
        full=f"{self.make},{self.model},{self.year}  {self.reading}"
        return full
    
my_car=Car('yadi','a6',2017,'wo de')
print(f"梁雅迪 is {my_car.full_name()}")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    