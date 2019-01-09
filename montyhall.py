"""
The Monty Hall Simulation
CS 550 Kevin  Xie

Prediction:
From what I remember about the problem, it's always best to swap, because once
one of the doors is revealed, the probability drops from 1/3 (when you chose first)
to 1/2 that you will get the car rather than the penny. However, I'm really not
sure why that would mean the swapped door is more likely to have the car.

Result:
Switching has an approximately 2/3 chance of winning, while not switching has an
approximately 1/3 chance of winning.

In a given simulation of 1000 trials:
Non-switch: 339
Switch = 646

How to use:
py montyhall.py [# trials] [Switch? (0/1)]

On my Honor, I have neither given nor received unauthorized aid.
Kevin Xie

"""

import sys, random

# number of trials entered in command line and whether or not player switches
trials = int(sys.argv[1])
switch = int(sys.argv[2])

# to keep count of victories
count = 0

# "trials" number of recursions
for i in range(trials):
	# available list choices
	doornums = [0,1,2]
	# doors
	doors = [False,False,False]
	# chooses a random door for prize and sets prize to True
	car = random.randrange(0,3)
	doors[car] = True
	# player's choice
	choice = random.randrange(0,3)
	# if player's choice is the car, remove only the car (so program can randomly remove one of remaining "pennies"), else, remove car and player's choice and reveal remaining "penny"
	if car == choice:
		doornums.remove(car)
	else:
		doornums.remove(car)
		doornums.remove(choice)
	# randomly choose a reveal from the remaining door numbers and reveal it as 0
	removed = random.choice(doornums)
	doors[removed]=0
	# if switch is true, then remove player's choice and revealed door from list of door numbers and choose remaining door
	if switch == 1:
		choicenums = [0,1,2]
		choicenums.remove(choice)
		choicenums.remove(removed)
		choice = choicenums[0]
	# else, stay with original choice
	else:
		pass
	# if player's choice is the car (prize), then counter moves up by 1
	if choice == car:
		count+=1

# prints final count
print(count)