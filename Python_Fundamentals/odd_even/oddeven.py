# for i in range(1,2000):
#     if(i % 2 == 1):
#         print "Number is ", i, " This is an odd number."
#     else:
#         print "Number is ", i, " This is an even number."

# a = [2,4,10,16]
# def multiply(arr):
#     for i in range(len(arr)):
#         arr[i] = arr[i] * 5
#     return arr

# b = multiply(a)
# print b

#Assignment Scores and Grades

# from random import randint

# print "Scores and Grades"
# for count in range(0,10):
#     score = randint(70,100)

#     if(score <= 70):
#         grade = "D"
#     elif(score <= 80):
#         grade = "C"
#     elif(score <= 90):
#         grade = "B"
#     else:
#         grade = "A"
#     print "Score: %d; Your grade is %s" %(score, grade)

# print "End of program. Bye!"

# import random
# random_num = random.random()
# #the random function will return a floating point number.
# #that is 0.0 <= random_num < 1.0

# #use built-in round function


# #Coin Toss
# for count in range(0,5):
#     x_rounded = round(random.random())
#     if(x_rounded == 0):
#         print "Tails"
#     else:
#         print "Heads"



# Draw Stars function
x = [4, "Greg", 6, "Tom", 1, 3, "G Dub", 5, 7, 25]

def draw_stars2(my_list):
    for item in my_list:
        output = ""
        if type(item) is int:
            for i in range(item):
                output += "*"
        elif type(item) is str:
            first_letter = item[0].lower()
            for i in range(len(item)):
                output += first_letter
        print output
draw_stars2(x)
