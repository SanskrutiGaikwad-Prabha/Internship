num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
try:
    result=num1/num2
except ZeroDivisionError as e:
    print("Cannot divide by zero")
else :
    print("Result :",result)

try:
    num=int(input("Enter a number :"))
except ValueError as e:
    print("Invalid input.Please a number")
list1=[23,76,86,54,21]
i=int(input("Enter index :"))
try :
    print("Element :",list1[i])
except IndexError as e:
    print("Index out of range")

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
try:
    result=num1/num2
except ZeroDivisionError as e:
    print("Cannot divide by zero")
else :
    print("Result :",result)


i=int(input("Enter index :"))
try:
    number=int(input("Enter a number:"))
    print("Element :",list1[i])
except ValueError as e:
    print("Invalid input")
except IndexError as e:
    print("Index out of range")

class NegativenumberError(Exception):
    pass

num=int(input("Enter a number :"))
if num<0:
    raise NegativenumberError("Negative numbers are not allowed")

try:
    open("abstrct.py")
except FileNotFoundError as e:
    print("File does not found")
finally:
    print("File operation completed")