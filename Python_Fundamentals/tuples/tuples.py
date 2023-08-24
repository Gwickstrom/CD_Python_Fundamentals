
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

#Tuples can't be changed, immutable. tuples use parentheses. declaring different comma-seperated values

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"


julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

print julia[2]

for data in julia:
     print data

julia = julia + ("Eat Pray Love", 2010)
#result is...
#("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia", "Eat Pray Love", 2010)


julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
#result is...
#("Julia", "Roberts", 1967, "Eat Pray Love", 2010, "Actress", "Atlanta, Georgia")

value = ("Michael", "Instructor", "Coding Dojo") #tuple packing


#IMPORTANT tuple unpacking

value = ("Michael", "Instructor", "Coding Dojo")
(name, position, company) = value #tuple unpacking
print name
print position
print company

#swapping
temp = a
a = b
b = temp

(a, b) = (b, a)


#len()
tuple_data = ('physics', 'chemistry', 1997, 2000)
print len(tuple_data)
#result: 4

#max()
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)
print max(tuple_data)
print max(tuple_num)
#result is..
#x-ray
#89


#min()
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)
print min(tuple_data)
print min(tuple_num)
#result is...
#chemistry
#15


#sum()
tuple_num = (67, 89, 31, 15)
print sum(tuple_num)
#result: 202


#any()
tuple_num = (67, 89, 31, False, 0, None)
print any(tuple_num)
#result: True


#all()
tuple_num = (67, 89, 31, False, 0, None)
print all(tuple_num)
#result: False

#enumerate()
num = (1, 5, 7, 3, 8)
for index, item in enumerate(num):
    print(str(index)+" = "+str(item))
#result is...
#0 = 1
#1 = 5
#2 = 7
#3 = 3
#4 = 8

#sorted()
num = (1, 5, 7, 3, 8)
print sorted(num)
#result: [1,3,5,7,8]


#reversed()
num = (9, 1, 8, 2, 7, 3)
print tuple(reversed(num))
#result: (3, 7, 2, 8, 1, 9)

#Functions can always only return a single value, but by making that value a tuple, we can effectively group
# together as many as we like, and return them together.
# highest lowest score, mean and standard deviation, year month and day.

#this returns the circum and the area of a circle of radius r:
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c,a)