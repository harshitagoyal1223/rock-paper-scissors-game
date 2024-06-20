# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:06:01 2024

@author: harsh
"""
import random

def get_user_choice():
    user_choice = input("Enter user input Stone, Paper, Scissors: ").lower()
    if user_choice in ["rock", "paper", "scissors"]:
      return user_choice
    else:
       print("Invalid choice")
      
def get_computer_choice():
   choices = ["rock", "paper", "scissors"]
   return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or\
        (user_choice == "scissors" and computer_choice == "paper") or\
            (user_choice == "paper" and computer_choice == "rock"):
                return "You Win!"
    else:
                return "You Lose!"
            
def start_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer's choice:",computer_choice)
    result = determine_winner(user_choice,computer_choice)
    print("Result is: ",result)
    
start_game()
    