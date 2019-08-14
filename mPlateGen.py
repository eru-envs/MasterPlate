#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:57:07 2019

@author: xam
"""
from PIL import Image
import numpy as np
import statistics
import getBlobLoc
import itertools
import math
import Kclus
import Squarepos
b1 = getBlobLoc.getOrdBlob('1.png')
b2 = getBlobLoc.getOrdBlob('2.png')
b3 = getBlobLoc.getOrdBlob('3.png')

pix1 = Squarepos.getPixels('1.png')
cord1 = Squarepos.coList()
pix2 = Squarepos.getPixels('2.png')
cord2 = Squarepos.coList()
pix3 = Squarepos.getPixels('3.png')
cord3 = Squarepos.coList()

a1 = []
a2 = [] 
a3 = []

blobs1r = []
blobs2r = []
blobs3r = []
blobs1ar = []
blobs2ar = []
blobs3ar = []

weirdBlobs = []

testVal = []

finPixList =[]
for blobs in b1:
    tempr = []
    tempar = []
    for blob in blobs:
        x,y,r = blob
        tempr = tempr + [r]
        tempar = tempar+ [(math.pi)*(r*r)]
    blobs1ar = blobs1ar + [tempar]
    blobs1r = blobs1r + [tempr]
    
for blobs in b2:
    tempr = []
    tempar = []
    for blob in blobs:
        x,y,r = blob
        tempr = tempr + [r]
        tempar = tempar+ [(math.pi)*(r*r)]
    blobs2r = blobs2r + [tempr]
    blobs2ar = blobs2ar + [tempar]
      
for blobs in b3:
    tempr = []
    for blob in blobs:
        x,y,r = blob
        tempr = tempr + [r]
        tempar = tempar+ [(math.pi)*(r*r)]
    blobs3ar = blobs3ar + [tempar]
    blobs3r = blobs3r + [tempr]
    
    
#for cord in cord1:
#    xys = cord[0]
#    xs = xys[0]
#    ys = xys[1]
#    xye = cord[1]
#    xe = xye[0]
#    ye = xye[1]
    
for pix in pix1:
    array = np.array(pix, dtype=np.uint8)
    image = Image.fromarray(array)
    area = Kclus.getArea(image)
    a1 = a1 + [area]
         
    
for pix in pix2:
    array = np.array(pix, dtype=np.uint8)
    image = Image.fromarray(array)
    area = Kclus.getArea(image)
    a2 = a2 + [area]
              
    
for pix in pix3:
    array = np.array(pix, dtype=np.uint8)
    image = Image.fromarray(array)
    area = Kclus.getArea(image)
    a3 = a3 + [area]
    
for rads in blobs1r:
    count = 0
    x = statistics.mean(rads)
    sd = statistics.stdev(rads)
    for r in rads:
        if r > (x+sd) or r <(x-sd):
            count+=1
    weirdBlobs= weirdBlobs +[count]    


for pos in range(0,96):
    it = itertools.repeat(0,3)
    testVal.append(it)

    
for pos in range(0,96):
    if testVal[pos]==1:
        finPixList = finPixList+ [pix1[pos]] 
    if testVal[pos]==2:
        finPixList = finPixList+ [pix2[pos]] 
    if testVal[pos]==3:
        finPixList = finPixList+ [pix3[pos]]   
        
array = np.array(finPixList, dtype=np.uint8)
image = Image.fromarray(array)   
image.save('master.png')
    
        
    
    
        
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    