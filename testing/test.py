# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:46:43 2019

@author: cammr
"""
import string
import pickle
import random

import os #https://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python SOURCE


word = 'Hello'

print('What is up' + word + 'Whats is up')



'''
def minus_hp (player_dic, enemy_dic):
    enemy_dic['hp'] = enemy_dic['hp'] - 5
    player_dic['hp'] = player_dic['hp'] -10
    
    defending = True
    
    return defending
    
#    print('Player', player_dic)
#    print('Enemy', enemy_dic)
    
    
    return

enemy_dic = {'hp':40, 'ac':13}
player_dic = {'hp':50, 'ac':15}
defending = False


print('Before\n')
print('Player', player_dic)
print('Enemy', enemy_dic)
print(defending)

defending = minus_hp(player_dic, enemy_dic)

print('After\n')
print('Player', player_dic)
print('Enemy', enemy_dic)
print(defending)
'''


'''
def determine_dmg_rolls (attackers_die, attack_txt):
    if attack_txt == '':
        attack_txt = 'nothing'
    die_roll_list = []
    die_roll_list = attackers_die.split('d')
    print(attack_txt)
    return die_roll_list


player_dic = {'max_hp':30, 'weapon':'Scimitar', 'dmg_die':'2d8'}

roll_list = determine_dmg_rolls(player_dic['dmg_die'])
val1 = roll_list[0]
val2 = roll_list[1]
val3 = (val1) + (val2)
print(roll_list)
print(val1 + ' ' + val2)
print(val3)
'''


'''
rand_num = random.randint(0, 2)
print(rand_num)
'''



'''
val = -1
print(val)

val += 1

print(val)
'''

'''
val1 = 30

val2 = 60

print(val1, "\t", end = '')
print(val2)
'''



'''
set1 = set([10, 20, 30, 40])
set2 = set([40, 50, 60])

set3 = set1.union(set2)

print(set3)
'''

'''
dic1 = {"Name":"Faria", "Class":"Rogue"}

dic2 = {"HP":20, "Weapon":"Scimitar", "Damage Die":"1d8"}

print(dic1)
print(dic2)

dic3 = {**dic1, **dic2}

print(dic3)
'''

""" SOURCE to allow merge of two dictionaries: 
    ://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
"""
'''    
class_choice = 'AA'

if class_choice.upper() < 'A' or class_choice.upper() > 'D':
    print("Is not A - B choice")
    
else:
    print("It is A - B choice!")
'''


'''
player_dic = {"Name":"Faria", "HP":10, "AC":15, "Weapon":"Scimitar", "damage_die":"1d8"}
print(player_dic)
test_file_name = 'char_files'
test_file_object = open(test_file_name, 'wb')
pickle.dump(player_dic, test_file_object)

player_dic2 = {"Name":"Vulwin", "HP":15, "AC":17, "Weapon":"Shortsword", "damage_die":"1d10"}
pickle.dump(player_dic2, test_file_object)
test_file_object.close()

test_file_object2 = open(test_file_name, 'rb')
faria_dic = pickle.load(test_file_object2)
print(faria_dic)

vulwin_dic = pickle.load(test_file_object2)
print(vulwin_dic)
'''


'''
VOWELS = ['a', 'e', 'i', 'o', 'u']

word = '"Why'
print(word)
end_punc = word[-1]
print(end_punc)

word = word.replace('"', '')
print(word)

word = word + end_punc

print(word)




print('Adding a Blank Char\n')

blank_char = ''
print(blank_char, 'k')

word = word + blank_char

print(word)
'''