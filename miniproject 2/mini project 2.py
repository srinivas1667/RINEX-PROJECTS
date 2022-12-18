# CREATING AN 8X8 CHECKER BOARD

import numpy as np
import cv2

img = np.zeros((800,800,3))

a1=0
b1=0


# CODE FOR THE 1st column , 3rd , 5th ....
for i in range(0,4):
    for j in range(0,8):
        img[0+a1:100+a1,0+b1:100+b1] = 255,255,255
        a1 = a1+200

    a1=0
    b1= b1+200
    

# CODE FOR 2ND ,4TH,6TH....columns
a2 = 0
b2 = 0
for i in range(0,4):
    for j in range(0,8):
        img[100+a2:200+a2,100+b2:200+b2] = 255,255,255
        a2 = a2+200

    a2=0
    b2= b2+200
    



cv2.imshow('8X8 Checker Box',img)







cv2.waitKey(0)
cv2.destroyAllWindows()



               
