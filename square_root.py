import math

num = int(input("Enter a Number:"))

if num >= 0:
    square_root = math.sqrt(num)
    print("The square root of the number is:", square_root)
else:
    print("Square root of a negative number is not real")