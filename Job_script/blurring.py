# We import the packages we need
import numpy as np
import cv2

def blur(strips):
    
    #following from this, the slices are then blurred to reduce noise and transformed to their original black and white colour
    for i in range(0,strips):
        Sec = cv2.imread("./ImagePrep/Sections/" + str(i) + ".png")
    
        Sec = cv2.cvtColor(Sec,cv2.COLOR_BGR2RGB)
    
        Blur = cv2.GaussianBlur(Sec, (7,7),0)
        cv2.imwrite("ImagePrep/Blurs/" + str(i) +".png",Blur)

        #while technically unnecessary, this stage restitches the blured slices to allow for viewing of the transformed image
        if i > 0:
            if i == 1:
                ImgL = cv2.imread("./ImagePrep/Blurs/" + str(i-1) + ".png")
                ImgR = cv2.imread("./ImagePrep/Blurs/" + str(i) + ".png")
                BlurJoin = np.concatenate((ImgL, ImgR), axis=1)
            else:
                ImgR = cv2.imread("./ImagePrep/Blurs/" + str(i) + ".png")
                BlurJoin = np.concatenate((BlurJoin, ImgR), axis=1)
    return BlurJoin
