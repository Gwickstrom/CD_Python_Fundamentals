"""
Create a function that counts from 1 to 2000. As it loops through each number, have your program generate the number and specify whether it's an odd or even number.
"""

def oddEven(x):
    i = 1
    for i in range(1,x + 1):
        if i % 2 == 1:
            print("This number is " + str(i) + " This is an odd number.")
        elif i % 2 == 0:
            print("This number is " str(i) + " This is an even number.")

print(oddEven(2000))
