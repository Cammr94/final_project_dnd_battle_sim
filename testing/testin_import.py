# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:08:14 2019

@author: cammr
"""

#import dice_rolls

def enter_to_continue():
    input("~Enter To Continue~")
    
    return


def character_selection():
    input("(Hit enter to progress through un-prompted texts!)")
    input("Welcome fellow adventureer!")
    input("I hope you are ready for glory and honor on the battlefield!")
    print("\nPlease do tell me friend, have you been here before?\nOr are you new around these parts?")
    
    print("(A) New Character")
    print("(B) Load Previous Character", end = '')
    char_choice = input("Choose: ")
    
    valid_answer = False
    while valid_answer != True:
        if char_choice.isalpha() == False:
            input("Uhh, pardon me? Could you repeat that? ~Invalid Choice~")
            print("(A) New Character")
            print("(B) Load Previous Character", end = '')
            char_choice = input("Choose: ")
        
        elif char_choice.upper() == 'A' or char_choice.upper() == 'B':
            valid_answer = True
        else:
            input("Uhh, pardon me? Could you repeat that? ~Invalid Choice~")
            print("(A) New Character")
            print("(B) Load Previous Character", end = '')
            char_choice = input("Choose: ")
            
    if char_choice.upper() == 'A':
        input("Ahhh a newcomer!\nWelcome welcome!")
        input("Now...Tell me about your self")
        create_chaaracter()
        
    elif char_choice.upper() == 'B':
        load_character()
    
    return
    
def create_chaaracter():
    print("In Create Char Mode")

def load_character():
    input("Oh its you! Welcome back...")
    input("...uh, remind me...")
    char_name_for_file = input("...who are you?\nYour Name: ")
    print(char_name_for_file)
    return

def main():
    character_selection()
    
    
main()