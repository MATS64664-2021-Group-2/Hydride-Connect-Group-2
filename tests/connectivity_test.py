#!/usr/bin/env python
# coding: utf-8

import pytest
import cv2

# import the package modules 
from hydride_package import *


#import images for testing 

img_45deg = cv2.imread('test_images/45Degrees.png',0)

img_0deg  = cv2.imread('test_images/Full_Horizontal.png',0)

img_90deg  = cv2.imread('test_images/Full_Vertical.png',0)

#Starting values
SecNum = 15
HydrideOtsu = 0
HydrideKmeans = 0


def test_HCC1():
# calculation for HCC is length of each Hydride in the radial direction / total length of micrograph
# radial direction is vertical direction?

    #for each of the images above confirm the output value 
strips=processing.vertical_strips(SecNum,img)

cv2.imwrite('ImageStates/ImagePrep/BlurJoined.png', processing.blur(strips))

cv2.imwrite('ImageStates/Thresholding/OtsuThresh.png', connectivity.otsu(strips))

cv2.imwrite("ImageStates/Thresholding/KThresh.png", connectivity.kmeans(strips))

cv2.imwrite("ImageStates/Edges/CannyOtsu.png", connectivity.edges(strips)[0])

cv2.imwrite("ImageStates/Edges/CannyKmeans.png", connectivity.edges(strips)[1])
       assert parameters.HCC1(HydrideOtsu, HydrideKmeans)== 1

