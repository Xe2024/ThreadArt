import cv2
import tkinter as  tk


def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

#function for calculating pixel(of reduced reso image) location and coordinate of its centre(pixel center , it is needed for algorithm i am going to build for preparing a image representing a line) corresponding to the given point's reative (w.rt frame or taking (0,0)  at the middle of the circular frame) coordinate 
# # the (x,y) represents the nail coordinate relative to frame and the function will return the centre of the pixel also with repsect to frame i.e (0,0) at the centre of the win_screen  


def locatePixel(CANVAS_CONTEXT,x,y,imagePath ,FRAME_RADIUS ,ROOT ):
         root =ROOT
         Ctx = CANVAS_CONTEXT
         frameRadius = FRAME_RADIUS
         image = cv2.imread(imagePath)
         height , width , channel = image.shape
         # z =  the height or width of the reduced reso image as both height and width are same 
         #pixelGap =( 2*frameRadius)/width
         #col = (z/2) + round(x/pixelGap) 
        #  print(height,width,channel) 

         z = width 
         pixelGap = (2*frameRadius)/width

         col = int(z/2) + int(round((x-5)/pixelGap)) 
         row = int(z/2) + int(round((y-5)/pixelGap)) 



    #_____just for debugging purposes and visually checking if pointed mouse is locating right pixeel
         label = tk.Label(root, text="row:"+str(row) +"  "+ "col"+str(col))
        #  Place the label at specific coordinates (x=50, y=50)
         label.place(x=200, y=50)
         consideredPixel = image[row,col]
         Ctx.create_rectangle(0, 0, 100, 100, fill=rgbtohex(consideredPixel[0],consideredPixel[1],consideredPixel[2]))
         return [row ,col]
#__________________________________________________________________
# #Calculating centre of the pixel by its coordinate (row,col)  relative to centre frame i.e (0,0) at the screen centre


def locatePixelCentre(ROW,COL , PIXEL_GAP  ,ROOT):
       i,j = ROW,COL
       root =ROOT
       
       if i > 19:
             y = (-0.5 +(i-19))*PIXEL_GAP

       else:
            y = (-0.5 - (19-i))*PIXEL_GAP



       if j > 19 :
             x =   (-0.5 +(j-19))*PIXEL_GAP     
         
       else:
             x =(-0.5 - (19-j))*PIXEL_GAP


       label = tk.Label(root, text= "y:" + str(y) +"  "+ "x:"+ str(x))
        #  Place the label at specific coordinates (x=50, y=50)
       label.place(x=300, y=50)      

class lineDrawer:
      def __init__(self,Canvas) :
            self.Canvas =Canvas
            self.X_o = None
            self.Y_o = None
            self.X_1 = None
            self.Y_1 = None
            self.lineId =None
      def drawLine(self,event):
            if self.X_o is None and self.Y_o is None :
                  self.X_o = event.x
                  self.Y_o = event.y
            else :
                  self.X_1 = event.x
                  self.Y_1 = event.y
                  if self.lineId :
                        self.Canvas.delete(self.lineId)
                  self.lineId = self.Canvas.create_line(self.X_o, self.Y_o, self.X_1, self.Y_1, fill="blue")
                  self.X_o, self.Y_o = self.X_1, self.Y_1





 
