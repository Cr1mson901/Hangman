import random
#imports from stages.py
from stages import logo
from stages import stages
print(logo)
#grabs a random number from a doc called word_list
rdm_val = random.randint(1,1000)
with open('./word_list.txt') as f:
	words = f.readlines()
word = words[rdm_val].lower()
#Use for testing
#print(word)	

#Generate blanks
blank_list = []
for x in range(1, len(word)):
	blank_list.append("_")
	
print(' '.join(blank_list))

lives = 6
correct = 0
incorrect_guesses = []
while lives > 0 and correct < len(word) - 1:
	guess = input("Pic a letter\n").lower()
	#If the guess does not meet the criteria so asks them to guess again
	if len(guess) != 1:
		print('Please guess 1 letter at a time')
	#checks if the guess has already been made, if yes, tells player and asks for them to guess again
	elif not guess.isalpha():
		print('{} is not a letter of the alphabet'.format(guess))
	#checks if the letter has already been guessed
	elif guess in blank_list:
		print("You've already guessed that word, Please guess another")
	#checks if the guess is inside the word, if yes, replaces the blank with the guess
	elif guess in word:
		for x in range(len(word)):
			if guess == word[x]:
				blank_list[x] = guess
				correct += 1
		print(stages[lives])
		print('Incorrect Guesses: ' + ' '.join(incorrect_guesses))
		print('There is a(n) {} in this word'.format(guess))
		print(' '.join(blank_list))
	#Decrease the remaing lives on a failed guess
	else:
		lives -= 1
		incorrect_guesses.append(guess)
		print(stages[lives])
		print('Incorrect Guesses: ' + ' '.join(incorrect_guesses))
		print(' '.join(blank_list))
		print('{} is not in the word'.format(guess))

#End game text if the user won the game or not
if correct == len(word) - 1:
	print("Congragulations, you guessed the word {}".format(word))
else:
	print("Unfortunately you were unable to guess the word {}".format(word))
