from tkinter import *
from tkinter import ttk
from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk
import tkinter as  tk
import math
# from imageshow import draw_point




def drawLine(CANVAS,LINETUPLE,THREAD_WIDTH,THREAD_COLOR):
    L= LINETUPLE 
    CANVAS.create_line(L[0],L[1],L[2],L[3],fill=THREAD_COLOR, width=THREAD_WIDTH)


def display_coordinates(canvas, x, y):
    """
    Displays coordinates on the canvas using a label.

    Args:
        canvas (tk.Canvas): The Tkinter canvas object.
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
    """

    # Create a label to display coordinates
    coord_label = tk.Label(canvas, text=f"({x}, {y})")

    # Position the label slightly above the point
    coord_label.place(x=x-0, y=y-0)  # Adjust offset as needed


def DrawMultipleThreads(CANVAS,THREADS ,THREAD_WIDTH,THREAD_COLOR):
   for thread in THREADS:
    x1,y1,x2,y2 = thread
    # print( "drawing thid thread", thread)
    if x1==800 :
     CANVAS.create_line(thread[0],thread[1],thread[2],thread[3],fill=THREAD_COLOR, width=THREAD_WIDTH)
   #   display_coordinates(CANVAS,x1,y1)
   #   display_coordinates(CANVAS,x2,y2)
   #   draw_point(CANVAS,x1,y1,"red") 
   #   draw_point(CANVAS,x2,y2,"blue") 

     print("coor",x1,y1,x2,y2)


def CreatePossibleThreads( FRAMENAILPOINTS ,OX,OY , REDUCED_RESO_PIXEL_GAP):
    

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


         #   conditions for iteration number depening on the value of
         # v = abs((s.real - e.real)/gap) 
         # case 1 : integral value : iteration num =  v+1
          #case 2 : non-integral value : floor(v)+1 +1  
          ## apply the condition before running the loop so that the functions differently for different cases

           iteration_num = int(abs((s.real - e.real)/gap))+1
           if s.real == e.real :
              iteration_num = int(abs((s.imag - e.imag)/gap)) +1
           pointsOntheline = []
           
           for k in range(iteration_num):
              
            #   print(k)
              if s.real>e.real:
                 x_coo = s.real -(k*int(gap))
                 y_coo  = lineEq(x_coo)
                 pointsOntheline.append(( round(x_coo,2) , round(y_coo,2) ))
              elif s.real == e.real:
                 x_coo = s.real
                 if s.imag > e.imag :
                    y_coo = s.imag - (k*gap)
                 else:   
                   y_coo = s.imag + (k*gap) 
              else :
                 x_coo = s.real +(k*int(gap))
                 y_coo  = lineEq(x_coo)

                 pointsOntheline.append((round(x_coo,2) , round(y_coo,2)  ))
           
           lines.append(pointsOntheline)

       totalLines.append(lines)
    print("length of totalLines list" + str(len(totalLines))) 
    print("length of lines through every point on the frame to other points on the frame "+ str(len(totalLines[0])))   




    #____Doing filteration of best line out of Lines[n], on the basis of darkness of the pixels lying on frame___
   
    


    return totalLines              