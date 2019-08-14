#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:04:45 2019

@author: xam
"""

import Squarepos
from skimage.feature import blob_log 
from skimage.color import rgb2gray
from skimage import io

from skimage.transform import resize
def getOrdBlob(a):
    img1 = io.imread(a)
    image1 = resize(img1,(3480,2320 ))
    e = Squarepos.getEnd()
    
    X = []
    Y = []
    xe = []
    ye =[]
    ep = []
    posList = []
    ordBlob = []
    image_gray = rgb2gray((image1))
    
    blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)
    
    for blob in blobs_log:
            x,y,r = blob
            print(x)
            print(y)
            X.append(x)
            Y.append(y)
            
    for x in X:
        for pos in range(0,len(e)):
            a = e[pos]
            b = a[0]
            if x < b:
                xe.append(b)
                break
                
    for y in Y:
        for pos in range(0,len(e)):
            a = e[pos]
            b = a[1]
            if y < b:
                ye.append(b)  
                break
        
    for pos in range(0,len(xe)):
         ep = ep + [(xe[pos],ye[pos])]     
    
    
    for end in e:
        temp = []
        i = 0     
        for endpiont in ep:
            if endpiont == end:
                temp = temp + [i]
            i+=1  
        posList = posList + [temp]   
        
        
    for pos in posList:
        temp = []
        for loc in pos:
            temp = temp + [blobs_log[loc]]
        ordBlob= ordBlob + [temp]    
    

    return ordBlob        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #img1 = io.imread('1.png')
#image1 = resize(img1,(3480,2320 ))
#e = Squarepos.getEnd()
#
#X = []
#Y = []
#xe = []
#ye =[]
#ep = []
#posList = []
#ordBlob = []
#image_gray = rgb2gray((image1))
#
#blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)
#
#for blob in blobs_log:
#        x,y,r = blob
#        print(x)
#        print(y)
#        X.append(x)
#        Y.append(y)
#        
#for x in X:
#    for pos in range(0,len(e)):
#        a = e[pos]
#        b = a[0]
#        if x < b:
#            xe.append(b)
#            break
#            
#for y in Y:
#    for pos in range(0,len(e)):
#        a = e[pos]
#        b = a[1]
#        if y < b:
#            ye.append(b)  
#            break
#    
#for pos in range(0,len(xe)):
#     ep = ep + [(xe[pos],ye[pos])]     
#
#
#for end in e:
#    temp = []
#    i = 0     
#    for endpiont in ep:
#        if endpiont == end:
#            temp = temp + [i]
#        i+=1  
#    posList = posList + [temp]   
#    
#    
#for pos in posList:
#    temp = []
#    for loc in pos:
#        temp = temp + [blobs_log[loc]]
#    ordBlob= ordBlob + [temp]    
#        
    
     
        
        
        
        
        
        
        
        
