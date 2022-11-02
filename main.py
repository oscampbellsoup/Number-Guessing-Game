# Import random module to give us a number to guess
import random
# Starting messages
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# Ask for difficulty input
while True:
    try:
        difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
    except:
        print("Invalid input. Please re-enter your difficulty.")
        continue
    if difficulty == 'easy':
        guess_attempts = 10
        break
    elif difficulty == 'hard':
        guess_attempts = 5
        break
    else:
        print("Invalid input. Please re-enter your difficulty.")
        continue
# Pick random nummber between 1 and 100
number = random.randint(1, 100)
# Track previous guesses
guesses = []
# Define guess retrieval function
def guess_retrieval():
    global guess
    global guess_attempts
    global guesses
    while True:
        try:
            guess = int(input("Make a guess: "))
        except:
            print("Invalid input. Please re-enter your guess.")
            continue
        if guess < 1:
            print("The number I'm thinking of is between 1 and 100. I'll give you another free guess.")
            continue
        elif guess > 100:
            print("The number I'm thinking of is between 1 and 100. I'll give you another free guess.")
            continue
        elif guess in guesses:
            print("You have already guessed this number. I'll give you another free guess.")
            continue
        else:
            guesses.append(guess)
            guess_attempts -= 1
            break
# Define guess response function
def guess_ask_and_response():
    guess_retrieval()            
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        exit()
# Create while loop to last duration of given guess attempts
while guess_attempts != 0:
        print(f"You have {guess_attempts} attempts remaining to guess the number.")
        guess_ask_and_response()
# Lose response
if guess_attempts == 0:
    print("You've run out of guesses, you lose.")
            
            