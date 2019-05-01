# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:22:50 2019

@author: cread09
"""


def main():

    player_dic = {'name':'Steve',
                  'class':'Barbarian'}
    
    print(player_dic)
    
    player_dic = barb_create(player_dic)
    
    print(player_dic)

def barb_create(player_dic):
    player_dic['hp'] = 36
    player_dic['weapon'] = 'Scimitar'
    
    return player_dic

main()