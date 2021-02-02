#书本149,9—4
class Rest:
    def __init__(self,name,typea):
        self.name=name
        self.typea=typea
        self.num=0
        
    def des(self):
        print(f"{self.name} 生意兴隆！")
        
    def open_re(self):
        print(f"一般来这吃饭的{self.typea}都很好")
    
    def number_served(self,num):
        self.num=num
        print(f'{self.num}人在这里吃过饭')
    def increment_number_served(self,new):  
        self.new=new
        self.num=self.num+self.new
        print(f'总共{self.num}')
        
res1=Rest('星河','有钱人')
res1.des()
res1.open_re()
res1.number_served(20)
res1.increment_number_served(5)
res1.increment_number_served(10)

class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        
        
    def describe(self): 
        self.full={self.first_name,self.last_name}
        print(f'{self.full}今天来我这吃饭')

u1=User('詹','峰')
u1.describe()
