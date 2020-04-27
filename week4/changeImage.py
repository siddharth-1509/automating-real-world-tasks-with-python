#!/usr/bin/env python3

from PIL import Image
import os

path=os.walk('supplier-data/images')

for root, dirs, files in path:
    for file in files:
        if '.tiff' in file:
            image=Image.open("supplier-data/images/"+file)
            image=image.convert('RGB')
            image=image.resize((600,400))
            temp=file.split('.')
            image.save('supplier-data/images/'+temp[0]+'.jpeg')
