# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:41:44 2020

@author: 16025
"""
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    h1 = hand_values(hand_1)
    h2 = hand_values(hand_2)
    
    if h1 > 21:
        return False
    elif h2 > 21:
        return True
    else:
        return h1 > h2

def hand_values(hand):
    possible = [0]
    for val in hand:
        if val == 'J' or val == 'Q' or val == 'K':
            possible = [x + 10 for x in possible]
        elif val == 'A':
            possible = balloon_aces(possible)
        else:
            possible = [x + int(val) for x in possible]
    return closest_21(possible)

def closest_21(cards):
    closest = 0
    for value in cards:
        if value > closest and value <= 21:
            closest = value
    return closest

def balloon_aces(cards):
    newlist = []
    for item in cards:
        newlist.append(item + 1)
        newlist.append(item + 11)
    return newlist

t1 = ['3', '4', 'K', 'A', 'A']
# print([n + 10 for n in t1])
# t1.append(3)
# print(t1)
print(hand_values(t1))