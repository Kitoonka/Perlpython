# inheritance

class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Child(Parent):
    def greet(self):
        return (f"my name is {self.name},i am {self.age}")

child=Child(name="pesh",age=8)
child2=Child(name="STELLA",age=10)
print(child.greet())
print(child2.greet())


class Parent:
    def __init__(self):
        def greet(self):
            return f"i am a parent"
print
