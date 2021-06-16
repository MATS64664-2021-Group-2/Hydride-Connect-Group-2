# We import the packages we need

import numpy as np
import cv2

def vertical_strips(SecNum,img):
    """
    This function separate the image into vertical strips.
    It confirms that the total width of the image can be
    split into the initially defined number of sections, if not,
    another section will be added until equality is achieved

    Parameters
    ----------
    SecNum : int
        initial number of vertical strips 
    img : numpy.ndarray
        data of the image that is going to be analysed

    Returns
    -------
    strips : int
        number of strips in which the image was finally split
        
    """
    while True:
        if (np.size(img,1) % SecNum) !=0:
            SecNum += 1
        else:
                break
    #between 15 and 20 hypothetically no value is ignored for image width outside of prime values - excessive computing will not occur.

    #introducing a tracker variable allows for simple passing of number of slices between chunks
    strips = 0

    #this loop takes the image and vertically slices it in equal widths as defined above
    for x in range(0,np.size(img,1),SecNum):
            x1 = x + SecNum
            section = img[0:np.size(img,0), x:x1]
            
            cv2.imwrite("ImageStates/ImagePrep/Sections/" + str(strips) +".png",section)
            
            strips +=1
    
    return strips

def blur(strips):
    """
    This function blurs the strips and joins them into a new image
    
    Parameters
    ----------
    strips : int
        number of strips in which the image was split

    Returns
    -------
    BlurJoin : numpy.ndarray
        data of the image after blurring and have joined the strips

    """
    #following from this, the slices are then blurred to reduce noise and transformed to their original black and white colour
    for i in range(0,strips):
        Sec = cv2.imread("./ImageStates/ImagePrep/Sections/" + str(i) + ".png")
    
        Sec = cv2.cvtColor(Sec,cv2.COLOR_BGR2RGB)
    
        Blur = cv2.GaussianBlur(Sec, (7,7),0)
        cv2.imwrite("ImageStates/ImagePrep/Blurs/" + str(i) +".png",Blur)

        #while technically unnecessary, this stage restitches the blured slices to allow for viewing of the transformed image
        if i > 0:
            if i == 1:
                ImgL = cv2.imread("./ImageStates/ImagePrep/Blurs/" + str(i-1) + ".png")
                ImgR = cv2.imread("./ImageStates/ImagePrep/Blurs/" + str(i) + ".png")
                BlurJoin = np.concatenate((ImgL, ImgR), axis=1)
            else:
                ImgR = cv2.imread("./ImageStates/ImagePrep/Blurs/" + str(i) + ".png")
                BlurJoin = np.concatenate((BlurJoin, ImgR), axis=1)
    return BlurJoin
