'''Write a Python program to create a class that represents 
a shape. Include methods to calculate its area and perimeter. 
Implement subclasses for different shapes like circle, 
triangle, and square'''
import math
class Shape:
  def area(self):
    pass
  def perimetwr(self):
    pass
class Circle(Shape):
  def __init__(self,r):
    self.r=r
  def area(self):
    return math.pi*self.r**2
  def perimeter(self):
    return 2*math.pi*self.r
class Triangle:
  def __init__(self,l,b):
    self.l=l
    self.b=b
  def area(self):
    return self.l*self.b
  def perimeter(self):
    return 2*(self.l+self.b)
class Square:
  def __init__(self,side):
    self.side=side
  def area(self):
    return self.side*self.side
  def perimeter(self):
    return 4*self.side
obj=Circle(5)
print("circle area:",obj.area())
print("perimeter of circle:",obj.perimeter())
obj1=Triangle(8,9)
print("area of triangle:",obj1.area())
print("perimeter of triangle:",obj1.perimeter())
obj2=Square(12)
print("area of square:",obj2.area())
print("perimeter of square:",obj2.perimeter())
