#!/usr/bin/env python
# coding: utf-8

import pytest
import cv2
import shutil
import os
import glob
import sys
from pathlib import Path

# Making the test look in the right place 

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#Importing package to be tested:
from Workflow.packages import parameters

#declaring variables:
strips = 7

#Remove all files from destination:
clean_otsu = "Workflow/ImageStates/Edges/Otsu/"
clean_kmean = "Workflow/ImageStates/Edges/Kmeans/"

#if os.listdir(clean_otsu) != 0: 
    #for filename in os.listdir(clean_otsu):
        #if filename.endswith(".png") or filename.endswith(".npy"):

            #remove files in Otsu output folder 
            #os.remove("./Workflow/ImageStates/Edges/Otsu/" + str(filename))
            
        #else:
            #pass
    #else:
        #pass

#if os.listdir(clean_kmean) != 0: 
    #for filename in os.listdir(clean_kmean):
        #if filename.endswith(".png") or filename.endswith(".npy"):
            
            #remove files in Kmeans output folder 
            #os.remove("./Workflow/ImageStates/Edges/Kmeans/" + str(filename))
        #else:
            #pass
    #else:
        #pass
    
src = "./test_images/hcc_strips/"
dst = "./Workflow/ImageStates/Edges/Otsu/"

for pngfile in glob.iglob(os.path.join(src, "*.png")):
    shutil.copy(pngfile, dst)

def test_HCC2():
        c = parameters.HCC2(strips)[2]
        assert c == 0.0824742268 

