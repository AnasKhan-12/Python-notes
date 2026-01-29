# Polymorphism = Greek word meaning having multiple forms


class Shape:
    def __init__(self):
        def area(self):
            pass
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius**2
    

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2
    
class Pizza(Circle):
    def __init__(self,topping,radius):
        super(Pizza,self).__init__(radius)
        self.topping=topping
        # self.radius=radius

# Pizza exists as three forms:
# 1. Pizza
# 2. Circle
# 3. Shape
        
shapes=[Circle(4),Square(5),Pizza("Pepperoni",4)]

print(shapes[0].area())  # simply waowwwwwwww

# for shape in shapes:
#     print(f"{shape.area()} cm")
        