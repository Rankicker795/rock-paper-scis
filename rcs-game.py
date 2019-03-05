import os
import sys
import random

choice_tup = ("Rock","Paper","Scissors")

def user_input():
    print("Enter rock, paper, or scissors")
    selection = input("Choice: ")
    if (selection == "rock" or selection == "Rock"):
        select_int = 1
    elif (selection == "paper" or selection == "Paper"):
        select_int = 2
    elif (selection == "scissors" or selection == "Scissors"):
        select_int = 3
    else:
        select_int = False
    return select_int

def comp_input():
    comp_choice = random.randint(1,3)
    return comp_choice

def game_decision(select_int,comp_choice):
    a = select_int
    b = comp_choice
    if (a == 1):
        if (b == 1):
            str_result = "TIE!"
        elif (b == 2):
            str_result = "LOSE!"
        else:
            str_result = "WIN!"
    if (a == 2):
        if (b == 1):
            str_result = "WIN!"
        elif (b == 2):
            str_result = "TIE!"
        else:
            str_result = "LOSE!"
    if (a == 3):
        if (b == 1):
            str_result = "LOSE!"
        elif (b == 2):
            str_result = "WIN!"
        else:
            str_result = "TIE!"
    return str_result

def main():
    print("Welcome to the Rock-Paper-Scissors Python Game!!!")
    game_loop = False
    while (game_loop == False):
        select_int = False
        while (select_int == False):
            select_int = user_input()
            if not select_int:
                print("Invalid choice. Try again.")
        comp_choice = comp_input()
        str_result = game_decision(select_int,comp_choice)
        print(f"User: {choice_tup[select_int-1]} Comp: {choice_tup[comp_choice-1]} Result: {str_result}")
        print("Play again?")
        game_inp = input("Yes or no: ")
        if (game_inp == "no" or game_inp == "No" or game_inp == "NO"):
            game_loop = True
    print("Thank you for playing! - REA")
     
if __name__ =="__main__":
    main()
