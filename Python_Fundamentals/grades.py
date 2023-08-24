"""
Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
The result should be like this...

Scores and Grades
Score: 87; Your grade is B
Score: 67; Your grade is D
Score: 95; Your grade is A
Score: 100; Your grade is A
Score: 75; Your grade is C
Score: 90; Your grade is A
Score: 89; Your grade is B
Score: 72; Your grade is C
Score: 60; Your grade is D
Score: 98; Your grade is A
End of the program. Bye!
"""


def gradeCalc():
    scores = []
    while len(scores) < 10:
      prompt = int(input("Enter a score: "))
      scores.append(prompt)
    print(scores)
    print("Scores and Grades")
    for x in scores:
      if x >= 90 and x <= 100:
        print("Score: " + str(x) + " Your grade is A")
      elif x >= 80 and x <= 89:
          print("Score: " + str(x) + " Your grade is B")
      elif x >= 70 and x <= 79:
          print("Score: " + str(x) + " Your grade is C")
      elif x >= 60 and x <= 69:
          print("Score: " + str(x) + " Your grade is D")
      else:
          print("Your grade is F")
    print("End of the program")

gradeCalc()
