#area of a rectangle. Class based

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.__height=height
#the double dash in front of height makes it private and unchangeable so line 13 can't change it
    def area(self):
        return self.width * self.__height

rect = Rectangle(7, 6)
print(rect.area())
#above will try and rint rec area
rect.width = 1
rect.__height = 100
#above tries to change this but can't change height.
print(rect.area())
