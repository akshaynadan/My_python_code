

#create a class mesurement
class Measurement:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
        print(self.length, self.breath)
#create a class rectangle
class Rectangle(Measurement):
    def __init__(self, length, breath): #flow of program
        print("check1")
        super().__init__(length, breath)
        print("check")
    def area(self):
        return self.length * self.length
    def perimeter(self):
        print("check2")
        return 4 * self.breath

#main program
l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breath of rectangle: "))
ans = Rectangle(l, b)
print(ans.perimeter())
