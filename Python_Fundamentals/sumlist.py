"""
    Create a program that prints the sum of all the values in the list:
"""
a = [1, 2, 5, 10, 255, 3]

def sumList(x):
    sumlist = 0
    for i in x:
        sumlist+=i
    return sumlist

print(sumList(a))
