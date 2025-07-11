#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Candidate nr: 357
Question4.py

Palindrome checker

Prompts the user for a string, normalizes it, and checks if it's a palindrome.
Ignores case, spaces, and non-alphanumeric characters.
"""


def clean_string(s):
    """Return a lowercase string containing only the alphanumeric characters from s."""
    result = ""
    for c in s:
        if c.isalnum():
            result += c.lower()
    return result

def is_palindrome(s):
    """
    Return True if the cleaned version of s is a palindrome.
    An empty cleaned string is not considered a palindrome here.
    """
    cleaned = clean_string(s)
    if not cleaned:
        return False
    return cleaned == cleaned[::-1] # Compare with reversed string


def main():
    """Prompt for input, check palindrome, and display a clear result message."""
    print("-" * 30)
    print("Welcome to Palindrome checker!")
    print("-" * 30)
    print()
    
    user_input = input("Enter a string to check: ").strip()
    cleaned = clean_string(user_input)
    
    if not cleaned:
        print("No letters or digits found. Nothing to check.")
    elif is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome!')
    else:
        print(f'"{user_input}" is not a palindrome.')


if __name__ == "__main__":
    main()