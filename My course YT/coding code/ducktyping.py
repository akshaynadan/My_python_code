class Duck:
    def quack(self):
        print('Quack, quack!')
    def fly(self):
        print('Flap, flap!')
class Hen:
    def cluck(self):
        print('Cluck, cluck!')
    def fly(self):
        print("I'm too heavy to fly")
class Person:
    def doing(self,a):
        a.fly()
        print("I'm quacking like a duck!")

duck = Duck()
hen = Hen()
person = Person()
person.doing(duck)