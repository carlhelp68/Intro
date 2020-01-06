from cImage import *
from sys import *

#def inter(image):
first_im=FileImage("AA.gif")
second_im=FileImage("AA.gif")
height_new=(first_im.getHeight())
width_new=(first_im.getWidth())
new_pic=EmptyImage(width_new,height_new)
counter = 0
n=11
t=11

while counter<=height_new-1:
    
    if counter + n > height_new-1:
                z= counter + n
                n = n - (z-height_new)
    for i in range(n):
        for x in range(width_new):
            y = counter
            

            newPix=first_im.getPILPixel(int(x),int(y))
            new_pic.setPILPixel(x,y,newPix)   
        counter +=1
        
        
    if counter + t > height_new-1:
                z= counter + t
                t = t - (z-height_new)
        
    for i in range(t):
        for x in range(width_new):
            y=counter
            
                
            newPixel=second_im.getPILPixel(int(x),int(y))
            new_pic.setPILPixel(x,y,newPixel)        	
        counter+=1
print(counter)
            

#return new_pic







#def main():
first_im=FileImage("flowers1.gif")
win = ImageWin(first_im.getWidth()*3, first_im.getHeight()*2)
#first_im.draw(win)
y = input("HELLO")
second_im=FileImage("flowers2.gif")
second_im.setPosition(first_im.getWidth()+1,0)
second_im.draw(win)


#new_pic=inter(first_im)
#new_pic.setPosistion(first_im.getWidth()+1,0)
new_pic.draw(win)

x = input("HIT ENTER")
print(counter)
print(list)



        #newPixel = first_im.getPILPixel(x,y)
        #new_pic.setPILPixel(x,y, newPixel)







#main()






#if first_im.getWidth()> second_im.getHeight():
#	new_pic=EmptyImage(second_im.getWidth,second_im.getHeight)