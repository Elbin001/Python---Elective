import math
number = float(input("Enter a positive number : "))
tolerance = 0.000001
estimate = 1.0
while(True):
    estimate = (estimate + number/estimate)/2
    diffrence = abs(number - estimate ** 2)
    if(diffrence <= tolerance):
        break
print("The program's estimate : ",estimate)
print("Python's estimate      : ",math.sqrt(number))
