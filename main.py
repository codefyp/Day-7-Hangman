#import the clear function to clear the hangman after each try
from replit import clear
#import random module so we can choose a random word from hangman_words.py
import random

#import the 'word_list' from hangman_words.py
from hangman_words import word_list
#chose randomly a word from word_list in a variable called chosen_word
chosen_word = random.choice(word_list)
#a variable which holds the number of the lengh of the chosen_word 
word_length = len(chosen_word)
#a variable to check if the game ended later
end_of_game = False
#starting lives before we lose
lives = 6 

#import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print (logo)
#testing code
#print(f'Pssst, the solution is {chosen_word}.')

#create a blank list
display = []
#we append in the blank list as many _ as the charachters of the random chosen_word
for _ in range(word_length):
    display += "_"

#the game starts at this point with a while loop, so while the end_of_game is true it will ask us to input a letter and convert it to a lower case
while not end_of_game:
    guess = input("Guess a letter: ").lower()
#clears the screen each time to guess a new letter    
    clear()
    #if the guessed a letter in display then print the letter and let them know
    if guess in display:
        print (f"You've already guessed this {guess} letter madafaka")
    #a for loop with a position variable to check if the letter is in the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        #then if the letter they guess is correct then add the letter to the display list at the position which is determined by the position variable
        if letter == guess:
            display[position] = letter

    #check if user is wrong.
    if guess not in chosen_word:
        #if the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        print(f"{guess} it's not in the chosen word, you lose a life")
        #then remove a life
        lives -= 1
        #then check if they run out of lives to end the game
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #join all the elements in the list and turn it into a string using the join function
    print(f"{' '.join(display)}")

    #check if user has got all letters with an if _ it's not in the display list then end the game and tell them they won
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #import the stages from hangman_art.py and print the stages by fetching the amount of lifes got left
    from hangman_art import stages
      
    print(stages[lives])
