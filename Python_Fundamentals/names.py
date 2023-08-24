"""
Part I
Given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
Create a program that outputs:
    Michael Jordan
    John Rosales
    Mark Guillen
    KB Tonel

Part II
Now, given the following dictionary:
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
Create a program that prints  the following format (including number of characters in each combined name):
Students
    1 - MICHAEL JORDAN - 13
    2 - JOHN ROSALES - 11
    3 - MARK GUILLEN - 11
    4 - KB TONEL - 7
Instructors
    1 - MICHAEL CHOI - 11
    2 - MARTIN PURYEAR - 13
"""

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
'''
# part II Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
'''
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printNames2(dic):
  i = 0
  for keys, values in dic.items():
    print keys
    for data in values:
      i+=1
      nameLength = len(data["first_name"]) + len(data["last_name"])
      fullName = data["first_name"] + " " + data["last_name"]
      print str(i) + " - " + fullName + " - " + str(nameLength)


printNames2(users)
