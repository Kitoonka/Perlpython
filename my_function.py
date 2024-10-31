# def addtwonumbers():
#     num=int(input("Enter first Number"))
#     num2=int(input("Enter second Number"))
#     print(f"The sum of {num} and {num2} is {num+num2}")
#
#     addtwonumbers()
#
# def multiply(a, b):
#     return a * b
#
# # Call the function
# result = multiply(4, 5)
# print(result)

def addtwonumbers():
    num = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum of {num} and {num2} is {num + num2}")

# Call the function once to avoid infinite recursion
addtwonumbers()

def multiply(a, b):
    return a * b

# Call the function
result = multiply(4, 5)
print(result)


# def perl_class(name,age,gender):
#     print(f"Student Name:{name} Age is {age} and {gender}")

# Define the perl_class function
def perl_class(name, age, gender):
    print(f"Student Name: {name}, Age: {age}, Gender: {gender}")
