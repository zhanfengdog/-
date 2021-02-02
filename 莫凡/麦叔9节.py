class Lover:
    num_of_lover=0#类属性
    #狗的构造方法,打游戏，颜色好看，实例属性
    def __init__(self,name,height,blood):
        self.name=name
        self.height=height
        self.blood=blood
        self.cj=100
        print(f"{self.name}好漂亮")
        
    def beai(self):
        print(f'我是这么认识{self.name},她的身高是{self.height}')
    
    def add(self):
        self.cj=self.cj+5
            
    def reduce_s(self,cj):
        if(cj>100):
            self.cj=100#记得加self
        else:
           self.cj=self.cj
    def update_cj(self,cj):
        if self.cj>=cj:
           self.cj=cj
        else:
            print("你真的有趣，傻仔")

l1=Lover('lyd', 152,'a')#这里就用上了
l2=Lover('zxm',158,'b')

print(l1.name,l1.height,l1.cj)
l1.cj=98#重新赋值
print(l1.name,l1.height,l1.cj)
print(l2.name,l2.height)

print(id(l1))#内存地址
print(id(l2))

l1.beai()
l1.add()

l1.reduce_s(l1.cj)#指出是谁的成绩
Lover.num_of_lover=3#重要
print(l1.cj)

print(Lover.num_of_lover)#通过类名访问
print(l1.num_of_lover)
l1.num_of_lover=5
print(l1.num_of_lover)
print(Lover.num_of_lover)

l1.update_cj(30)
print(l1.cj)
l1.update_cj(150)



