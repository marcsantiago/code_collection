from random import choice

#The code was written for python3, the block below allows the code to work with python 2.7
try:
    from future_builtins import *
except ImportError:
    pass

try:
    input = raw_input
    range = xrange
except NameError:
    pass

#global variables
choices = ["rock", "paper", "scissor"]
player_score = 0
computer_score = 0

def computers_choice(choices):
	return choice(choices)

def players_choice():
	print("1 = rock")
	print("2 = paper")
	print("3 = scissor")
	
	answer = ''
	while answer not in choices:
		answer = input("Please enter 1, 2, or 3\n")
		if answer == "1":
			answer = "rock"
		elif answer == "2":
			answer = "paper"
		elif answer == "3":
			answer = "scissor"
	return answer

def check_winner():
	player = players_choice()
	computer = computers_choice(choices)
	#access variables from the outer scope and edit them
	global player_score 
	global computer_score
	#game logic
	if player == "rock" and computer == "scissor":
		print("Player wins")
		player_score += 1

	elif player == "scissor" and computer == "rock":
		print("Computer wins")
		computer_score += 1

	elif player == "paper" and computer == "rock":
		print("Player wins")
		player_score += 1
	
	elif player == "rock" and computer == "paper":
		print("Computer wins")
		computer_score += 1
	
	else:
		print("Tie!")

def play_game():
	check_winner()
	answer = ""
	while True:
		answer = input("Would you like to play again? [yes] [no]\n")
		if answer.lower() in ["y", "yes"]:
			check_winner()
		elif answer.lower() in ["n", "no"]:
			print("Your Score is: %s -- The Computer's score: %s" % (player_score, computer_score))
			break
		else:
			print("Invalid Entry")

play_game()
