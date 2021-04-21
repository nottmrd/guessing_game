# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:43:32 2020

@author: peter
"""

import random

x = random.randint(1, 100)
y = int(input("Try to guess the number between 1 and 100. Enter your guess: "))
tries = 1
while y != x:
    tries += 1
    print("Wrong!")
    if y < x:
        print("Guess higher")
    if y > x:
        print("Guess lower")
    y = int(input("Guess again: "))
    if y == x:
        print("Well done you got it!")
        print("It took you", str(tries), "attempts.")
        break