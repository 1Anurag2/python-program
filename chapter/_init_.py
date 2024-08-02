class Myclass():
   def __init__(self,name,age,salary):     #default constroctor jo obj argument ko pass karta hai
      self.myname=name
      self.myage=age
      self.mysalary=salary
obj = Myclass("Anurag",21,200000)
print("my name is ",obj.myname)

