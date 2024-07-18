from tkinter import *
from tkinter import ttk
from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk
import tkinter as  tk
import math



thread_width = 3
thread_color = "blue"

def drawLine(CANVAS,LINETUPLE):
    L= LINETUPLE 
    CANVAS.create_line(L[0],L[1],L[2],L[3],fill=thread_color, width=thread_width)
def drawThreads( FRAMENAILPOINTS ,OX,OY , REDUCED_RESO_PIXEL_GAP):
    totalLines = []
    for i in range(len(FRAMENAILPOINTS)):
     
      #  print(i)
       lines=[]
       z = FRAMENAILPOINTS
       for j in range(len(FRAMENAILPOINTS)):
        
        s = z[i] #start point of the thread
        if j != i :
        #    print(j)
           e = z[j] # endpoint of the thread
           def lineEq(xcoordinate):
              a =s.real
              b = s.imag
              c= e.real
              d = e.imag
              x = xcoordinate
              value = (x-a)*((b-d)/(a-c)) +b
              return value
           
           gap = REDUCED_RESO_PIXEL_GAP
           iteration_num = int(abs((s.real - e.real)/gap))
           pointsOntheline = []
           
           for k in range(iteration_num):
              
            #   print(k)
              if s.real>e.real:
                 x_coo = s.real -(k*int(gap))
                 y_coo  = lineEq(x_coo)
                 pointsOntheline.append(( int(x_coo) , int(y_coo) ))
              else :
                 x_coo = s.real +(k*int(gap))
                 y_coo  = lineEq(x_coo)

                 pointsOntheline.append(( int(x_coo) , int(y_coo) ))
           
           lines.append(pointsOntheline)

       totalLines.append(lines)
    print("length of totalLines list" + str(len(totalLines))) 
    print("length of lines through every point on the frame to other points on the frame "+ str(len(totalLines[0])))   




    #____Doing filteration of best line out of Lines[n], on the basis of darkness of the pixels lying on frame___
   
    for lines in range(len(FRAMENAILPOINTS)):
       for line in range(len(FRAMENAILPOINTS)-1):
           for dot in totalLines[lines][line]:
              pass


    return totalLines              