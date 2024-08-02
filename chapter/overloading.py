class A:
    def show(self):
        print("Welcome")
    def show(self , firstname=''):
        print("Welcome",firstname)
    def show(self,firstname='',lastname=''):
        print("Welcome",firstname,lastname)
obj = A()
obj.show()
obj.show('Rajesh')
obj.show('Rajesh','Kumar')