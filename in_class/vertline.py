#stadelmane_broadbentc.py
#Eric Stadelman Charlie Broadbent
#create 4 filtered photos


from cImage import *
from sys import *
def vertLine(imag, lineWidth):
    linePic= imag.copy()
    numPix = imag.getNumPixels() - imag.getNumPixels//2
    for pixel in range(numPix):
        p imag.getPixel1D(pixel)
        p.red=0
        p.green=0
        p.blue=255
        linePic.setPixel1D(pixel,p)
    return linePic
    

def main():
    # open AA.gif and use its dimensions to make a suitably sized window
    origImage = FileImage("AA.gif")
    win = ImageWin("dogs! are great!",origImage.getWidth()*2,origImage.getHeight()*2)
    origImage.draw(win)

    linePicture = vertLine(origImage)
    linePicture.setPosition(0, origImage.getHeight()+1)
    linePicture.draw(win)
   
    # ask for input so window stays open until user hits enter on terminal
    input("enter to quit")
main()
