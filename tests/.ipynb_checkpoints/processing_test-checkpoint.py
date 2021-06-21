#!/usr/bin/env python
# coding: utf-8

# This sections imports standard modules to us 
import os
import sys
import pytest 
import cv2


# Making the test look in the right place 

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#Importing package to be tested:
from Workflow.packages import processing

# The data of the image that is going to be analysed are storaged in the "img" variable

img_1 = cv2.imread('test_images/45Degrees.png',0)

def test_vertical_strips():
       assert processing.vertical_strips(15,img_1) == 7
