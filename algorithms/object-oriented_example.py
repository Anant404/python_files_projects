# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 01:23:24 2020

@author: admin
"""
import datetime

class Person(object):
    
    def __init__(self, name):
        self.name = name
        self.birthday = None 
        self.lastName = name.split(' ')[-1]
        
        
    def setBirthday(self,month,day,year) :
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        
        if self.birthday == None:
            raise ValueError
        
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name 
        return self.lastName < other.lastName 
    
    def __str__(self):
        return self.name
    
    def getLastName(self):
        return self.lastName
        
    
    
    
p1 = Person('adam smith')
print(p1)
p1.setBirthday(5,4,55)
c = p1.getAge()
print(c)    



class MITPerson(Person):
    nextIDNum = 0
    
            
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIDNum
        MITPerson.nextIDNum += 1
        
    def getIdNumber(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance )
    
    
        
        
m3 = MITPerson('Mark zuckerberg')
m3.setBirthday(10,4,89)
print(m3.lastName)

print(m3.getAge())


class UG(MITPerson):
    def __init__(self, name, year):
        MITPerson.__init__(self, name)
        self.year = year 
        
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude" + utterance)
    

    def speak(self, utterance):
        return MITPerson.speak(self, "dude" + utterance)
    
class Grad(MITPerson):
    pass



def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad) 


s1 = UG( "Matt Damon", 2017)
s2 = UG("Kevin Butler", 2018)


print(s1.speak('what are you'))
print(m3.speak('what are you'))



       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    