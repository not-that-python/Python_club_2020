# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:55:34 2020

@author: Avni
"""


for i in range(1, 101):
    if i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print('buzz')
    elif i%3 == 0 and i%5 == 0:
        print('fizzbuzz')
    else:
        print(i)
print('hello')