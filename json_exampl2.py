# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:34:11 2023

@author: Arpit Akar
"""

import json
input='''[{
"id":"001",
"x":"04",
"name":"Arpit"
},
{"id":"009",
 "x":"7",
 "name":"Akar"}]
'''
info=json.loads(input)
#info is a list
print('User count:',len(info))
for item in info:
    print('Name',item['name'])
    print('Id',item['id'])
    print('Attribiute',item['x'])