

                                                            #Inheritance 
# #create a class called "Person"
class Person:
    name = input("Enter your name: ")
    def sleep(self):
        print(self.name + " is sleeping")
    def eat(self):
        print(self.name + " is eating")
    def study(self):
        print(self.name + " is studying")

#Create a class called "man"
class Man(Person):
    def work(self):
        print(self.name + " is working")
    def earn(self):
        print(self.name + " is earning")

#Create a class women
class Women(Person):
    def cook(self):
        print(self.name + " is cooking")
    def clean(self):
        print(self.name + " is cleaning")


Person = Person()
Man = Man()   
Women = Women()



print(Person.name)
print(Women.name)
Person.sleep()
Man.sleep()
Man.work()
Women.cook()


    