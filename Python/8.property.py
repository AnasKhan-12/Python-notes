class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height =height

    @property #this becomes a getter which makes widdth a attriibute of rectangle instead of calling it like a function
    #more defined in line 27
    def width1 (self):
        return f"{self._width}cm"
    
    # @property 
    # def height(self):
    #     return f"{self._height}cm"
    
   # @width.setter ->the name must be same as property function name this throws a error
    @width1.setter
    def width2(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("Width must be greater than zero")
    
rectangle= Rectangle(32,22)
rectangle.width2=33
print(rectangle.width1)
#print(rectangle.height)


# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     def get_width(self):   # just a normal function
#         return f"{self._width}cm"

# rectangle = Rectangle(32, 22)
# print(rectangle.get_width())   # need parentheses
