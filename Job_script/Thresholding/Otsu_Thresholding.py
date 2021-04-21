#!/usr/bin/env python
# coding: utf-8

# Import any necessary modules as required
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# First the file data has to be imported from the initial processing
def Otsu():
    
    img = cv2.imread("image.jpg",0)
    
# Use a Gaussian blurring technique on the image to reduce noise - the area for blurring was chosen as (3,3) to maintain accuracy, test
    Blur = cv2.GaussianBlur(img, (3,3),0)
    
# Use adaptive Otsu method for gaining threshold value
    ThreshValue, ThreshImg = cv2.threshold(Blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    plt.imshow(ThreshImg, 'gray')
    
    return ThreshImg


# To transfer the data into a 2D image matplotlib is required as shown:
#   from matplotlib import pyplot as plt
#   plt.imshow(ThreshImg, 'gray')
