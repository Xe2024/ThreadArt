import cv2
import extraModules







def GreedyAlgoLoop(CANVAS_CONTEXT, POINTS_lIST,REDUCED_RESO_IMAGE_PATH,FRAME_RADIUS , FRAME_NAIL_COUNT):
    Ctx = CANVAS_CONTEXT
    no_of_nails = FRAME_NAIL_COUNT
    nails = POINTS_lIST
    modifiedImage =REDUCED_RESO_IMAGE_PATH
    frameRadius =FRAME_RADIUS
    n =0
    # print(nails[n])
    # print(nails , len(nails))


    #________________________________________________________________________________________________________
   

    while n < 1 :
           # first we will try to calculate the nearest image pixel to the starting and endpoint of the line which comes from nailslist
           startingNail = nails[n]
           X_o = startingNail.real # x_coordinate of starting nail
           Y_o = startingNail.imag # y_coordinate of starting nail
           
           
           for nailnumber in range(0,no_of_nails):
                #  print(nailnumber)
                otherNail = nails[nailnumber]

                X_1 =otherNail.real
                Y_1 =otherNail.imag
                # print("X_o:" + str(X_o),"Y_o:" + str(Y_o) ,"X_1:" + str(X_1),"Y_1:" + str(Y_1) , nailnumber)

           n =+1
                

           
             
       
