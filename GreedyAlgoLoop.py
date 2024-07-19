import cv2
import extraModules
import threading






def GreedyAlgoLoop(CANVAS_CONTEXT, POINTS_lIST,REDUCED_RESO_IMAGE_PATH,FRAME_RADIUS , FRAME_NAIL_COUNT ,ROOT):
    root = ROOT
    Ctx = CANVAS_CONTEXT
    no_of_nails = FRAME_NAIL_COUNT
    nails = POINTS_lIST
    modifiedImage =REDUCED_RESO_IMAGE_PATH
    frameRadius =FRAME_RADIUS
    n =0
    # print(nails[n])
    # print(nails , len(nails))

    #Setting the initial starting nail 
    currentNail_no =0 
    currentNail = nails[0]


    while n<1:

        Xo , Yo  = currentNail.real ,currentNail.imag
        # print(Xo ,Yo)
    #________________________________________________________________________________________________________
        
        for nail in nails :
            if nail.real != Xo  or nail.imag != Yo:
                X1 = nail.real 
                Y1 = nail.imag
               
                # print("Xo:"+str(Xo),"Yo:"+str(Yo),"X1:"+str(X1),"Y1:"+str(Y1) , " "+ str(N))
                

        n=1

              
     








    
           
             
       
