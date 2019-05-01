# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:08:14 2019

@author: cammr
"""



import dice_rolls #small program that houses all different Die Types ~My Creation
import string
import pickle
import random

import os #https://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python SOURCE 
#- To get current directory

#All Levels of players scaled to Lvl 10
CHAR_LEVEL = 10


#Base Choices for Armor, could be expanded upon later if needed/wanted to
#~~~~~Armor Base Stats~~~~~~~~~~~
NAT_ARMOR = 10
LEATHER_ARMOR_BASE = 11
STUDDED_LEATHER_ARMOR_BASE = 12
SCALE_MAIL_BASE = 14
HIDE_ARMOR_BASE = 12
CHAIN_MAIL_BASE = 16
PLATE_ARMOR_BASE = 18
SHIELD_AC_BONUS = 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Bonus to AC when charater chooses to defend
DEFEND_BONUS_AC = 5


#All base lvl 1 Hp for all classes found in DnD 5th Edition Players handbook
#~~~~~~~CLASSS'S BASE HP~~~~~~~~~
BARBARIAN_HP = 12
RANGER_HP = 10
PALADIN_HP = 10
ROGUE_HP = 8
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''First major chunk of the program where it allows the player to eithier 
load in a previously made character (made with this program only) or create one
from scratch.

It talks to the player with a lot of prompts in dialog to allow the user to progress
through it to their own speed.
'''

def character_selection():
    input("(Hit enter to progress through un-prompted texts!)")
    input("Welcome fellow adventureer!")
    input("I hope you are ready for glory and honor on the battlefield!")
    print("\nPlease do tell me friend, have you been here before?\nOr are you new around these parts?")
    
    print("(A) New Character")
    print("(B) Load Previous Character", end = '')
    char_choice = input("Choose: ")
    
    valid_answer = False
    

#Will make sure that the user enters in a valid choice to progress through.
    while valid_answer != True:
        if char_choice.isalpha() == False:
            input("Uhh, pardon me? Could you repeat that? ~Invalid Choice~")
            print("(A) New Character")
            print("(B) Load Previous Character", end = '')
            char_choice = input("Choose: ")
        
        elif len(char_choice) == 1 and char_choice.upper() == 'A' or char_choice.upper() == 'B':
            valid_answer = True
        else:
            input("Uhh, pardon me? Could you repeat that? ~Invalid Choice~")
            print("(A) New Character")
            print("(B) Load Previous Character", end = '')
            char_choice = input("Choose: ")
            


    if char_choice.upper() == 'A':
        player_dic = create_chaaracter()
        
    elif char_choice.upper() == 'B':
        player_dic = load_character()
    
    return player_dic
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
Function that will go through the basic and I mean basic steps of creating a 
character for this battlie sim.  It will follow basic DnD 5th Edition Character
creating rules found in the player handbook.

It will prompt the user at every step for information and choices of the character 
as it progresses through the proccess.

Some parts it will generate stats dependent on the info provided by the player

It will then at the end of the function save and output the created characters 
dictionary to a folder called 'character' within the directory that the main 
program is housed!
'''


def create_chaaracter():
    player_dic = {}
    input("Ahhh a newcomer!\nWelcome welcome!")
    input("Now...Tell me about your self")
    
    #Concatenate the name with a string to allow input conversations!

  
#Player choooses class and determines what function to be called forth for
#further character creation!'

    player_name = input("Your Name: ")
    player_dic["name"] = player_name
    
    print("Choose a class!")
    print("(A) Barbarian")
    print("(B) Ranger")
    print("(C) Paladin")
    print("(D) Rogue")
    
    class_choice = input("Choice: ")
    
    valid_answer = False
    
    while valid_answer != True:
        if class_choice.isalpha() == False:
            print("~Not a valid choice!~\n")
            print("Choose a class!")
            print("(A) Barbarian")
            print("(B) Ranger")
            print("(C) Paladin")
            print("(D) Rogue")
            
            class_choice = input("Choice: ")
            
        elif len(class_choice) > 1 or class_choice.upper() < 'A' or class_choice.upper() > 'D':
            print("~Not a valid choice!~\n")
            print("Choose a class!")
            print("(A) Barbarian")
            print("(B) Ranger")
            print("(C) Paladin")
            print("(D) Rogue")
            
            class_choice = input("Choice: ")
            
        else:
            valid_answer = True
            
    class_choice = class_choice.upper()
    if class_choice == 'A':
        player_dic['class'] = 'Barbarian'
        player_dic = barbarian_create(player_dic)

        
    elif class_choice == 'B':
        player_dic['class'] = 'Ranger'
        player_dic = ranger_create(player_dic)
        
    elif class_choice == 'C':
        player_dic['class'] = 'Paladin'
        player_dic = paladin_create(player_dic)
    else:
        player_dic['class'] = 'Rogue'
        player_dic = rogue_create(player_dic)
    
    attack_text = player_dic['name'] + ' draws their ' + player_dic['weapon'] + ' strikes the '
    player_dic['attack_text'] = attack_text
    
    save_player_char(player_dic)    
        
    return player_dic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Program that quickly outputs the character dictionary to be used at later date

def save_player_char(player_dic):
    current_dir = os.getcwd()
    char_name = player_dic['name']
    file_name = current_dir + '/characters/' + char_name.replace(' ', '_')
    file_object = open(file_name, 'wb')
    pickle.dump(player_dic, file_object)
    file_object.close()
    
    return            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Will roll and get a score for an ability and return that score
#It will also sort, and chop off the lowest roll and sum the rest
#Returning the total    

def get_ability_score():
    list_of_d6s = []
    for count in range(4):
        rolled_num = dice_rolls.roll_d6()
        list_of_d6s.append(rolled_num)
    list_of_d6s.sort()
    list_of_d6s.remove(list_of_d6s[0]) 
    
    total = 0
    for element in list_of_d6s:
        total += element
    return total    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A quick function that will take in an ability score and then return
#the matching modifer!    

def determine_modifers(ability_score):
    if ability_score == 20:
        modifer = 5
    elif ability_score == 18 or ability_score == 19:
        modifer = 4
    elif ability_score == 16 or ability_score == 17:
        modifer = 3
    elif ability_score == 14 or ability_score == 15:
        modifer = 2
    elif ability_score == 12 or ability_score == 13:
        modifer = 1
    elif ability_score == 10 or ability_score == 11:
        modifer = 0
    elif ability_score == 8 or ability_score == 9:
        modifer = -1
    elif ability_score == 6 or ability_score == 7:
        modifer = -2
    elif ability_score == 4 or ability_score == 5:
        modifer = -3        
    elif ability_score == 2 or ability_score == 3:
        modifer = -4
    else:
        modifer = -5
        
    return modifer

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Gets the HP for the current character depending on the character class
#and the rolled constitution modifer!    

def get_max_hp(con_mod, CLASS_HP):
    hp = CLASS_HP + con_mod     
    count = 1
    while count < CHAR_LEVEL - 1:
        count += 1
        rolled_hp = dice_rolls.roll_d12()
        hp += rolled_hp    

    return hp
#~~~~~~~~~~~~~~~~CLASS CREATING FUNCTIONS~~~~~~~~~~~~~

'''
The next 4 functions are all almost identical except for the armor, and weapon
choices for each of the classes.

I will throughly explain how each of the functions work within the Barbarian
class creating function!
'''


#/////////////Barbarian Class Creaton/////////////
    
def barbarian_create (player_dic):    
    print("Barbarian Choosen")
    
    
    #Rolling Abilities Scores
    str_score = get_ability_score()
    str_mod = determine_modifers(str_score)
    dex_score = get_ability_score()
    dex_mod = determine_modifers(dex_score)
    con_score = get_ability_score()
    con_mod = determine_modifers(con_score)
    
    #Rolling for HP
    #HP at First Level
    hp = get_max_hp(con_mod, BARBARIAN_HP)
    player_dic['hp_max'] = hp
    
    #Putting them into the Dictionary
    player_dic['str_score'] = str_score
    player_dic['str_mod'] = str_mod
    player_dic['dex_score'] = dex_score
    player_dic['dex_mod'] = dex_mod
    player_dic['con_score'] = con_score
    player_dic['con_mod'] = con_mod
    
   
    #Choosing Armor for player's character!
    #All info for all of these aromors are in player's handbook
    #Will also check to make sure it is a valid choice
    #By checking the length of Char/that its a letter/and if it meets the choice
    
    print("Choose your armor set!")
    print("(A) Unarmored - (Unarmored Defense Feature [10 + Dex Mod + Con Mod])")
    print("(B) Studded Leather (12 + Dex Mod)")
    print("(C) Scale Mail (14 + Dex Mod)")
    armor_choice = input ("Armor Choice: ")
    
    valid_answer = False
    while valid_answer != True:
        if armor_choice.isalpha() != True:
            input("~Not a valid choice~\n")
            print("Choose your armor set!")
            print("(A) Unarmored - (Unarmored Defense Feature [10 + Dex Mod + Con Mod])")
            print("(B) Studded Leather (12 + Dex Mod)")
            print("(C) Scale Mail (14 + Dex Mod)")
            armor_choice = input ("Armor Choice: ") 
            
        elif len(armor_choice) > 1 or armor_choice.upper() < 'A' and armor_choice.upper() > 'C':
            input("~Not a valid choice~\n")
            print("Choose your armor set!")
            print("(A) Unarmored - (Unarmored Defense Feature [10 + Dex Mod + Con Mod])")
            print("(B) Studded Leather (12 + Dex Mod)")
            print("(C) Scale Mail (14 + Dex Mod)")
            armor_choice = input ("Armor Choice: ")
    
        else:
            valid_answer = True        
        
    #Determing AC value based on players choice!
    #All Info for armor is a Constant above the program
    #Again all info in Dnd 5E Players Handbook
    if armor_choice.upper() == 'A':
        AC = NAT_ARMOR + dex_mod + con_mod
    elif armor_choice.upper() == 'B':
        AC = STUDDED_LEATHER_ARMOR_BASE + dex_mod 
    elif armor_choice.upper() == 'C':
        AC = SCALE_MAIL_BASE
        if dex_mod > 2:
            AC += 2
        else:
            AC += dex_mod
    
    #Storing the AC to the player dictionary        
    player_dic['AC'] = AC
    
    #Weapon Choice Time!
    #Will also make sure the player's choice is valid!
    print("Choose your weapon!")
    print("(A) Battleaxe (1d10 + Str Mod)")
    print("(B) Warhammer (1d10 + Str Mod)")
    print("(C) Dual Hanaxes (2d6 + Str Mod)")
    weapon_choice = input("Weapon Choice: ")
    
    valid_answer = False
    
    while valid_answer != True:
        if weapon_choice.isalpha() != True:
            input("~Not a valid choice~\n")
            print("Choose your weapon!")
            print("(A) Battleaxe (1d10 + Str Mod)")
            print("(B) Warhammer (1d10 + Str Mod)")
            print("(C) Dual Hanaxes (2d6 + Str Mod)")
            weapon_choice = input("Weapon Choice: ")  
            
        elif len(weapon_choice) > 1 or weapon_choice.upper() < 'A' and weapon_choice.upper() > 'C':
            input("~Not a valid choice~\n")
            print("Choose your weapon!")
            print("(A) Battleaxe (1d10 + Str Mod)")
            print("(B) Warhammer (1d10 + Str Mod)")
            print("(C) Dual Hanaxes (2d6 + Str Mod)")
            weapon_choice = input("Weapon Choice: ")
            
        else:
            valid_answer = True
    
    #Determining Weapon and weapon's damage die        
    if weapon_choice.upper() == 'A':
        weapon = 'Battleaxe'
        weapon_dmg_die = '1d10'
        
    elif weapon_choice.upper() == 'B':
        weapon = 'Warhammer'
        weapon_dmg_die = '1d10'
        
    elif weapon_choice.upper() == 'C':
        weapon = 'Dual Handaxes'
        weapon_dmg_die = '2d6'
        
    #Storing new data to player's dictionary
    player_dic['weapon'] = weapon
    player_dic['weapon_dmg_die'] = weapon_dmg_die
    
    #May go back and make this a check for all weapons and all classes
    #BUT FOR NOW ADD IT TO END OF EACH CLASS
    player_dic['key_mod'] = str_mod
    
    
    
    return player_dic    
    
#/////////////////////////////////////////////////


#/////////////Ranger Class Creation///////////////

def ranger_create (player_dic):
    print("Ranger Choosen")
    
    
    
    #Rolling Abilities Scores
    str_score = get_ability_score()
    str_mod = determine_modifers(str_score)
    dex_score = get_ability_score()
    dex_mod = determine_modifers(dex_score)
    con_score = get_ability_score()
    con_mod = determine_modifers(con_score)
    
    #Rolling for HP
    #HP at First Level
    hp = get_max_hp(con_mod, RANGER_HP)
    player_dic['hp_max'] = hp    
    
    #Putting them into the Dictionary
    player_dic['str_score'] = str_score
    player_dic['str_mod'] = str_mod
    player_dic['dex_score'] = dex_score
    player_dic['dex_mod'] = dex_mod
    player_dic['con_score'] = con_score
    player_dic['con_mod'] = con_mod
    
   
    #Choosing Armor for player's character!
    print("Choose your armor set!")
    print("(A) Leather Armor (11 + Dex Mod)")
    print("(B) Hide Armor (12 + Dex Mod)")
    armor_choice = input ("Armor Choice: ")
    
    valid_answer = False
    while valid_answer != True:
        if armor_choice.isalpha() != True:
            input("~Not a valid choice~\n")
            print("Choose your armor set!")
            print("(A) Leather Armor (11 + Dex Mod)")
            print("(B) Hide Armor (12 + Dex Mod)")
            armor_choice = input ("Armor Choice: ") 
            
        elif len(armor_choice) > 1 or armor_choice.upper() < 'A' and armor_choice.upper() > 'B':
            input("~Not a valid choice~\n")
            print("Choose your armor set!")
            print("(A) Leather Armor (11 + Dex Mod)")
            print("(B) Hide Armor (12 + Dex Mod)")
            armor_choice = input ("Armor Choice: ")
    
        else:
            valid_answer = True        
        
    #Determing AC value based on players choice!
    if armor_choice.upper() == 'A':
        AC = LEATHER_ARMOR_BASE + dex_mod
    elif armor_choice.upper() == 'B':
        AC = HIDE_ARMOR_BASE + dex_mod 
    
    #Storing the AC to the player dictionary        
    player_dic['AC'] = AC
    
    #Weapon Choice Time!
    print("Choose your weapon!")
    print("(A) Longbow (1d8 + Dex Mod)")
    print("(B) Longsword (1d10 + Str Mod")
    print("(C) Shortsword & Shield (1d6 + Str Mod & +2 to AC)")
    weapon_choice = input("Weapon Choice: ")
    
    valid_answer = False
    
    while valid_answer != True:
        if weapon_choice.isalpha() != True:
            input("~Not a valid choice~\n")
            print("Choose your weapon!")
            print("(A) Longbow (1d8 + Dex Mod)")
            print("(B) Longsword (1d10 + Str Mod")
            print("(C) Shortsword & Shield (1d6 + Str Mod & +2 to AC)")
            weapon_choice = input("Weapon Choice: ")  
            
        elif len(weapon_choice) > 1 or weapon_choice.upper() < 'A' and weapon_choice.upper() > 'C':
            input("~Not a valid choice~\n")
            print("Choose your weapon!")
            print("(A) Longbow (1d8 + Dex Mod)")
            print("(B) Longsword (1d10 + Str Mod")
            print("(C) Shortsword & Shield (1d6 + Str Mod & +2 to AC)")
            weapon_choice = input("Weapon Choice: ")
            
        else:
            valid_answer = True
    
    #Determining Weapon and weapon's damage die        
    if weapon_choice.upper() == 'A':
        weapon = 'Longbow'
        weapon_dmg_die = '1d8'
        player_dic['key_mod'] = dex_mod
        
    elif weapon_choice.upper() == 'B':
        weapon = 'Longsword'
        weapon_dmg_die = '1d10'
        player_dic['key_mod'] = str_mod
        
    elif weapon_choice.upper() == 'C':
        weapon = 'Shortsword'
        weapon_dmg_die = '1d6'
        player_dic['key_mod'] = dex_mod
        AC += SHIELD_AC_BONUS
        player_dic['AC'] = AC
        
    #Storing new data to player's dictionary
    player_dic['weapon'] = weapon
    player_dic['weapon_dmg_die'] = weapon_dmg_die
    
    
    
    return player_dic
    
#///////////////////////////////////////////////
    

#///////////Paladin Class Creation///////////////

def paladin_create (player_dic):
    print("Paladin Choosen")
    
    #Rolling Abilities Scores
    str_score = get_ability_score()
    str_mod = determine_modifers(str_score)
    dex_score = get_ability_score()
    dex_mod = determine_modifers(dex_score)
    con_score = get_ability_score()
    con_mod = determine_modifers(con_score)
    
    #Rolling for HP
    #HP at First Level
    hp = get_max_hp(con_mod, PALADIN_HP)
    player_dic['hp_max'] = hp
    
    #Putting them into the Dictionary
    player_dic['str_score'] = str_score
    player_dic['str_mod'] = str_mod
    player_dic['dex_score'] = dex_score
    player_dic['dex_mod'] = dex_mod
    player_dic['con_score'] = con_score
    player_dic['con_mod'] = con_mod
    
   
    #Choosing Armor for player's character!
    print("Choose your armor set!")
    print("(A) Chain Mail (16 AC)")
    print("(B) Studded Leather (12 + Dex Mod)")
    print("(C) Plate (18 AC)")
    armor_choice = input ("Armor Choice: ")
    
    valid_answer = False
    while valid_answer != True:
        if armor_choice.isalpha() != True:
            input("~Not a valid choice~\n")
            print("Choose your armor set!")
            print("(A) Chain Mail (16 AC)")
            print("(B) Studded Leather (12 + Dex Mod)")
            print("(C) Plate (18 AC)")
            armor_choice = input ("Armor Choice: ") 
            
        elif len(armor_choice) > 1 or armor_choice.upper() < 'A' and armor_choice.upper() > 'C':
            input("~Not a valid choice~\n")
            print("Choose your armor set!")
            print("(A) Chain Mail (16 AC)")
            print("(B) Studded Leather (12 + Dex Mod)")
            print("(C) Plate (18 AC)")
            armor_choice = input ("Armor Choice: ")
    
        else:
            valid_answer = True        
        
    #Determing AC value based on players choice!
    if armor_choice.upper() == 'A':
        AC = CHAIN_MAIL_BASE
    elif armor_choice.upper() == 'B':
        AC = STUDDED_LEATHER_ARMOR_BASE + dex_mod 
    elif armor_choice.upper() == 'C':
        AC = PLATE_ARMOR_BASE
    
    #Storing the AC to the player dictionary        
    player_dic['AC'] = AC
    
    #Weapon Choice Time!
    print("Choose your weapon!")
    print("(A) Mace & Shield (1d6 + Str Mod & +2 AC)")
    print("(B) Flail (1d8 + Str Mod)")
    print("(C) Morningstar 1d8 + Str Mod)")
    weapon_choice = input("Weapon Choice: ")
    
    valid_answer = False
    
    while valid_answer != True:
        if weapon_choice.isalpha() != True:
            input("~Not a valid choice~\n")
            print("Choose your weapon!")
            print("(A) Mace & Shield (1d6 + Str Mod & +2 AC)")
            print("(B) Flail (1d8 + Str Mod)")
            print("(C) Morningstar 1d8 + Str Mod)")
            weapon_choice = input("Weapon Choice: ")  
            
        elif len(weapon_choice) > 1 or weapon_choice.upper() < 'A' and weapon_choice.upper() > 'C':
            input("~Not a valid choice~\n")
            print("Choose your weapon!")
            print("(A) Mace & Shield (1d6 + Str Mod & +2 AC)")
            print("(B) Flail (1d8 + Str Mod)")
            print("(C) Morningstar 1d8 + Str Mod)")
            weapon_choice = input("Weapon Choice: ")
            
        else:
            valid_answer = True
    
    #Determining Weapon and weapon's damage die        
    if weapon_choice.upper() == 'A':
        weapon = 'Mace'
        weapon_dmg_die = '1d6'
        AC += 2
        player_dic['AC'] = AC
        
    elif weapon_choice.upper() == 'B':
        weapon = 'Flail'
        weapon_dmg_die = '1d8'
        
    elif weapon_choice.upper() == 'C':
        weapon = 'Morningstar'
        weapon_dmg_die = '1d8'
        
    #Storing new data to player's dictionary
    player_dic['weapon'] = weapon
    player_dic['weapon_dmg_die'] = weapon_dmg_die
    
    #May go back and make this a check for all weapons and all classes
    #BUT FOR NOW ADD IT TO END OF EACH CLASS
    player_dic['key_mod'] = str_mod
    
    
    
    return player_dic     
    
#///////////////////////////////////////////////


#////////////Rogue Class Creation///////////////    
    
def rogue_create (player_dic):
    print("Rogue Choosen")
    
    #Rolling Abilities Scores
    str_score = get_ability_score()
    str_mod = determine_modifers(str_score)
    dex_score = get_ability_score()
    dex_mod = determine_modifers(dex_score)
    con_score = get_ability_score()
    con_mod = determine_modifers(con_score)
    
    #Rolling for HP
    #HP at First Level
    hp = get_max_hp(con_mod, ROGUE_HP)
    player_dic['hp_max'] = hp
    
    #Putting them into the Dictionary
    player_dic['str_score'] = str_score
    player_dic['str_mod'] = str_mod
    player_dic['dex_score'] = dex_score
    player_dic['dex_mod'] = dex_mod
    player_dic['con_score'] = con_score
    player_dic['con_mod'] = con_mod
    
   
    #Choosing Armor for player's character!
    print("Choose your armor set!")
    print("(A) Leather Armor (11 + Dex Mod)")
    print("(B) Studded Leather (12 + Dex Mod)")
    print("(C) Hide Armor (12 + Dex)")
    armor_choice = input ("Armor Choice: ")
    
    valid_answer = False
    while valid_answer != True:
        if armor_choice.isalpha() != True:
            input("~Not a valid choice~\n")
            print("Choose your armor set!")
            print("(A) Leather Armor (11 + Dex Mod)")
            print("(B) Studded Leather (12 + Dex Mod)")
            print("(C) Hide Armor (12 + Dex)")
            armor_choice = input ("Armor Choice: ") 
            
        elif len(armor_choice) > 1 or armor_choice.upper() < 'A' and armor_choice.upper() > 'C':
            input("~Not a valid choice~\n")
            print("Choose your armor set!")
            print("(A) Leather Armor (11 + Dex Mod)")
            print("(B) Studded Leather (12 + Dex Mod)")
            print("(C) Hide Armor (12 + Dex)")
            armor_choice = input ("Armor Choice: ")
    
        else:
            valid_answer = True        
        
    #Determing AC value based on players choice!
    if armor_choice.upper() == 'A':
        AC = LEATHER_ARMOR_BASE + dex_mod
    elif armor_choice.upper() == 'B':
        AC = STUDDED_LEATHER_ARMOR_BASE + dex_mod 
    elif armor_choice.upper() == 'C':
        AC = HIDE_ARMOR_BASE 
        if dex_mod > 2:
            AC += 2
        else:
            AC += dex_mod
    
    #Storing the AC to the player dictionary        
    player_dic['AC'] = AC
    
    #Weapon Choice Time!
    print("Choose your weapon!")
    print("(A) Dual Daggers (2d4 + Dex Mod)")
    print("(B) Light Crossbow (1d8 + Dex Mod)")
    print("(C) Scimitar (1d6 + Dex Mod)")
    weapon_choice = input("Weapon Choice: ")
    
    valid_answer = False
    
    while valid_answer != True:
        if weapon_choice.isalpha() != True:
            input("~Not a valid choice~\n")
            print("Choose your weapon!")
            print("(A) Dual Daggers (2d4 + Dex Mod)")
            print("(B) Light Crossbow (1d8 + Dex Mod)")
            print("(C) Scimitar (1d6 + Dex Mod)")
            weapon_choice = input("Weapon Choice: ")  
            
        elif len(weapon_choice) > 1 or weapon_choice.upper() < 'A' and weapon_choice.upper() > 'C':
            input("~Not a valid choice~\n")
            print("Choose your weapon!")
            print("(A) Dual Daggers (2d4 + Dex Mod)")
            print("(B) Light Crossbow (1d8 + Dex Mod)")
            print("(C) Scimitar (1d6 + Dex Mod)")
            weapon_choice = input("Weapon Choice: ")
            
        else:
            valid_answer = True
    
    #Determining Weapon and weapon's damage die        
    if weapon_choice.upper() == 'A':
        weapon = 'Dual Daggers'
        weapon_dmg_die = '2d4'
        
    elif weapon_choice.upper() == 'B':
        weapon = 'Light Crossbow'
        weapon_dmg_die = '1d8'
        
    elif weapon_choice.upper() == 'C':
        weapon = 'Scimitar'
        weapon_dmg_die = '1d6'
        
    #Storing new data to player's dictionary
    player_dic['weapon'] = weapon
    player_dic['weapon_dmg_die'] = weapon_dmg_die
    
    #May go back and make this a check for all weapons and all classes
    #BUT FOR NOW ADD IT TO END OF EACH CLASS
    player_dic['key_mod'] = dex_mod
    
    
    
    return player_dic 
    
#///////////////////////////////////////////////    
       

#~~~~~~~~~~~~~~~~~~~~~~END OF CLASS FUNCTIONS~~~~~~~~~~~~~~

def load_character():
    input("Oh its you! Welcome back...")
    input("...uh, remind me...")
    current_dir = os.getcwd() #import os #https://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python SOURCE
    char_found = False
    while char_found != True:
        char_name = input("...who are you?\nYour Name: ")
        char_name_file = char_name.replace(' ', '_')
        file_path = current_dir + '/characters/' + char_name_file
        
        try:
            char_file_object = open(file_path, 'rb')
        except IOError:
            input("Uhh, I've never heard of you stranger? ~Character Not Found~")
        else:
            char_found = True
            
    player_dic = pickle.load(char_file_object)
    return player_dic


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def picking_enemy():
    easy_enemies_list = ['Skeleton', 'Ghast', 'Hobgoblin Captain', 'Bandit Captain']
    normal_enemies_list = ['Gnoll', 'Werewolf', 'Orog']
    
    print("Pick your challenge fighter!")
    print("(A) Easy Fight")
    print("(B) Normal Fight")
    player_diff_choice = input("Your choice: ")
    valid_answer = False
    
    while valid_answer != True: 
        if player_diff_choice.isalpha() != True:
            input("~Not a valid choice~")
            print("Pick your challenge fighter!")
            print("(A) Easy Fight")
            print("(B) Normal Fight")
            player_diff_choice = input("Your choice: ")
            
        elif len(player_diff_choice) > 1 or player_diff_choice.upper() < 'A' and player_diff_choice.upper() > 'B':
            input("~Not a valid choice~")
            print("Pick your challenge fighter!")
            print("(A) Easy Fight")
            print("(B) Normal Fight")
            player_diff_choice = input("Your choice: ")
            
        else:
           valid_answer = True
           
    enemy_found = False
    enemy_dic = {}
    while enemy_found != True:
        if player_diff_choice.upper() == 'A':
            rand_num = random.randint(0, 3)
            enemy_name = easy_enemies_list[rand_num]
            enemy_dic = load_enemy(enemy_name)            
            
        elif player_diff_choice.upper() == 'B':
            rand_num = random.randint(0, 2)
            enemy_name = normal_enemies_list[rand_num]
            enemy_dic = load_enemy(enemy_name)            
        
        if enemy_dic != {}:
            enemy_found = True
    
    return enemy_dic
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_enemy(enemy_name):
    current_dir = os.getcwd()
    file_path = current_dir + '/enemies/' + enemy_name
    input_file_object = open(file_path, 'rb')
    
    try:
        enemy_dic = pickle.load(input_file_object)
        
    except IOError:
        print("did not work")
        return
    else:
        return enemy_dic
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




##################################################################
##################################################################
#!!!!!!!!!!!!!!!!!!!!!BATTLE SIM TIME!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##################################################################
##################################################################

'''
Second half of the program that will simulate the battle between the player
and the enemy of their choice above.

It will step through a basic loop of checking to see if eithier player or
enemy have passed or are at 0 HP and knock it out of the loop.  It will check this
at the start of each characters turn and knock it out of the loop it sense the 
chage when HP drops below that.

Within this loop it also checks to make sure that eithier character has choosen
to defend in their turn and reset there AC (Minus the AC Bonus to Defence) 

Player will always go first no matter what (MAY ADD SPEED STAT)
'''

def battle_sim (player_dic, enemy_dic):
    input(enemy_dic['intro_text'])
    input("Ready?")
    input('Fight!!')

#Bool_Flag that will end the loop if flipped to true
    fight_over = False
#    player_hp_max = player_dic['hp_max']

#A bool variable that tells us if the player has 'Defended' recently
    player_defending = False
    
    #Variable that holds a record of the enemies MAX HP for choosing how the Enemy Responds
    enemy_hp_max = enemy_dic['max_hp']
    #A bool variable that tells us if the enemy has 'Defended' recently    
    enemy_defending = False
    
    #Appends the player attack text with the enemy name, to make it more immersive
    new_player_attack_text = player_dic['attack_text'] + enemy_dic['enemy_name']

    #Then stores it into the player's dictionary to be used in the attack_func    
    player_dic['attack_text'] = new_player_attack_text
    
    turn_num = 1
    
    #MAIN BIG LOOP - Will end once eithier char runs out HP
    while fight_over == False:
        
#TEST!!
#        print('Player AC: ', player_dic['AC'], 'Player HP: ', player_dic['hp_max'])
#        print('Enemy AC: ', enemy_dic['enemy_ac'], 'Enemy HP: ', enemy_dic['max_hp'])        
        print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_TURN: ', turn_num)

#////////////////////////////PLAYER'S TURN/////////////////////////////////        
        
        #Checks to see if the player has defended recnetly and will reset their AC        
        if player_defending == True:
            player_dic['AC'] = player_dic['AC'] - DEFEND_BONUS_AC
            player_defending = False
            print("PLayer's AC: ", player_dic['AC'])
        

        if enemy_dic['max_hp'] <= 0 or player_dic['hp_max'] <= 0:
            fight_over = True        
        
        #Will change HP of Enemy if hits, only returns true for defending if Player chose it
        #if the player chooses DEFEND it will change AC for a single turn. 
    

        else:  
            player_defending = players_turn(player_dic, enemy_dic) 

#////////////////////////////ENEMY'S TURN////////////////////////////////////

        if enemy_defending == True:
            enemy_dic['enemy_ac'] = enemy_dic['enemy_ac'] - DEFEND_BONUS_AC
            print("Enemy AC: ", enemy_dic['enemy_ac'])
            enemy_defending = False            



        if enemy_dic['max_hp'] <= 0 or player_dic['hp_max'] <= 0:
            fight_over = True
            
            #Will change HP of Player if hits, only returns true for defending if Enemy chose it
            #if the Enemy chooses DEFEND it will change AC for a single turn. 

        else:
            
            enemy_defending = enemy_turn(player_dic, enemy_dic, enemy_hp_max)
        turn_num += 1
            
#////////////////////////WHEN THE BATTLE IS OVER!!////////////////////////////
    print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    input("The Battle is over! Whose the victory?")
    if enemy_dic['max_hp'] <= 0:
        victory_text = 'Congratulations ' + player_dic['name'] + ' you have proven your mettle and are victorious!'
        input(victory_text)
        
    else:
        print("You have perished but fought valiantly!")
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        

'''
Attack Function that is used by both the player and enemy.
Will roll a d20 + the attackers modifer and see if it is greater than the 
defenders AC

If it is it will calculate Damage and return that damage! If it does not hit
it returns a 0 and nothing will get subtracted from defenders HP

If the d20 roll is a 20 (Nat 20) a critical hit will occur and will double damage!
'''

def attack_func(defender_ac, defender_hp, attacker_dmg_die, attacker_key_mod, attacker_weapon, attack_text):
    roll_to_hit  = dice_rolls.roll_d20()
    print('roll to hit: ', roll_to_hit + attacker_key_mod)
    multiply_attack = 1
    
    if roll_to_hit == 20:
        input("CRITICAL HIT!")
        multiply_attack = 2
            
    if roll_to_hit == 20 or roll_to_hit + attacker_key_mod > defender_ac:
        input(attack_text)        

#Determines from the dmg_die how many dies to roll, and what type of die to roll
        roll_die_list = determine_dmg_rolls(attacker_dmg_die)

         
#Using the list created just before, it looks at the first element, which is the
#number of times to roll, and then use the second element, which is the type of
#die to use!        

        num_of_times_to_roll = int(roll_die_list[0])
        count = 1
        total_damage = 0
        while count <= num_of_times_to_roll:
            total_damage += roll_die_for_damage(roll_die_list[1])
            count += 1
       
        #Multiply damage, will be 1x unless its a CRIT!
        total_damage = multiply_attack * total_damage
        
        print('For ', total_damage, ' damage!')
            
#If the roll to hit doesnt pass the defenders AC
    elif roll_to_hit == 1 or roll_to_hit + attacker_key_mod <= defender_ac:
        if roll_to_hit == 1:
            print ("CRITICAL MISS...")
        else:
            input('*woosh* the attack goes wide, and misses!')
        total_damage = 0        
    return total_damage
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
        
#Will take in the second element of the roll_die_list and then 
#roll the corresponding dice that matches that value and then 
#return the result of that roll    

def roll_die_for_damage(type_of_die):
    type_of_die = int(type_of_die)
    if int(type_of_die) == 100 :
        roll_result = dice_rolls.roll_d100()
        
    elif int(type_of_die) == 20 :
        roll_result = dice_rolls.roll_d20()        
        
    elif int(type_of_die) == 12 :
        roll_result = dice_rolls.roll_d12() 

    elif int(type_of_die) == 10 :
        roll_result = dice_rolls.roll_d10() 

    elif int(type_of_die) == 8 :
        roll_result = dice_rolls.roll_d8() 

    elif int(type_of_die) == 6 :
        roll_result = dice_rolls.roll_d6() 

    elif int(type_of_die) == 4 :
        roll_result = dice_rolls.roll_d4()         
        
    return roll_result
        
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    

#Function that will boost the characters AC and return the new boosted AC

def defend_func(defender_ac):
    defender_ac += DEFEND_BONUS_AC
    return defender_ac

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
       
#Will take the charaters dmg die and split it into two elements
#First being the num times to roll, and the second being type of die
#And returns the list!    

def determine_dmg_rolls (attackers_die):
    die_roll_list = []
    die_roll_list = attackers_die.split('d')
    return die_roll_list
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
Function that will contain all of the actions that the player can take
and all the functions tied with it as well.

It will include nice dialog with the player to help them through the proccess

The end result will eithier be a change to the enemies HP with a successful attack

Or

Bolstering your defence for a single turn.

All includes input validation from the user!
'''

def players_turn(player_dic, enemy_dic):
    
    input("~~~~~PLAYER'S TURN~~~~~~~~\n")
    
    print("Current HP: ", player_dic['hp_max'])
    print("(A) ATTACK    or   (B) DEFEND")
    player_choice = input("Your choice: ")
    char_defending = False
    
    valid_answer = False
    while valid_answer != True:
        if player_choice.upper() == 'A' or player_choice.upper() == 'B':
            valid_answer = True

        else:
            input('~Invalid Choice~')
            print("(A) ATTACK    or   (B) DEFEND")
            player_choice = input("Your choice: ")            
            
            
    if player_choice.upper() == 'A':
        total_damage = attack_func(enemy_dic['enemy_ac'], enemy_dic['max_hp'], player_dic['weapon_dmg_die'], player_dic['key_mod'], player_dic['weapon'], player_dic['attack_text'])
        enemy_dic['max_hp'] = enemy_dic['max_hp'] - total_damage
        
    elif player_choice.upper() == 'B':
        player_dic['AC'] = defend_func(player_dic['AC'])
        char_defending = True
        defend_string = player_dic['name'] + " turtles up, raising their defense!"
        print("Defending AC thats BOOSTED: ", player_dic['AC'])
        input(defend_string)
                

            
    return char_defending
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   

'''
Similiar to what the players turn function is like but operates through if and elif 
statements!  Contains the same options as player where they can defend or Attack
but chooses based on two factors. 
1.) Current Hp compared to MAX HP amd where it stands
2.) And a random number determines Enemy's final decision                
'''

def enemy_turn(player_dic, enemy_dic, enemy_max_hp):

    input('~~~~~ENEMIES TURN~~~~~~\n')
        
    enemy_choosing_num = 0
    char_defending = False
    #If Enemy's HP is higher than 50%

#If Enemy HP is 50% or better than this set of code will occur!

    if enemy_dic['max_hp'] >= round(enemy_dic['max_hp'] * 0.50): #https://www.programiz.com/python-programming/methods/built-in/round 
        enemy_choosing_num = random.randint(1, 4)
        if enemy_choosing_num == 4:
            enemy_dic['enemy_ac'] = defend_func(enemy_dic['enemy_ac'])
            char_defending = True
            defending_text = enemy_dic['enemy_name'] + " turtles up, and raises it's defense!"
            print("Defending AC thats BOOSTED: ", enemy_dic['enemy_ac'])            
            input(defending_text)
        else:
            total_damage = attack_func(player_dic['AC'], player_dic['hp_max'], enemy_dic['enemy_dmg_die'], enemy_dic['enemy_key_mod'], enemy_dic['enemy_weapon'], enemy_dic['enemy_attack_description'])
            player_dic['hp_max'] = player_dic['hp_max'] - total_damage
            
#If Enemy's HP is below than 50%
    elif enemy_dic['max_hp'] <= round(enemy_dic['max_hp'] * 0.50): #https://www.programiz.com/python-programming/methods/built-in/round 
        enemy_choosing_num = random.randint(1, 2)
        if enemy_choosing_num == 2:
            enemy_dic['enemy_ac'] = defend_func(enemy_dic['enemy_ac'])
            char_defending = True
            defending_text = enemy_dic['enemy_name'] + " turtles up, and raises it's defense!"
            print("Defending AC thats BOOSTED: ", player_dic['AC'])            
            input(defending_text)            
        else:
            total_damage = attack_func(player_dic['AC'], player_dic['hp_max'], enemy_dic['enemy_dmg_die'], enemy_dic['enemy_key_mod'], enemy_dic['enemy_weapon'], enemy_dic['enemy_attack_description'])
            player_dic['hp_max'] = player_dic['hp_max'] - total_damage                
            
    
            
    return char_defending
        
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        

        
def main():
    player_dic = character_selection()
#    print(player_dic)
    enemy_dic = picking_enemy()
#    print(enemy_dic)
    battle_sim(player_dic, enemy_dic)
    
main()