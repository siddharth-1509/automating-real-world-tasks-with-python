
#! /usr/bin/env python3

import os
import requests

for root, dirs, files in os.walk("supplier-data/descriptions/"):
    path = root.split(os.sep)
    for file in files:
        temp='supplier-data/descriptions/'+file
        print(file)
        f=open(temp,'r')
        a=f.readlines()
        f.close()
        d={}
        d['name']=a[0].strip()
        d['weight']=a[1].strip().split(' ')[0]
        d['image_name']=file.split('.')[0]+'.jpeg'
        t=''
        for i in range(2,len(a)):
            t+=a[i].strip()
        d['description']=t
        print(d)
        response=requests.post('http://35.202.65.117/fruits/',data=d)
        print(response)
