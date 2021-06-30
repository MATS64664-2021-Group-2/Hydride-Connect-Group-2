#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python
# coding: utf-8

import pytest
import cv2
import os
import glob
import sys
from PIL import Image
from numpy import asarray


# Making the test look in the right place 

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


# import the package modules 
from Workflow.packages import connectivity

# copy from test image folder to Otsu strips         
src = "test_images/Gradient.png"
dst = "Workflow/ImageStates/ImagePrep/Blurs/"

for pngfile in glob.iglob(os.path.join(src, "*.png")):
    shutil.copy(pngfile, dst)

strips = 7 

image = Image.open('Workflow/ImageStates/ImagePrep/Blurs/0.png')

data = asarray(image)

#convert image into numpy array 


def test_otsu():
    
    answer = connectivity.otsu(strips)
    
    assert answer == data

