# Note  : Search "mro docs Python"
      # :  mro Indicate the position of function search during execution 

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}") 
        
class Dancer:
    def __init__(self, dance):
        self.dance = dance 
    def show(self):
        print(f"The dance is {self.dance}") 

class DancerEmployee(Dancer,Employee): 
    def __init__(self, dance , name ):
        self.name= name 
        self.dance = dance 

    def show(self): #Inheritance Invoking depends on position of parent class
        super().show()
       

a = DancerEmployee( "Atif","waqas")
print(a.name)
print(a.dance)
a.show()
print(DancerEmployee.mro())