# Hangman in Python

I've done this school team project at Codecool's tester course.

## Story

Let's hang somebody! Implement the popular [Hangman](<https://en.wikipedia.org/wiki/Hangman_(game)>) game.

## Tasks

1. Implement the `play(word, lives)` function as a basic hangman game.
    - The function uses the `word` parameter as the word to guess and the `lives` parameter as the number of available mistakes.
    - The initial game state is displayed as `_ _ _ _ _ _ _ _` (one underscore for each letter in `word`).
    - The game state is displayed as `_ o d _ _ o o _` if letters 'd' and 'o' are revealed.
    - It is possible to make guesses, and letters that occur in the word are revealed.
    - When a guessed letter does not occur in `word`, the player loses one life.
    - When a guess is repeated (regardless of its occurrences), the player is notified, and nothing happens.
    - When a guess is wrong (either a new or a repeated letter), the previous wrong letters are shown to the user.
    - The player wins when all letters in `word` are revealed.
    - The player loses when the number of wrong guesses is higher than the value of `lives` (not counting repeated guesses).
    - When the player types `'quit'` as input, the program says good-bye and terminates.

2. The game uses a random word from a pre-defined word collection.
    - The game randomly picks a word at each run.
    - The game randomly picks a country from `countries-and-capitals.txt`.