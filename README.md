# Number Guessing Game

## Overview

The Number Guessing Game is a command-line Python application where the computer generates a random number between 1 and 100, and the player tries to guess it within a limited number of attempts.

The game provides feedback after every guess, informing the player whether their guess is too high or too low.

Players can choose from three difficulty levels, each with a different number of attempts.

## Features

- Random number generation using Python's `random` module.
- Three difficulty levels:
  - Easy: 10 attempts.
  - Medium: 7 attempts.
  - Hard: 5 attempts.
- Feedback after every guess (Too High or Too Low).
- Tracks the number of attempts used.
- Displays remaining attempts.
- Handles invalid inputs using exception handling.
- Notifies the player when they win or run out of attempts.

## Technologies Used

- Python 
- Random module
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`)
- Functions
- Exception handling (`try`, `except`)
- User input and output

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate into the project folder

```bash
cd number_guessing_game
```

### 3. Run the application

```bash
python main.py
```

## How to Play

1. Start the game.
2. Choose your preferred difficulty level.
3. Enter a number between 1 and 100.
4. Follow the feedback:
   - Too High: Your guess is greater than the secret number.
   - Too Low: Your guess is smaller than the secret number.
5. Continue guessing until you find the correct number or run out of attempts.

## Project Structure

```
number_guessing_game/
│
├── main.py
└── README.md
```

## Learning Objectives

This project was developed to practice fundamental Python programming concepts, including:

- Defining and calling functions.
- Generating random numbers.
- Working with variables and user input.
- Using conditional statements.
- Implementing while loops.
- Counting attempts.
- Handling errors with try/except.
- Controlling program flow with break and continue.


## License

This project is open-source and available for learning and educational purposes.