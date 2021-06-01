# Import the necessary packages

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