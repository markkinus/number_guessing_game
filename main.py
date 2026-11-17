import random

def get_random_number():
    return random.randint(1,100)
# print(get_random_number())

secret_number = get_random_number()

print ("Number Guessing Game")
print ("I'm thinking of a number between 1 and 100.")

# difficulty levels

print("\nChoose a difficulty level:")
print("1 - Easy - 10 attempts")
print("2 - Medium - 7 attempts")
print("3 - Hard - 5 attempts")

difficulty = input("Enter your choice (1, 2, or 3): ")

if difficulty == "1":
    max_attempts = 10
    print("You have chosen Easy difficulty. You have 10 attempts to guess the number.")

elif difficulty == "2":
    max_attempts = 7
    print("You have chosen Medium difficulty. You have 7 attempts to guess the number.")

elif difficulty == "3":
    max_attempts = 5
    print("You have chosen Hard difficulty. You have 5 attempts to guess the number.")

else:
    print("Invalid choice. Defaulting to Easy difficulty.")
    max_attempts = 10

# initialize attempts
attempts = 0    

# input to guess a number between 1 and 100
guess = int(input("Guess a number between 1 and 100: "))
attempts += 1
    
# loop until the guess is correct
while guess != secret_number and attempts < max_attempts:
    
    if guess < secret_number:
        print("Too low")
    else:
        print("Too high")

    # calculate and display the remaining attempts
    remaining_attempts = max_attempts - attempts
    print(f"You have {remaining_attempts} attempts left.")

    guess = int(input("Guess again: "))
    attempts += 1 

# check if the guess is correct or if the user ran out of attempts
if guess == secret_number:
    print("You got it!")
    print(f"It took you {attempts} attempts.")
else:
    print("You ran out of attempts.")
    print(f"The number was {secret_number}.")
