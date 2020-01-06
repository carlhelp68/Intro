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
#def blur(image,radius):
 #   blurImage = EmptyImage(
def main():
    origImage=FileImage("AA.gif")
    win = ImageWin(origImage.getWidth()*4, origImage.getHeight()*4)
    origImage.draw(win)
    scaleImage = scale(origImage, 0.5)
    scaleImage.setPosition(origImage.getWidth()+1,0)
    scaleImage.draw(win)
    input("Click enter to click")
main()