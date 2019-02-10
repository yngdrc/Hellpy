#python3 main.py [img_path]

from PIL import Image
import sys
import numpy as np
import matplotlib.pyplot as plt
import os

#ARGS-----------------------------------------------------
#file_name = sys.argv[0]
#image = sys.argv[1]
#---------------------------------------------------------

#FUNCTIONS------------------------------------------------
def getImage( path ):
    im = Image.open(path)
    w, h = im.size
    return (im, w, h)

def pixelsToArr( image ):
    im_pixels = np.asarray(image)
    return im_pixels

def imgFromArr( array ):
    image = Image.fromarray(array.astype('uint8', 'RGB'))
    return image

def imgHistogram( image ):
    histogram = getImage(image)[0].histogram()
    r = histogram[0:256]
    g = histogram[256:512]
    b = histogram[512:768]
    rgb_array = [r, g, b]
    clr_string = '#%02x%02x%02x'
    
    def getValues( value ):
        red = clr_string % (value, 0, 0)
        green = clr_string % (0, value, 0)
        blue = clr_string % (0, 0, value)
        return red, green, blue

    def createHistogram( rgb ):
        for x in range(0,3):
            plt.figure(x)
            for i in range(0,256):
                plt.bar(i, rgb[x][i], color = getValues(i)[x], edgecolor=getValues(i)[x], alpha=0.3)
            plt.show()
    createHistogram(rgb_array)

def encodeImage( image, new_name, text, i=0 ):
    img_bytes = getImage(image)[0].tobytes()
    bytearr = bytearray(img_bytes)
    for x in range(len(bytearr)-1-len(text), len(bytearr)-1):
        bytearr[x] = text.encode()[i]
        i = i+1
    img = Image.frombytes('RGB', getImage(image)[0].size, bytes(bytearr), 'raw')
    img.save(new_name+".png")
    #os.system("mv "+new_name+".png "+new_name+".jpg")
    #print(img.tobytes())

def decodeImage( path ):
    img = getImage(path)[0]
    #print(img.tobytes())
    return img.tobytes()
#--------------------------------------------------------
