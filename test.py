# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 22:31:34 2017

@author: isaacb
"""

import string

shiftDict = {}
        
shift = 2


for letter in string.ascii_letters:
    if chr(ord(letter)+shift) in string.ascii_letters:
        shiftDict[letter] = chr(ord(letter)+shift)
    else:
        shiftDict[letter] = chr(ord(letter)-26+shift)
        
        
print(shiftDict)

print(ord('z'))