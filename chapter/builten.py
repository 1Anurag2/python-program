class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value

# Create an instance of MyClass
my_instance = MyClass(1)

# Get the directory of the class
print("Class Directory:", dir(MyClass))

# Get the directory of the instance
print("Instance Directory:", dir(my_instance))
