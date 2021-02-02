class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is sitting.")
        
    def roll_over(self):
        print(f"{self.name} rolled over!")
        
      
        
my_dog=Dog('ming',7)        
my_dog.sit(),my_dog.roll_over()


    def build_person(first_name,last_name):
        person=f{first_name}{last_name}
        return person
    