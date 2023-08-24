# for i in range(1,1000):
#     if(i % 2 == 1):
# #         print i

# for i in range(5,1000):
#     if(i % 5 == 0):
#         print i


#avg
a = [1,2,5,10,255,3]
sum = 0
for num in a:
    sum += num

print sum/len(a)

#Function is a named block of code that we can execute to perform a specific task.
def add(a,b):
    x = a + b
    return x
#the return value gets assigned to the "result" variable
result = add(3,5)
print result


# the def keyword signifies the declaration of a function
# Declaration means naming the function and creating the instruction
# we've named the function 'add' and we give it two parameters(inputs to the function)
def add(a,b):
  x = a + b
  return x  # we return something (more on this later)

# this function has one parameter(input)
def say_hi(name):
  print "Hi, " + name

say_hi('Michael')


def add(a, b):
  x = a + b
  return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print sum3
