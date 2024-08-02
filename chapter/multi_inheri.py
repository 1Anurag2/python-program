class Father():
    surname = "Verma"
class Son(Father):
    def show(self):
        print("Anurag", self.surname)
class Gs(Son):
    def display(self):
        print("Ayansh",self.surname)
obj1 = Son()
obj1.show()

obj = Gs()
obj.display()
obj.show()