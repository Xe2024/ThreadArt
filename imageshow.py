from tkinter import *
from tkinter import ttk
from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk
import tkinter as  tk


root = Tk()

CanvasHeight =650
CanvasWidth = 1000
Ox = CanvasWidth/2
Oy = CanvasHeight/2
frameRadius = 200

C = Canvas(root, bg="#2B2C2B",
           height=CanvasHeight, width=CanvasWidth)



def resizePhoto(maxWidth , imagePath):
  
  originalImage = Image.open(imagePath)
  oW, oH= originalImage.size
  slope = (oH/oW) 
  nH = int(slope*maxWidth)
  newImage =  originalImage.resize((maxWidth,nH)) 
  return ImageTk.PhotoImage(newImage)

photo = resizePhoto(370,"assets/image/kitten.jpg")
C.create_image(Ox,Oy, image= photo)


C.create_oval(Ox - frameRadius, Oy - frameRadius, Ox + frameRadius, Oy + frameRadius, outline='black', fill='' ,width=5)
               
 
C.grid()












def close_window():
  root.destroy()
# Create a quit button
quit_button = tk.Button(root, text="Quit", command=close_window)
quit_button.grid(column=100,row=0)
root.mainloop()