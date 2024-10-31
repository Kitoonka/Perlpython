num=int(input("Enternumber:"))

if num%2==0:
      print(f"{num} is even number")

else:
     print(f"{num} is odd number")


# create a program that checks if someone can vote or not using age above 18

age=int(input("Enter your age:"))
if age>=18:
      print("you are eligible to vote")
else:
    print("you are underage")

    # Program to grade a student as pass or fail
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("You have passed!")
else:
    print("You have failed.")

if marks <= 100 and marks >= 80:
    print("You have an A")
elif marks <= 79 and marks >= 60:
    print("You have a B")
elif marks <= 59 and marks >= 40:
    print("You have a C")
elif marks >= 0 and marks <= 39:
    print("You have failed terribly")
else:
    print("Invalid marks entered")



