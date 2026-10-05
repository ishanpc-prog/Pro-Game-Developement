class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello my name is ", self.name)

p1 = Person("Ishan",14)
print(p1.name)
p1.greet()
# p1 is thee object