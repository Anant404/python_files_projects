# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:34:42 2020

@author: admin
"""
# find the cube root of a number by using bisection search 

## bisection search algorithm example 
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


## convert a decimal to binary for fractions find a p such that 2^p*x is a 
## whole number that is ( 2^p*x )%1 = 0 , then use the below algorithm to 
## calculate to binary and then shift the resultant number by p points.
## if you get 1011 and p = 3 then answer is 1.011
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



# recursion breakdown the problem into a smaller version of itself, 
# find a base case and define that 
    
#multiplying two numbers 
    
def mult(a, b):
    if b == 1:
        return a
    
    else:
        return a + mult(a, b-1)
    
print(mult(3,2))


def fact(n):
    if n== 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(4))



def recur(base , exp):
    ans = 1
    for i in range(exp):
        ans = ans*base
        
    return ans

print(recur(2, 3))

def recuriter(base, exp):
    if exp == 1:
        return base
    else:
        return base*recuriter(base, exp-1)
    
    
#print(recuriter(2,3))

def gcd(a, b):
    
    if a <= b:
        a1 = a
        b1= b
    else:
        a1 = b
        b1 = a
        
    if b1%a1 == 0 :
        return a1
    
    else:
        return gcd( a1-1, b1)
    

print(gcd(17,12))


#-----------


##generating fibonacci series the n == 0 can be 0 or 1 depending on community of interest in the context of rabbits
## it is 1
    
def  fib(n):
    
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)
    
    
print(fib(6))
    
    
        
    
# to revise towers of hanoi

# recursive is an example of divide and conquer algorithm   

# is the word a palindrome recursion

def isrecur(s):
    if s == '':
        return True
    
    else :
        print(s)
        return (s[0] == s[-1]) and (isrecur(s[1: -1]))
    
print(isrecur('abcba'))



# returning all possible combinations of a string: variation given below sorts all the unique element

def combi(s):
    list1 = []
    temp = ''
    for i in range(len(s)):
        for j in range(len(s)-i):
            temp = temp + s[i + j]
            list1.append(temp)
        temp = ''   
    
    list1 = list(set(list1))
    list1.sort(key = len)
    
    return list1

#print(combi('abbadabbc'))
        
    
        

## finding the cube root with bisection search 

def bisec(x, error):
    start = 0 
    end = x
    guess = (start + end)/2
    
    while abs(guess**3 - x) >= error:
        if guess**3  >  x  :  
            end = guess
            
        else:
            start = guess
            
        guess = (start+ end)/2
        
    return guess 




    


        
            
            