from tkinter import *
from tkinter import ttk
from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk
import tkinter as  tk
import math


def getThreads(CIRCULAR_REPETITION,FRAMENAILCOUNT , FRAME_RADIUS,TOTALLINESLIST ,FINAL_IMAGE ,OX,OY ,DARKTHRESHOLD):
    Cr=CIRCULAR_REPETITION
    Tl =TOTALLINESLIST
    Threads =[]
    for i in range(FRAMENAILCOUNT):
      for k in range(Cr):  
        highestDarkDensity = [0,0,0]
        
        for j in range(FRAMENAILCOUNT-(1+k)):
            
            lineTuples = Tl[i][j]
            print(lineTuples)
            DarknessSum = 0
            DarkDensity = 0 
            tuplepointCount=0
            for tuplepoint in lineTuples:
                # print(tuplepoint)
                tuplepointCount+=1
                pixelAccess= FINAL_IMAGE.load()
                
                #____NOTE________for calculating pixelValue___
                '''
                pixelData[x,y], accepts location x, y relative to top-corner of the image (taken as 0,0 for points(pixels) relative to the image )
                therefore we must calculate , for tuple point , its relative position from top-corner of the image
                .Simple geometry can be used to see that y = abs(tuplepoint[1]-(Oy +frameradius))
                and that x = abs(tuplepoint[0]-(Oy -frameradius))

                 
                '''

                x_relative =abs(tuplepoint[0]-(OX + FRAME_RADIUS) )
                y_relative =abs(tuplepoint[1]-(OY- FRAME_RADIUS) ) 
                # print(tuplepoint[0],tuplepoint[1])
                # print(x_relative,y_relative)
                # print("comp " + str(OX -FRAME_RADIUS) + str(OX+FRAME_RADIUS))
                # print("comp2" + str(tuplepoint[0]-OX +FRAME_RADIUS) + str(tuplepoint[0] -OX -FRAME_RADIUS))

                # print(int(x_relative) ,int(y_relative))
                if int(x_relative)<400 and int(y_relative)<400:
                  pixelValue = pixelAccess[int(x_relative),int( y_relative)]

                #_________________________________be very careful
                Error = pixelValue
                Darkness = (255 - pixelValue)
                DarknessSum += Darkness
            if tuplepointCount > 0 : 
              DarkDensity = (DarknessSum)/(tuplepointCount)
            if highestDarkDensity[0]< DarkDensity and DarkDensity > DARKTHRESHOLD:
                highestDarkDensity[0]= DarkDensity
                highestDarkDensity[1]= i
                highestDarkDensity[2]= j
                # print(DarkDensity)    


                lineLoc = Tl[highestDarkDensity[1]][highestDarkDensity[2]]
                lineTuple = (lineLoc[0][0],lineLoc[0][1] ,lineLoc[-1][0] ,lineLoc[-1][1] )
               
                Threads.append(lineTuple)
                print("appended tuple " , lineTuple)
       
        print(highestDarkDensity)
        
        Tl[highestDarkDensity[1]][highestDarkDensity[2]].pop()
    return Threads

