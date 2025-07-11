#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Candidate nr: 357
Question1.py

Word Guessing Game

Read a list of words from a file, pick one at random, and let the player guess
letters until they either reveal the word or exhaust their allowed wrong guesses.
"""

import random


def load_words(path):
    """Returns a list of non-empty stripped lines, or None if file not found."""
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
        return None
    
    
class WordGuessGame:
    """Handles one session of the word guessing game."""
    
    def __init__(self, word_list):
        """Select a random secret word from a non-empty list."""
        if not word_list:
            raise ValueError("No words available to play with.")
        idx = random.randint(0, len(word_list) - 1)
        self._secret_word = word_list[idx].lower()
        self._max_wrong_guesses = len(self._secret_word)
        self._wrong_guesses = 0
        self._guessed_letters = []
    
    def secret(self):
        """Return a secret word for end-of-game reveal."""
        return self._secret_word
    
    def remaining(self):
        """Return how many wrong guesses remain."""
        return self._max_wrong_guesses - self._wrong_guesses
    
    def show_progress(self):
        """Return the secret word with unguessed letters as underscores."""
        return ' '.join(
            c if c in self._guessed_letters else '_'
            for c in self._secret_word
        )
    
    def guess_letter(self, letter):
        """Process a letter guess and return feedback string."""
        if len(letter) != 1 or not letter.isalpha():
            return "Enter exactly one alphabetic letter."
        letter = letter.lower() # normalize to lowercase
        if letter in self._guessed_letters:
            return f"You already guessed '{letter}'."
        self._guessed_letters.append(letter)
        if letter in self._secret_word:
            return None
        self._wrong_guesses += 1
        return "Sorry that letter is not in the word."
        
    def is_won(self):
        """Return True if all letters have been guessed."""
        return all(c in self._guessed_letters for c in self._secret_word)
    
    def is_lost(self):
        """Return True if wrong guesses >= maximum allowed."""
        return self._wrong_guesses >= self._max_wrong_guesses
    
    
def main():
    """Run a single game session, loads words, initialize game, and process guesses."""
    print("-" * 30)
    print("Welcome to Word Guessing Game!")
    print("-" * 30)
    
    path = input("Enter the name or path to word list file (e.g., word.txt): ").strip()
    words = load_words(path)
    if not words:
        return

    game = WordGuessGame(words)
    print()
    print(f"The word you need to guess has '{len(game.secret())}' characters.")
    print(f"You have now {game.remaining()} guesses.")
    print()
    print(game.show_progress())
    print()
        
    # Game loop
    while not game.is_won() and not game.is_lost():
        guess = input("Guess a character: ").strip()
        print()
        feedback = game.guess_letter(guess) # Evaluate the guess
        if feedback:
            print(feedback)
            print()
        print(game.show_progress()) # Show current progress
        print()
        print(f"You have {game.remaining()} guess(es) left.")
        print("-" * 30)
        print()
    
    # Prints game results
    if game.is_won():
       print(f'You found the word --> "{game.secret()}"')
       print("Congratulations! You won!")
    else:
       print("Sorry! You lost.")
       print(f'The word is --> "{game.secret()}"')
      
        
if __name__ == "__main__":
    main()