#Occurence of objects in multiple forms

class Dog:
    def speak(self):
        return "woof"

class Cat:
    def speak(self):
        return "meow"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

greetings="Hello World"
print(len(greetings))

fruits=("Apples","mangoes","Cherry")
print(len(fruits))