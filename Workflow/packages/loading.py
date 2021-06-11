# Import the necessary packages

import os.path
from os import path
import shutil
import stat

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
        
    if path.exists("ImageStates/Edges") is False:
        os.mkdir("ImageStates/Edges")
        
    if path.exists("ImageStates/Edges/ContKmeans") is False:
        os.mkdir("ImageStates/Edges/ContKmeans")
    else: 
        shutil.rmtree("ImageStates/Edges/ContKmeans", onerror=remove_readonly)
        os.mkdir("ImageStates/Edges/ContKmeans")
        
    if  path.exists("ImageStates/Edges/ContOtsu") is False:
        os.mkdir("ImageStates/Edges/ContOtsu")
    else: 
        shutil.rmtree("ImageStates/Edges/ContOtsu", onerror=remove_readonly)
        os.mkdir("ImageStates/Edges/ContOtsu")
        
    if  path.exists("ImageStates/Edges/Kmeans") is False:
        os.mkdir("ImageStates/Edges/Kmeans")
    else: 
        shutil.rmtree("ImageStates/Edges/Kmeans", onerror=remove_readonly)
        os.mkdir("ImageStates/Edges/Kmeans")
        
    if path.exists("ImageStates/Edges/Otsu") is False:
        os.mkdir("ImageStates/Edges/Otsu")
    else: 
        shutil.rmtree("ImageStates/Edges/Otsu", onerror=remove_readonly)
        os.mkdir("ImageStates/Edges/Otsu")
        
    if path.exists("ImageStates/ImagePrep") is False:
        os.mkdir("ImageStates/ImagePrep")
        
    if path.exists("ImageStates/ImagePrep/Blurs") is False:
        os.mkdir("ImageStates/ImagePrep/Blurs")
    else: 
        shutil.rmtree("ImageStates/ImagePrep/Blurs", onerror=remove_readonly)
        os.mkdir("ImageStates/ImagePrep/Blurs")
        
    if path.exists("ImageStates/ImagePrep/Sections") is False:
        os.mkdir("ImageStates/ImagePrep/Sections")
    else: 
        shutil.rmtree("ImageStates/ImagePrep/Sections", onerror=remove_readonly)
        os.mkdir("ImageStates/ImagePrep/Sections")
        
    if path.exists("ImageStates/Thresholding") is False:
        os.mkdir("ImageStates/Thresholding")
        
    if path.exists("ImageStates/Thresholding/Kmeans") is False:
        os.mkdir("ImageStates/Thresholding/Kmeans")
    else: 
        shutil.rmtree("ImageStates/Thresholding/Kmeans", onerror=remove_readonly)
        os.mkdir("ImageStates/Thresholding/Kmeans")
        
    if path.exists("ImageStates/Thresholding/Otsu") is False:
        os.mkdir("ImageStates/Thresholding/Otsu")
    else: 
        shutil.rmtree("ImageStates/Thresholding/Otsu", onerror=remove_readonly)
        os.mkdir("ImageStates/Thresholding/Otsu")
        
        
def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)
        