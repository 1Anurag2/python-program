class A:
    def show(self):
        print("This is a parent class method")
class B(A):
    def show(self):
        print("This is a child class method")
        super().show()      # super fuction is for parent class method
obj = B()
obj.show()
obj.show()