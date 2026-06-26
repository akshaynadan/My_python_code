from abc import ABC, abstractmethod
class Vechile(ABC):
    @abstractmethod
    def start(self):
        pass
  
    def stop(self):
        print("Vechile is stopped")
class Car(Vechile):
    def start(self):
        print("Car is started")
    def stop(self):
        print("Car is stopped")
class Bike(Vechile):
    def start(self):
        print("Bike is started")
   
c = Car()
b = Bike()
c.start()
Vechile.stop(c)#no obj is created for Vechile class
