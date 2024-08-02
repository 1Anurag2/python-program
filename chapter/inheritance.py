class A:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    def add(self):
        print( self.num1 + self.num2)
    def sub(self):
        print( self.num1 - self.num2)
class B(A):
    def mul(self):
       print( self.num1 * self.num2)
    def div(self):
       print( self.num1 / self.num2)
obj = B()
obj.add()
obj.sub()
obj.mul()
obj.div()

