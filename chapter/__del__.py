class Myclass():
    def __init__(self):
        print("Hello , world")
    def show(self):
        print("welcome")
    def _del_(self):
        print("obj  is deleted")
obj = Myclass()
obj.show()
del obj

obj.show()