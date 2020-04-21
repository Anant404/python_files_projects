# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:34:42 2020

@author: admin
"""
# find the cube root of a number by using bisection search 


def cube(x, error):
    guess = x/2
    start = x
    end = 1
    
    while abs(guess**3 - x) >= error:
        if guess**3 < x:
            start = guess
            
            guess = (start + end )/2
            
        else:
            end = guess
            guess = (start + end)/2
            
    return guess


print(cube(.270, .0000001))

def binary(x):
    if x < 0:
        isneg = True
        x = abs(x)
        
    if x == 0:
        return 0
    
    result = ''
    num = x
    while num > 0:
        result = str(num%2) + result
        num = num//2
        
    return result

print(binary(4))
        
            
            