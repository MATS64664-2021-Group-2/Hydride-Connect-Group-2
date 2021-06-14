#!/usr/bin/env python
# coding: utf-8
import pytest 
import os 
import cv2

# import the package modules 
from Workflow.packages import *


# The data of the image that is going to be analysed are storaged in the "img" variable
img_1 = cv2.imread('test_images/45Degrees.png',0)


def test_vertical_strips():
       assert processing.vertical_strips(15,img_1) == 7

#def test_blur():
#blur function takes strips created in the vertical_strips
#stitches them together 
#make strips save into temp directory 
    #strips=processing.vertical_strips(15,img_1)
    #check for the final image has not gotten bigger 
    #check the blurring is correct 
    #assert processing.blur(strips)== 1
    
