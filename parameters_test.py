#!/usr/bin/env python
# coding: utf-8

import pytest
import cv2
import tempfile
import shutil
import os

# import the package modules 
from Workflow.packages import *

#declaring variables:
strips = 7

#copy image from test folder:

#remove existing file if in input folder
#os.remove("./Workflow/ImageStates/Edges/Otsu/0.png" )

#pre-cut test image 
test_1= r'./test_images/hcc_strips/'

#copy of test image to input file for HCC2
test_out_otsu= r'.Workflow/ImageStates/Edges/Otsu/'

#function to copy test image to input file
#shutil.copy2(test_1, test_out_otsu)

def copytree(test_1, test_out_otsu, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(test_1,"1.png")
        d = os.path.join(test_out_otsu, '1.png')
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
            
#Remove all files from destination:
clean = r'./Workflow/ImageStates/Edges/Otsu/'
#for filename in os.listdir(clean):
    #if filename.endswith(".png") or filename.endswith(".npy"):
        
        #remove files in Otsu output folder 
        #os.remove("./Workflow/ImageStates/Edges/Otsu/" + str(filename))
        
        #remove files in Kmeans output folder 
        #os.remove("./Workflow/ImageStates/Edges/Kmeans/" + str(filename))
    #else:
        #continue 
        
#source = r'./test_images/hcc_strips/'
#destination_Otsu = ''
#destination_Kmeansn = ''

#copy images from test folder to Edges/Otsu and Edges/Kmeans:
#for x in os.listdir(source):
   # if x.endswith(".png"):
        #copy images from test folder to Edges/Otsu:
        #s = source + str(x)
        #destination_Otsu = ".Workflow/ImageStates/Edges/Otsu/"+ str(x)
        #shutil.copy2(s, destination_Otsu)
        
        #copy images from test folder to Edges/Kmeans:
        #destination_Kmeans = "./Workflow/ImageStates/Edges/Kmeans/"+ str(x)
        #shutil.copy2(s, destination_Kmeans)
   # else:
        #continue 

def test_HCC2():

    assert parameters.HCC2(7)== 0.0824742268
    #assert parameters.HCC2(7)[1]== 0.0824742268

