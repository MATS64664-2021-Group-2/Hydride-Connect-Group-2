Read me file: 

Aim of the project: Characterize hydride connectivity in Zr alloys.

Description of the project: Hydrides are a major concern in Zr alloys due to their embrittling effect. Characterizing their connectivity would allow for the creation of tougher Zr alloys for nuclear applications. The project consists of loading up existing micrographs of Zr alloy microstructures, binarizing them using thresholding (otsu, k-means and adaptive Gauss thresholding) and devising a method to study their connectivity. The project is carried out using GitHub.

Report link: https://www.overleaf.com/5247653557zpchnxykpztr

Testing:

Tests were created to make sure the main funcations were working properly.
Input files were manually made with known outputs.

Function:
    parameters_test.py 

    HCC2():
        Description:
            HCC2 calculates the Hydride Continuity co-efficient values using the Otsu and Kmeans methods
        Input: 
            Images manually sliced with known HCC values. 
           
        Method:
            HCC value was calculated by looking at the ratio of hieght of hydrides at slice boundaries to length total hieght of micrograph

Function:
    processing_test.py
    
    vertical_strips():
        Description: 
            Vertical strips splits the image into sections which are then transformed in consequent proccesses.
        Input: 
            Initial number of strips for loop and Test image
        Output:
            Number which the length of image is divisble by
            
       
Function:
    thresholding_test.py
    
    
    otsu():
        Description:
            Checking the threshold when image is transformed to black and white form grey scale
        Input:
            Grey scale image saved as indivual strips in test folder 
        Output: 
            Numpy D-Array which can be compared to the final image
    

