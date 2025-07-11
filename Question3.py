#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Candidate nr: 357
Question3.py

Bank Account Management System

Menu class to display options and retrieve the user´s choice.
BankAccount class for deposit, withdraw, interest, and get balance.
"""


class Menu:
    """Presents a menu of options and retrieves a validated choice."""
    
    def __init__(self):
        """Initialize the menu by registering it´s base functions."""
        self.options = []
        self.add_option("Open a new account")
        self.add_option("Deposit money into your account")
        self.add_option("Withdraw money from your account")
        self.add_option("Add interests to your account")
        self.add_option("Get the current balance of your account")
        self.add_option("Quit")
        

    def add_option(self, option):
        """Add a new option to the menu."""
        self.options.append(option)

    def get_input(self):
        """Display the menu and prompt the user for a selection."""
        print()
        for idx, text in enumerate(self.options, start=1):
            print(f"{idx} {text}")
        
        print()
        choice = input(f"Select an option (1-{len(self.options)}): ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(self.options):
                return num
        return None


class BankAccount:
    """Represents a bank account."""

    def __init__(self, balance=0.0):
        """Initialize the account with a starting balance."""
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw money if enough funds."""
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def add_interest(self, rate):
        """Apply interest to the account based on a rate (0.07 for 7%)."""
        self.balance += self.balance * rate

    def get_balance(self):
        """Return the current account balance."""
        return self.balance


def main():
    """Run the bank account system with user interaction."""
    print("-" * 40)
    print("Welcome to Bank Account Management System!")
    print("-" * 40)
    print()
    
    interest_rate = 0.07
    menu = Menu()
    account = None

    while True:
        choice = menu.get_input()
        if choice is None:
            print("Invalid selection. Please enter a valid number.")
            continue
        
        # 1) Open account    
        if choice == 1:
            account = BankAccount()
            print("New account opened. Balance is $0.00.")
        
        # 2) Deposit 
        elif choice == 2:
            if account is None:
                print("No account exists. Please open one first.")
            else:
                amt_str = input("Enter amount to deposit: ").strip()
                try:
                    amount = float(amt_str)
                    if amount < 0:
                        raise ValueError
                    account.deposit(amount)
                    print(f"Deposited ${amount:.2f}.")
                except ValueError:
                    print("Invalid amount.")
        
        # 3) Withdraw
        elif choice == 3:
            if account is None:
                print("No account exists. Please open one first.")
            else:
                amt_str = input("Enter amount to withdraw: ").strip()
                try:
                    amount = float(amt_str)
                    if amount < 0:
                        raise ValueError
                except ValueError:
                        print("Invalid amount. Please enter a positive number.")
                else:
                    if account.withdraw(amount):
                        print(f"Withdrew ${amount:.2f}.")
                    else:
                        print("Insufficient funds.")

        # 4) Add interest
        elif choice == 4:
            if account is None:
                print("No account exists. Please open one first.")
            else:
                account.add_interest(interest_rate)
                print(f"Interest of {interest_rate*100:.1f}% applied.")

        # 5) Get Balance
        elif choice == 5:
            if account is None:
                print("No account exists. Please open one first.")
            else:
                bal = account.get_balance()
                print(f"Current balance: ${bal:.2f}")

        # 6) Quit
        elif choice == 6:
            print("Goodbye!")
            break
                        
        print()


if __name__ == "__main__":
    main()