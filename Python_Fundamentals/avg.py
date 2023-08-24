"""
Create a program that prints the average of the values in the list:
a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

def avgValue(x):
    sumlist = 0
    avg = 0
    for i in x:
        sumlist+=i
    avg = sumlist / len(x)
    return avg

print(avgValue(a))
