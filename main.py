import random
from art import logo
#making these the global variables to call them anywhere below
easy_game = 10
hard_game = 5

print("Welcome to the Number Guessing Game!")

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

#def function for difficulty level and return whether it will be a easy or hard game (5 or 10 turns...also return is used to be an output of the function)
def set_difficulty():
    difficulty_level = input("Would you like to play the game on 'easy' or 'hard'? ")
    if difficulty_level == "easy":
        return easy_game 
    else:
        return hard_game

#def function to determine how user_choice compares with random_choice to see if user needs to keep guessing...also returns number of turns remaining  
def compare(user_guess, random_choice, turns): 
    if user_guess < random_choice:
        print("Too Low")
        #after setting turns to 0...return turns - 1 to countdown by 1 after each turn...will do it after elif statement too because if guess is too high or low they lose a turn...won't lose a turn if wins
        return turns - 1
    elif user_guess > random_choice:
        print("Too High")
        return turns - 1
    else:
        print(f"Winner, the answer was {random_choice}!")
    
#def function to play game within         
def play():
    print(logo)

    print("I'm thinking of a number between 1 and 100.")
    random_choice = random.choice(num_list)
    #calling function which triggers input within function, the output is the actual number of turns they have
    turns = set_difficulty()

    #declaring user_guess outside of while loop and setting it to 0 to start it off
    user_guess = 0
    #use !=(not equal) instead of using end of game variable
    while user_guess != random_choice:
        print(f"You have {turns} guesses remaining to guess the number.")
        user_guess = int(input("Make a guess. "))
        #calling function in variable turns will update the turns = set_difficulty() each guess to tell how many turns is remaining
        turns = compare(user_guess, random_choice, turns)
        if turns == 0:
            print("You are out of guesses, You lose!") 
            #writing return just exits the loop so make a guess won't pop up after user runs out of turns
            return
        #adding guess again statement after make a guess if user got answer wrong
        elif user_guess != random_choice:
            print("Guess again.")
while input("Type 'y' if you want to play again or 'n' to decline. ") == "y":   
    play()
    
        



#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

