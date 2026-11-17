import random

def get_random_number():
    return random.randint(1,100)
# print(get_random_number())

secret_number = get_random_number()

attempts = 0    

# input to guess a number between 1 and 100
guess = int(input("Guess a number between 1 and 100: "))
attempts += 1
    
# loop until the guess is correct
while guess != secret_number:
    
    if guess < secret_number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess again: "))
    attempts += 1
    
print("You got it!")
print(f"It took you {attempts} attempts.")