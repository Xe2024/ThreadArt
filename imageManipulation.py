from PIL import Image, ImageTk



def Scale(REDUCEDRESO , FRAMERADIUS ):
    print(len(REDUCEDRESO))
    print(REDUCEDRESO[59][59])

    print(REDUCEDRESO)
    finalImage = Image.new("L" , (2*FRAMERADIUS,2*FRAMERADIUS))
    finalImagePixelData = finalImage.load()
    gap = (2*FRAMERADIUS)/len(REDUCEDRESO)
    print(gap)
    for i in range(len(REDUCEDRESO)):
        for j in range(len(REDUCEDRESO)):
            for x in range(round(gap)):
              for y in range(round(gap)):
                  finalImagePixelData[ int(gap*i)+ x, int(gap*j)+y] = int(REDUCEDRESO[i][j])
    finalImage.save("checkfinal.jpg") 
    print(finalImagePixelData[399,399]) 
    return finalImage
                
