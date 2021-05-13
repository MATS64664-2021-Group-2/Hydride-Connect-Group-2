# We import the packages we need

import numpy as np
import cv2


def vertical_strips(SecNum,img):
    #this small loop confirms that the total width of the image can be split into the defined number of sections, 
    # if not another section will be added until equality is achieved
    while True:
        if (np.size(img,1) % SecNum) !=0:
            SecNum += 1
        else:
                break

    #introducing a tracker variable allows for simple passing of number of slices between chunks
    strips = 0

    #this loop takes the image and vertically slices it in equal widths as defined above
    for x in range(0,np.size(img,1),SecNum):
            x1 = x + SecNum
            section = img[0:np.size(img,0), x:x1]
            
            cv2.imwrite("ImagePrep/Sections/" + str(strips) +".png",section)
            
            strips +=1
    
    return strips


