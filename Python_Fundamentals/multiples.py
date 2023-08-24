# Create a program that prints all the odd numbers from 1 to 1000. Use the for loop and don't use array to do this exercise.

def oddNum(x):
    for i in range(x):
        if i % 2 == 1:
            print(i)

def multipleFive(x):
    for i in range(x):
        if i % 5 == 0:
            print(i)
