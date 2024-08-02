from abc import ABC,abstractmethod
class Car(ABC):
    def show(self):
        print("Every car has 4 wheels")
    @abstractmethod
    def speed(self):
        pass
class Maruti(Car):
    def speed(self):
        print("Maruti speed is 100kmph")
class Suziki(Car):
    def speed(self):
        print("Suzuki speed is 120kmph")
class BMW(Car):
    def speed(self):
        print("BMW speed is 250kmph")
obj = Maruti()
obj.show()
obj.speed()

obj1 = Suziki()
obj1.show()
obj1.speed()

obj2 = BMW()
obj2.show()
obj2.speed()