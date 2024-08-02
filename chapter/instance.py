class Myclass():
    def printdetails(self):
        return f"My name is {self.name} ,my  age is {self.age} and my salary is {self.salary}"
obj = Myclass()
obj.name = "Anurag"
obj.age = 20
obj.salary = 250000

amit = Myclass()
amit.name = "Amit"
amit.age = 21
amit.salary = 300000

print(obj.printdetails())
print(amit.printdetails())