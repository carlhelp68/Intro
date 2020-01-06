from cImage import *
from sys import *
def scale(image, s):
    height_new = int(image.getHeight()*s)
    width_new= int(image.getWidth()*s)
    scaleImage = EmptyImage(width_new,height_new)
    for x in range(width_new):
        for y in range(height_new):
            newPixel = image.getPILPixel(int(x//s),int(y//s))
            scaleImage.setPILPixel(x,y, newPixel)    
    return scaleImage
def blur(image,radius):
    
    height = image.getHeight() #245
    width = image.getWidth() #327
    print(height)
    print(width)
    print(image.getPILPixel(image.getWidth()-1, image.getHeight()-1))
    blurImage = EmptyImage(width, height)
    for i in range(0,width-1):
        for j in range(0,height-1):
            #set up square dimensions to average
            right = min(i+radius, width-1)
            left = i if i < radius else (i - radius)
            down = min(j+radius, height-1)
            up = j if j < radius else (j-radius)

            #initalize variables outside loop    
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            count = 0
            for x in range(left,right-1):
                for y in range(up,down-1):
                    sum_red += image.getPILPixel(x,y)[0]
                    sum_green += image.getPILPixel(x,y)[1]
                    sum_blue += image.getPILPixel(x,y)[2]
                    count += 1
            newPixel = image.getPILPixel(i,j)
            newPixel.setRed(int(sum_red/count))
            newPixel.setGreen(int(sum_green/count))
            newPixel.setBlue(int(sum_blue/count))
            blurImage.setPILPixel(i,j, newPixel)
    return blurImage

def main():
    origImage=FileImage("AA.gif")
    win = ImageWin(origImage.getWidth()*4, origImage.getHeight()*4)
    # origImage.draw(win)
    # scaleImage = scale(origImage, 0.5)
    # scaleImage.setPosition(origImage.getWidth()+1,0)
    # scaleImage.draw(win)
    blurImage = blur(origImage, 3)
    blurImage.draw(win)
    # input("Click enter to click")
    #blur(origImage, 3)
main()

