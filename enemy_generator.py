# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:08:42 2019

@author: cammr
"""

import pickle
import string
import dice_rolls
import os #https://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python SOURCE

#Creat Enemies for DnD Sim!

#NEED TO CAST ALL NUMBERS ON ENEMIES TO BE INTS! CAUSES AN ERROR!!!

def creating_enemy_dic ():
    enemy_dic = {}
    intro_text = input("Introduction Text: ")
    confirm_description = False
    while confirm_description != True:
        answer= input("Y/N?: ")
        if answer == 'N':
            intro_text = input("Introduction Test: ")
        else:
            confirm_description = True
            
    enemy_name = input("Enemy Name: ")
    max_hp = int(input("Max Hp: "))
    AC = int(input("AC: "))
    weapon = input("Weapon: ")
    dmg_die = input("Dmg_Die: ")
    key_mod = int(input("Key_Mod: "))
    attack_description = input("Attack Description: ")
    confirm_description = False
    while confirm_description != True:
        answer = input("Y/N?: ")
        if answer == 'N':
            attack_description = input("Attack Description: ")
        else:             
            confirm_description = True
            
    half_health_condition = input("50% Condition Description: ")
    confirm_description = False
    while confirm_description != True:
        answer = input("Y/N?: ")
        if answer == 'N':
            half_health_condition = input("50% Condition Description: ")
        else:
            confirm_description = True
            
    quarter_health_description = input("25% Condition Descripton: ")
    confirm_description = False
    while confirm_description != True:
        answer = input("Y/N?: ")
        if answer == 'N':
            quarter_health_description = input("25% Condition Description: ")
        else:
            confirm_description = True
            
    enemy_dic["intro_text"] = intro_text
    enemy_dic['enemy_name'] = enemy_name
    enemy_dic["max_hp"] = max_hp
    enemy_dic['enemy_ac'] = AC
    enemy_dic['enemy_weapon'] = weapon
    enemy_dic['enemy_dmg_die'] = dmg_die
    enemy_dic['enemy_key_mod'] = key_mod
    enemy_dic['enemy_attack_description'] = attack_description
    enemy_dic['half_health_description'] = half_health_condition
    enemy_dic['quarter_health_description'] = quarter_health_description
    
    return enemy_dic
        

def save_enemy_file (enemy_dic):
    
    current_dir = os.getcwd()
    file_name = current_dir + '/enemies/' + enemy_dic['enemy_name']
    output_file_object = open(file_name, 'wb')
    pickle.dump(enemy_dic, output_file_object)
    output_file_object.close()
    return



def main():
    enemy_dictionary = creating_enemy_dic()
    print(enemy_dictionary)
    save_enemy_file(enemy_dictionary)
    

main()
