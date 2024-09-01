#imported sys
import sys
#Using Exception handling when user enter the string then it not give error 
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)
try:
    result =  x / y
except ZeroDivisionError:
    print("Error: Cannot be divisible by zero")
    sys.exit(1)   
print(result)