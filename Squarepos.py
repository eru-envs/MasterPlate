#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:16:50 2019

@author: xam
"""
import cv2 
height = 2320
width = 3480
widthIterator = 12
heightIterator = 8
Hstep= int(height/heightIterator)
Wstep = int(width/widthIterator) 
Slist = []
Elist = []
combList = []
sList = []
eList = []
coList = []
for y in range(0,(height-Hstep)+1,Hstep):
   for x in range(0,(width-Wstep)+1,Wstep):
      Slist = Slist + [(x,y)]
      
for y in range(Hstep,(height)+1,Hstep):
   for x in range(Wstep,(width)+1,Wstep):
      Elist = Elist + [(x,y)]

if(len(Slist) != len(Elist)):
    print("lists not equal")       

for pos in range(0,len(Slist)):
     combList = combList + [(Slist[pos],Elist[pos])]
    




for y in range(0,(400-50)+1,50):
   for x in range(0,(600-50)+1,50):
      sList = sList + [(x,y)]
      
for y in range(50,(400)+1,50):
   for x in range(50,(600)+1,50):
      eList = eList + [(x,y)]

if(len(sList) != len(eList)):
    print("lists not equal")       

for pos in range(0,len(sList)):
     coList = coList + [(sList[pos],eList[pos])]
    

def getPixels(a):
    l1 = []
    img = cv2.imread(a)
    image = cv2.resize(img,(400, 600))
    for pos in range(0,len(coList)):
        b = coList[pos]
        c = b[0]
        r = b[1]
        d = c[0]
        e = c[1]
        s = r[0]
        t = r[1]
        z = []
        for x in range(d,(s+1)):
            for y in range(e,(t+1)):
             pixel = image[x,y]
             z = z + [(pixel)]
        l1 = l1+ [(z)]
    return l1    



def getComb():
    return combList
def getEnd():
    return Elist
def getStart():
    return Slist()
def getCo():
    return coList
 