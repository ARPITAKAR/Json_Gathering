# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:29:25 2023

@author: Arpit Akar
"""

import json
data='''{
"name":"chuck",
"phone":{
    "type":"intl",
    "number":"+17343034456"},
"email":{
    "hide":"yes"}}'''
info=json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])