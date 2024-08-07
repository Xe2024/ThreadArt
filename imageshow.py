from tkinter import *
from tkinter import ttk
from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk
import tkinter as  tk
import math
from imageManipulation import Scale
import GreedyAlgoLoop
import extraModules
from extraModules import lineDrawer



root = Tk()

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# print(screenWidth , screenHeight)


framenailCount = 120
CanvasHeight =screenHeight
CanvasWidth = screenWidth
Ox = CanvasWidth/2
Oy = CanvasHeight/2
frameRadius = 200
pointsList = []
reducedReso_Size = 40*40
reducedReso_pixelgap = int((2*frameRadius)/math.sqrt(reducedReso_Size))
C = Canvas(root, bg="#2B2C2B",
           height=CanvasHeight, width=CanvasWidth)


  


#_________________________________________________________________________________
#image related things

def resizePhoto(maxWidth , imagePath):
  
  originalImage = Image.open(imagePath)
  oW, oH= originalImage.size
  slope = (oH/oW) 
  nH = int(slope*maxWidth)
  newImage =  originalImage.resize((maxWidth,nH)) 
  imgcenX = maxWidth/2
  imgcenY =(nH/2)
  top_left_x =imgcenX-frameRadius
  top_left_y =imgcenY -frameRadius
  squareBox = (top_left_x ,top_left_y  , top_left_x+2*frameRadius , top_left_y + 2*frameRadius )

  croppedImage = newImage.crop(squareBox)
  grayscaledImage = croppedImage.convert('L')
  

  gsimageData = grayscaledImage.load()
  # print(gsimageData)
  reducedreso = []
  for i in range(int(math.sqrt(reducedReso_Size))):
    innerlist_reducedreso = []
    for j in range(int(math.sqrt(reducedReso_Size))):
      averagebigPixelSum=0
      for x in range(reducedReso_pixelgap):
       for y in range(reducedReso_pixelgap):
         averagebigPixelSum += gsimageData[(reducedReso_pixelgap)*i+x , (reducedReso_pixelgap)*j+y]
      innerlist_reducedreso.append(int(averagebigPixelSum/(reducedReso_pixelgap**2))) 
    reducedreso.append(innerlist_reducedreso) 
  reducedResoImage = Image.new('L', (int(math.sqrt(reducedReso_Size)),int(math.sqrt(reducedReso_Size))))
  reducedResoPixels = reducedResoImage.load()
  
  for x in range(int(math.sqrt(reducedReso_Size))):
    for y in range(int(math.sqrt(reducedReso_Size))):

      reducedResoPixels[x,y] =int(reducedreso[x][y])
  
  reducedResoImage.save("reducedreso.jpg")
  
  finalImage = Scale(reducedreso,frameRadius)
  





  return [ImageTk.PhotoImage(croppedImage), ImageTk.PhotoImage(grayscaledImage) , ImageTk.PhotoImage(finalImage)]

photos = resizePhoto(2*frameRadius,"assets/image/kitten.jpg")
C.create_image(Ox,Oy, image= photos[2])
C.create_image(Ox+2*frameRadius , Oy , image = photos[1])
C.create_image(Ox-2*frameRadius , Oy , image = photos[0] )


C.create_oval(Ox - frameRadius, Oy - frameRadius, Ox + frameRadius, Oy + frameRadius, outline='black', fill='' ,width=5)

#creating axis
C.create_line(Ox, 0, Ox, screenHeight, fill="red")
C.create_line(0, Oy, screenWidth, Oy, fill="red")


#______________________________________________________________________________________________________

#_________________________________________________________________________________________________________
#creating N-points to place on the circular frame
'''
we will create these points using complex number rotations , where the angle difference  = 360/N and vectors from centre of the frame to those symmetrically placed n-points will be the C.numb represented by 
R*e**(i*(pi/180)*(360/N)). the vectors will be calculated through a loop named pointsCalculator.
'''

#loop for calculating points on the frame
def pointCalculator(FRAMENAILCOUNT , OX , OY , RADIUSOFFRAME ):
  R=RADIUSOFFRAME
  N=FRAMENAILCOUNT
  for i in range(N):
     theta = ((math.pi)/180)*(360/N)
     x_comp = R*math.cos(i*theta)
     y_comp = R*math.sin(i*theta)
     

     a = round(x_comp,2)
     b= round(y_comp,2)
     Z = a + b*(1j)

     # push the Z into the pointsList[]
     pointsList.append(Z)

pointCalculator(framenailCount,Ox,Oy , frameRadius)

def draw_point(x, y,OX,OY, color="white"):


# drawing points on the frame 
  """Draws a point on the canvas.

  Args:
      x: The x-coordinate of the point.
      y: The y-coordinate of the point.
      color: The color of the point (defaults to black).
  """
  radius = 4  # Adjust radius as needed
  C.create_oval((OX+x) - radius, (OY+y) - radius,
                     (OX+x) + radius,( OY+y) + radius,
                     fill=color)

#DRawing points on the frame from poistslist

for i in range(framenailCount):
  z = pointsList[i]
  x= z.real
  y =z.imag
  draw_point(x,y,Ox,Oy,"white" );
 
#_______________________________________________________________________________________________________

# Actual Greedy algorithm for calculating the suitable lines 
#_______________________________________________________________________________________________________

def findSuitableLines(CANVAS_CONTEXT, POINTS_lIST,REDUCED_RESO_IMAGE_PATH,FRAME_RADIUS , FRAME_NAIL_COUNT,ROOT):
  GreedyAlgoLoop.GreedyAlgoLoop(CANVAS_CONTEXT, POINTS_lIST,REDUCED_RESO_IMAGE_PATH,FRAME_RADIUS , FRAME_NAIL_COUNT,ROOT)


reducedResoImagePath = "C:/Users/COMPUTER/Desktop/ThreadArt/reducedreso.jpg"
findSuitableLines(C , pointsList,reducedResoImagePath,frameRadius, framenailCount,root)
  
  



drawer =lineDrawer(C)
def click(e):
  drawer.drawLine(e)
  

        
  pixelLocation =  extraModules.locatePixel(C , (e.x - Ox) , (e.y - Oy)  ,reducedResoImagePath , frameRadius ,root  )
  extraModules.locatePixelCentre(pixelLocation[0] ,pixelLocation[1] ,10 ,root)

# #_____just for debugging ___
root.bind("<Button-1>", click)  # Left mouse button click














C.grid()












def close_window():
  root.destroy()
# Create a quit button
quit_button = tk.Button(root, text="Quit", command=close_window)
quit_button.grid(column=100,row=0)
root.mainloop()