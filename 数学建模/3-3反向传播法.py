import numpy as np
import math
import random

def rand(a,b):
    return (b-a)*random.random()+a
def make_matri3(m,n,fill=0.0):
    mat=[]
    for i in range(m):
        mat.append([fill]*n)
    return mat

def sigmoid(x):
    return 1.0/(1.0+math.exp(-x))
    
def sigmoid_derivate(x):
    return x*(1-x)
class BPNeuralNetwork:
    def __init__(self):
        self.input_n=0
        self.hidden_n=0
        self.output_n=0
        self.input_cells=[]
        self.hidden_cells=[]
        self.output_cells=[]
        self.input_weight=[]
        self.output_weight=[]
    def setup(self,ni,nh,no):
        self.input_n=ni+1
        self.hidden_n=nh
        self.output_n=no
        self.input_cells=[1.0]*self.input_n
        self.hidden_cells=[1.0]*self.hidden_n
        self.output_cells=[1.0]*self.output_n
        self.input_weight=make_matri3(self.input_n, self.hidden_n)
        self.output_weight=make_matri3(self.hidden_n, self.output_n)
        #random activate
        for i in range(self.input_n):
            for h in range(self.hidden_n):
                self.input_weight[i][h]=rand(-0.2,0.2)
        for h in range(self.hidden_n):
            for o in range(self.output_n):
                self.output_weight[h][o]=rand(-2.0,0.2)
    def predict(self,inputs):
        for i in range(self.input_n-1):
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        










    