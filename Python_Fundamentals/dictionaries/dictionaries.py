#A  Dictionary  is another  mutable container type that can store any number of Python objects, 
# including other container types. Dictionaries consist of pairs (called items) of keys and their corresponding values. 
# Python dictionaries are also known as associative arrays or hash tables.

#When you initially create a dictionary, it is very much like making a tuple or list. 
# Tuples use the '(' and ')' characters and lists use the '[' and ']' characters. 
# Guess what! dictionaries use the '{' and '}' characters - curly braces. 
#The '( )' and '[ ]' pairs can also be useful with dictionaries, though. Below is an example:

weekend = { "Sun": "Sunday", "Mon": "Monday" } #literal notation
vals = dict(one=1, two=2) # dict() function
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
d = { i: object() for i in range(4) } #dictionary comprehension

#in the example above 
#1. Using literal notation. The key-value pairs are enclosed by curly brackets. The pairs are separated by commas. The first value of a pair is a key, which is followed by a colon character and a value. 
# The "Sun" string is a key and the "Sunday" string is a value.
#2. Using the dict()  function.
#3. Creating empty dictionary and then, adding some values. 
#  The keys are inside the square brackets, the values are located on the right side of the assignment.
#4. Using a dictionary comprehension. The comprehension has two parts.
#  The first part is the i: object() expression, which is executed for each cycle of a loop.
#  The second part is: for i  in range(4) loop. The dictionary comprehension creates a dictionary having four pairs,
#  where the keys are numbers 0, 1, 2, and 3 and the values are simple objects.

# Each key in a dictionary must be unique. If you make an assignment using an existing key as the index, 
# the old value associated with that key is overwritten by the new value.
# You can use this characteristic to an advantage in order to modify an existing value for an existing key.

#Accessing Values
#Use square brackets with the key to obtain its value
print weekend["Sun"]
print capitals["svk"]

#Or use the for loop to access all keys and values

#to print all keys
for data in capitals:
    print data
#another way to print all keys
for key in capitals.iterkeys():
    print key
#to print the values
for val in capitals.itervalues():
    print val
#to print all keys and values
for key,data in capitals.items():
    print key, "=", data


#functions for dictionaries
# cmp(dict1, dict2) - compares elements of both dictionaries
# len() 
# str() - produces a printable string representation of a dictionary
# type() = returns the type of the passed variable.

#python includes the following dictionary methods:
#(either dict.method(yourDictionary) or yourDictionary.method() will work)
# .clear() - removes all elements from the dictionary
# .copy() - returns a shallow copy
# .fromkeys(sequence, [value]) - create a new dictionary with the keys from the sequence and values set to value.
# .get(key, default=None) - For key key, returns avalue or defaults if key is not in dictionary.
# .has_key(key) - returns true if a given key is available in the dictionary, otherwise false.
# .items() - returns a list of dictionary's (key, value) tuple pairs.
# .keys() - returns a  list of dictionary keys
# .setdefault(key, default=None) = similar to get(), but will set dict[key]=default if key is not already in dictionary
# .update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary
# .values() - returns list of dictionary values.

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

 #to iterate values, use nested for loop
for key, data in context.items():
    #print data
    for value in data:
        print "Question #", value["id"], ": ", value["content"]
        print "----"

#Lists from Dictionary
#use methods items(), keys() and values().
data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()
#['house', 'red', 'cat']
print data.values()
#['Haus', 'rot', 'Katze']

#Dictionaries from Lists
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]


#zip function
country_specialities = zip(countries, dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]

#dict() function
country_specialities_dict = dict(country_specialities)
print country_specialities_dict
#Result is...
#{'Germany': 'sauerkraut', 'Spain': 'paella', 'Italy': 'pizza', 'USA': 'hamburger'}

#For zip() 
# if one of the two argument lists contains more elements than the other one
# The superfuluous elements will not be used, whether the extras are keys or values:
countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
country_specialities = zip(countries,dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
#Switzerland is dropped in the last one


# part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def printNames(dic):
  for data in dic:
    for value in data.itervalues():
        print value,
    print ""
printNames(students)



#Create a program that prints  the following format 
# (including number of characters in each combined name):

users = {
    'students': [ 
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
     'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Trey', 'last_name' : 'Villafane'}
  ]
 }

for key, data in users.items():
    print "\n%s" %key.title()
    counter = 0

    for value in data:
        counter = counter + 1
        full_name = value["first_name"] + " " + value["last_name"]
        full_name_upper = full_name.upper()
        name_count = len(value["first_name"]) + len(value["last_name"])

        print "%d - %s - %d" %(counter, full_name_upper, name_count)
