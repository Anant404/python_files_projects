# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:39:24 2020

@author: admin
"""

class plane:
    def __init__(self, obj):
       
        self.obj = obj
    def start(self):
        self.obj.starts()
    
class rolls:
    
    def starts(self):
        print("rolls engine is starting")
        
class pratt:
    
    def starts(self):
        print("pratt engine is starting")
        
x = rolls()
y = pratt()

a77 = plane(y) ## plane(x) will give a different result depending on the type of
                ## object similar to + operator for strings and numbers and lists 
                ## its different
            
a77.start()

    