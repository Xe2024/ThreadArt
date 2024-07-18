from PIL import Image, ImageTk



def Scale(REDUCEDRESO , FRAMERADIUS ):
    print(len(REDUCEDRESO))

    finalImage = Image.new("L" , (2*FRAMERADIUS,2*FRAMERADIUS))
    finalImagePixelData = finalImage.load()
    gap = (2*FRAMERADIUS)/len(REDUCEDRESO)
    for i in range(len(REDUCEDRESO)):
        for j in range(len(REDUCEDRESO)):
            for x in range(round(gap)):
              for y in range(round(gap)):
                  finalImagePixelData[ int(gap*i)+ x, int(gap*j)+y] = int(REDUCEDRESO[i][j])
    finalImage.save("checkfinal.jpg") 
    return finalImage
                
