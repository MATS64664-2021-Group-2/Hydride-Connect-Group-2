# Import the necessary packages

import os.path
from os import path

import re

def sorted_aphanumeric(data):
    """
    This function loads the images and sorts them

    Parameters
    ----------
    data : list
        data of all the initial images

    Returns
    -------
    sort : list
        sorted data of all the images
    
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    sort=sorted(data, key=alphanum_key)
    return sort


def DirCheck():
    
    if path.exists("ImageStates") is False:
        os.mkdir("ImageStates")
    
    if path.exists("ImageStates/Connectivity") is False:
        os.mkdir("ImageStates/Connectivity")
        
    if path.exists("ImageStates/Edges") is False:
        os.mkdir("ImageStates/Edges")
        
    if path.exists("ImageStates/Edges/ContKmeans") is False:
        os.mkdir("ImageStates/Edges/ContKmeans")
        
    if  path.exists("ImageStates/Edges/ContOtsu") is False:
        os.mkdir("ImageStates/Edges/ContOtsu")
        
    if  path.exists("ImageStates/Edges/Kmeans") is False:
        os.mkdir("ImageStates/Edges/Kmeans")
        
    if path.exists("ImageStates/Edges/Otsu") is False:
        os.mkdir("ImageStates/Edges/Otsu")
        
    if path.exists("ImageStates/ImagePrep") is False:
        os.mkdir("ImageStates/ImagePrep")
        
    if path.exists("ImageStates/ImagePrep/Blurs") is False:
        os.mkdir("ImageStates/ImagePrep/Blurs")
        
    if path.exists("ImageStates/ImagePrep/Sections") is False:
        os.mkdir("ImageStates/ImagePrep/Sections")
        
    if path.exists("ImageStates/Thresholding") is False:
        os.mkdir("ImageStates/Thresholding")
        
    if path.exists("ImageStates/Thresholding/Kmeans") is False:
        os.mkdir("ImageStates/Thresholding/Kmeans")
        
    if path.exists("ImageStates/Thresholding/Otsu") is False:
        os.mkdir("ImageStates/Thresholding/Otsu")