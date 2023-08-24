my_string = "This is a string stored in the my_string variable"
my_num = 5 # an integer stored in a variable
my_tuple = (1,2,3,4,5) # a tuple stored in a variable
# a dictionary stored in a variable
my_dictionary = {'name': 'Michael Choi', 'fave_lang': 'Python', 'level': 'Sensei'}

print my_string

# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
    #these lines are indented therefore part of the function
    if name:
        print 'Hello, ' + name + 'from inside the function'
    else:
        print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'
""" 
    This wont be printed 
"""

name = "Greg"
print "My name is", name

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

#Built in string functions
my_string = 'hello world'
print my_string.capitalize()
# the output would be:
# Hello world

my_string = 'Hello WORLD'
print my_string.lower()
# the output would be:
# hello world

my_string  = "Hello WORLD"
print my_string.swapcase()

my_string = 'hello world'
print my_string.upper()
# the output would be:
# HELLO WORLD


#Determines if specified string occurs in a given string and returns index where substring occurred -1 if not.
my_string = "hello world"
print my_string.find("el")
# the output would be:
# 1

my_string = "hello world"
print my_string.replace("world", "kitty")
# the output would be:
# hello kitty

my_string = "egg, egg, Spam, egg and Spam"
print my_string.replace("egg", "Spam", 2)
# the output would be:
# Spam, Spam, Spam, egg and Spam
# notice that only the first 2 "egg" matches were replaced in the string.



#Lists
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []


#Accessing Values
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens


x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]

x = [1,2,3,4,5]
x.insert(2,99)
print x
#the output would be [1,2,99,3,4,5]

x = [1,2,3,4,5]
x.remove(3)
print x
#the output would be [1,2,4,5]

x = [1,2,3,4,5]
x.pop()
print x
#the output would be [1,2,3,4]
y = [10,11,12,13,14]
y.pop(1)
print y
#the output would be [10,12,13,14]


x = [99,4,2,5,-3];
x.sort()
print x
#the output would be [-3,2,4,5,99];

x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3]
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5]


#LIST BUILT-IN FUNCTIONS
#len()
my_list = [1, 'Zen', 'hi']
print len(my_list)
# the output would be 3

#max()
my_list = [1, 7, 3]
print max(my_list)
# the output would be 7

#min()
my_list = [1, 20, 42]
print min(my_list)
#output would be 1


#any()
my_list = [0, 'hi', '']
print any(my_list)
# the output would be True since a string would equate to true in this case
my_list = [0, '']
print any(my_list)
# the output would be False since 0 (zero) and an empty string will both be false

#all()
my_list = [0, 'Zen', '']
print all(my_list)
# the output would be False
my_list = [4, 'hi']
print all(my_list)
# the output would be True
