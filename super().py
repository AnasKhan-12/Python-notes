class shape:
    def __init__(self,color,isfilled):
        self.color=color
        self.isfilled=isfilled

    def find_color(self):
        print(f"The color found is {self.color}")

class circle(shape):
    def __init__(self,color,isfilled):
        super().__init__(color,isfilled) #to reuse the constructor of parent class
        # self.color=color
        # self.isfilled=isfilled

    def find_color(self): # jb bhi class ma koi function bnaogy self pass hga hi hga
        
        super().find_color() # <---
        
        print(f"{self.color} is green")

class triangle(shape):
    def __init__(self,color,isfilled):
        super().__init__(color,isfilled) #to reuse the constructor of parent class
        # self.color=color
        # self.isfilled=isfilled

a= circle('greem','true')
square=circle(color='red',isfilled='false')
print(square.color)
print(a.color)
a.find_color()

# super(CurrentClass, self)  --- general form
# Here:
# CurrentClass → the class where you are writing the code.

# self → the object instance being used.

# So inside a method of Child, you might write:

# super(circle, self).show() ---according to my class

# This explicitly says:
# 👉 “Go to the parent class of circle and call its show() method for this object (self).”

# Why do we sometimes write parameters and sometimes not?

# In Python 3, you can usually just write super() with no arguments, and Python automatically figures out CurrentClass and self using context.

# In Python 2, you had to write super(ClassName, self). That’s why you may still see the parametrized version — for backward compatibility or explicitness.

