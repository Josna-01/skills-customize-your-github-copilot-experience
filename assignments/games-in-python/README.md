
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You'll practice string manipulation, conditionals, and random selection by creating an interactive game where players guess letters to reveal a hidden word.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the game by creating a word list and implementing a function that randomly selects a word for the player to guess.

#### Requirements
Completed program should:

- Create a predefined list of words to choose from
- Implement a function to randomly select a word from the list
- Initialize game variables (word, guessed letters, remaining attempts)
- Display the initial hidden word state (_ _ _ format)

### 🛠️ Letter Guessing and Progress Display

#### Description
Implement the core game loop where players guess letters and see their progress updated.

#### Requirements
Completed program should:

- Accept letter guesses from the player using `input()`
- Display the current word progress after each guess
- Track which letters have been guessed
- Provide feedback on correct and incorrect guesses
- Update remaining attempts count

### 🛠️ Game Win/Lose Logic

#### Description
Complete the game by implementing win and lose conditions with appropriate messaging.

#### Requirements
Completed program should:

- End the game when the word is correctly guessed
- End the game when attempts are exhausted
- Display a win message with the completed word
- Display a lose message with the correct word revealed
- Offer to play again
