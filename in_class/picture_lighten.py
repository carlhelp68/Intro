# Author: Sherri Goings
# Simple example using cImage to filter a .gif to be in greyscale
# Also includes helper function to use in saturate filter

from cImage import *


def main():
    # open AA.gif and use its dimensions to make a suitably sized window
    origImage = FileImage("AA.gif")
    win = ImageWin("dogs! are great!",origImage.getWidth()*2,origImage.getHeight())
    origImage.draw(win)

    # ask for input so window stays open until user hits enter on terminal
    input("enter to quit")

main()