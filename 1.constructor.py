class Person:

    numofpersons=0 #class variable

    def __init__(self,n,c):
        self.name=n
        self.occupation=c
        Person.numofpersons+=1
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        print(f"number of persons {Person.numofpersons}")


a=Person("Anas","Engineer")  # a goes to self anas to n  and engineer tto c 
a.info()