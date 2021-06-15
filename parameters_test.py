#!/usr/bin/env python
# coding: utf-8

import pytest
import cv2
import shutil
import os
import glob

from pathlib import Path

# import the package modules 
from Workflow.packages import *

#declaring variables:
strips = 7

#Remove all files from destination:
clean_otsu = "./Workflow/ImageStates/Edges/Otsu/"
clean_kmean = "./Workflow/ImageStates/Edges/Kmeans/"

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
    
# copy from test image folder to Otsu strips         
#src = "./test_images/hcc_strips/"
#dst = "./Workflow/ImageStates/Edges/Otsu/"

#for pngfile in glob.iglob(os.path.join(src, "*.png")):
#    shutil.copy(pngfile, dst)

def test_HCC2():
        c = parameters.HCC2(strips)[2]
        
        src = "./test_images/hcc_strips/"
        dst = "./Workflow/ImageStates/Edges/Otsu/"

        for pngfile in glob.iglob(os.path.join(src, "*.png")):
            shutil.copy(pngfile, dst)
        assert c == 0.0824742268 

