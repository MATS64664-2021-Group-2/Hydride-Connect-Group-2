#!/usr/bin/env python
# coding: utf-8
import pytest 

# We import the packages we need

from matplotlib import pyplot as plt
import re
from PIL import Image
import os, os.path
from os import listdir
import matplotlib.axes
import matplotlib.image as mpimg
import numpy as np
import cv2


# import the package
import packages

# import the antigravity module
from packages import loading

# import the antigravity module
from packages import processing

#pre processing

mypath = './base_line_images/'
def_files = loading.sorted_aphanumeric(listdir(mypath))

# The data of the image that is going to be analysed are storaged in the "img" variable
img_1 = cv2.imread('./base_line_images/45Degrees.png',0)

# And the original image is plotted here
#imgplot = plt.imshow(img_1)

def test_add():
    assert processing.add(1,3)==4
    
def test_vertical_strips():
       assert processing.vertical_strips(15,img_1) == 7