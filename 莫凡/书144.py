class Rest:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def des(self):
        print(f"{self.name} 生意兴隆！")
        
        
    def open_re(self):
        print(f"一般来这吃饭的{self.type}都很好")

res1=Rest('星河','有钱人')
res1.des()
res1.open_re()
