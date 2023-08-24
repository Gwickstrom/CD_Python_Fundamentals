#if statement:
age = 15
if age >= 18:
    print 'Legal Age'
else:
    print "You are so young!"

age = 17
if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'One more year and you will be of legal age'
else:
  print 'You are so young!'

#== check if the value of two operands are equal or notm if yes, true.
# != and <> similar

# and... Checks each expression on the left and right. If both are true then this evalutes true. If either 
# or both is falese then this is False

# not... Reverses the true-false value of the operand. not(true) is false. not(1 >= 2) is true.abs

for count in range(0,5):
    print "looping - ", count

# for <counter> in <sequence or range>:
# do something

#create a new list
#remember lists can hold many data-types even lists!
my_list = [4, 'dog', 99, ['list', 'inside', 'another'], 'hello world']
for element in my_list:
    print element

count = 0
while count < 5: #colon
    print "looping - ", count
    count += 1

for val in "string":
    if val == "i":
        break
    print(val)

for val in "string":
    if val == "i":
        continue
    print(val)

#The pass statement is used when a statement is required syntactically but you do not#
#want any command or code to execute

class EmptyClass:
    pass
my_string = "this"
for val in my_string:
    pass
    #pass almost never seen in final production

x = 3
y = x
while y > 0:
    print y
    y = y - 1
    if y == 0:
        break
else:
    print "final else"