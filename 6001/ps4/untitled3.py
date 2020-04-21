# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:17:18 2020

@author: admin
"""




def is_list_permutation(L1, L2):
    def create_dict(list1):
        dict1 = {}
        for i in list1:
            try:
                dict1[i] = dict1[i]+1
            except:
                dict1[i] = 1
            
        return dict1
  
            
    
    dc1 = create_dict(L1)
    dc2 = create_dict(L2)
    
    if dc1.items() == dc2.items() :
        keymax = max(dc2, key = dc2.get)
        return (keymax, dc2[keymax], type(keymax))
    else:
        return False


L1 = ['a', 'd','c','a']
L2 = ['a', 'd','a', 'c']

print(is_list_permutation(L1, L2))
            
            
            