#! /usr/bin/env python3

import requests
import os


for root, dirs, files in os.walk("/data/feedback"):
    path = root.split(os.sep)
    for file in files:
        temp='/data/feedback/'+file
        f=open(temp,'r')
        a=f.readlines()
        f.close()
        d={}
        d['title']=a[0].strip()
        d['name']=a[1].strip()
        d['date']=a[2].strip()
        t=''
        for i in range(3,len(a)):
            t+=a[i].strip()
        d['feedback']=t
        response=requests.post('http://34.67.202.174/feedback/',data=d)
        print(response)
