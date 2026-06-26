#create a class measurement
class Measurement:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
       
#create a class rectangle
class Rectangle(Measurement):
    def area(self):
        return self.length * self.length
    def perimeter(self):
        return 4 * self.breath
l = int(input("Enter the length of rectangle: "))#f
b = int(input("Enter the breath of rectangle: "))
a = Rectangle(l, b)
print(a.perimeter())
