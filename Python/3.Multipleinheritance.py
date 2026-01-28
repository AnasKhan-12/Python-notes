class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
        
class Predator(Animal):
    def hunt(self):
        print("Hunting")

class Prey(Animal):
    def flee(self):
        print("Fleeing")

class Hawk(Predator):
    pass
    
class Rabit(Prey):
    pass



a=Rabit('rabbit')
a.flee()
b=Hawk('abcs')
b.hunt()

a.eat()