# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:43:47 2023

@author: Arpit Akar
"""

import urllib.request,urllib.parse, urllib.error
import json
## note:Google is increasingly requiring keys
#for this api
serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=input('Enter  Location: ')
    if len(address)<1: break
    url = serviceurl+urllib.parse.urlencode(
        {'address:':address})
    
    print('Retriving',url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retrived',len(data),'characters')
    
    try:
        js=json.loads(data)
    except json.JSONDecodeError:
        print('Error parsing JSON data')
        
    if not js or 'status' not in js or js['status']!='OK':
        print('=== Failure to retrieve===')
        print(data)
        continue
    
    print(json.dumps(js,ident=4))
    
    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)
    location=js['results'][0]['formatted address']
    print(location)