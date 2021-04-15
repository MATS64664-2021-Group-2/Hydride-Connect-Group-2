#!/usr/bin/env python
# coding: utf-8

# Import any necessary modules as required
import cv2

Test = cv2.imread('Chu10.JPG',0)

# First the file data has to be imported from the initial processing
def Otsu(ImgIn):
    
# Use a Gaussian blurring technique on the image to reduce noise - the area for blurring was chosen as (3,3) to maintain accuracy
    Blur = cv2.GaussianBlur(ImgIn, (3,3),0)
    
# Use adaptive Otsu method for gaining threshold value
    ThreshValue, ThreshImg = cv2.threshold(Blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    return ThreshImg

# To transfer the data into a 2D image matplotlib is required as shown:
#   from matplotlib import pyplot as plt
#   plt.imshow(ThreshImg, 'gray')
