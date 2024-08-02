class Duck:
    def show(self):
        print("This is a Duck")

class Horse:
    def display(self):
        print("This is a horse")

class cat:
    def show(self):
        print("This is a cat")

def myfunction(obj):
    if hasattr(obj, 'show'):
        obj.show()
    if hasattr(obj,'display'):
        obj.display()

d = Duck()
myfunction(d)

h = Horse()
myfunction(h)

c = cat()
myfunction(c)