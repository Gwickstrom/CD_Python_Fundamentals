"""
Create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
Sample output should be like the following:
          Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
........
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far

Ending the program, thank you!
"""

import random

numOftoss = int(input("How many times do you want to toss the coin?"))

def coinToss(num):
    attempt = 1
    heads = 0
    tails = 0
    while attempt <= num:
        x = random.random()
        if round(x) == 1:
            heads +=1
            print("Attempt #" + str(attempt) + " Throwing a coin....Heads! Got " + str(heads) + " heads and " + str(tails) + " tails so far" )
        elif round(x) == 0:
            tails +=1
            print("Attempt #" + str(attempt) + " Throwing a coin....Tails! Got " + str(heads) + " heads and " + str(tails) + " tails so far")
        attempt+=1

coinToss(numOftoss)
