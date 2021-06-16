# Readme file: Hydride_Connection

- [Aim of the project](#aim-of-the-project)
- [Description of the project](#description-of-the-project)
- [Folders](#folders)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Functions](#functions)
  - [image_count](#image_count)
  - [Gaussian_thresholding](#Gaussian_thresholding)
  - [image_clean_up](#image_clean_up)


## Aim of the project: 
Characterize hydride connectivity in Zr alloys.

## Description of the project:
Hydrides are a major concern in Zr alloys due to their embrittling effect. Characterizing their connectivity would allow for the creation of tougher Zr alloys for nuclear applications. The project consists of loading up existing micrographs of Zr alloy microstructures, binarizing them using thresholding (otsu, k-means and adaptive Gauss thresholding) and devising a method to study their connectivity. The project is carried out using Python language and GitHub for sharing.


## Folders:

- **test_images** --> In this folder there are images needed to apply code testing

- **tests** -->  This folder has .py files with code for code testing

- **Workflow** --> This folder has a Jupyter notebook and three subfolders described below:
     - _Workflow_Group2.ipynb_ --> demo notebook to help the user to use the code
     - _packages_ --> subfolder with .py files with all the functions that are called from the demo notebook
     - _Micrographs_ --> subfolder in which there are images to be analysed
     - _ImageStates_ --> subfolder with images produced after running the code
     
         
## Prerequisites:

It is necessary to install the following Python packages to run the code correctly.

* matplotlib 3.4.2
  ```sh
  pip install matplotlib
  ```
* numpy 1.20.3
  ```sh
  pip install numpy
  ```
* opencv-python 4.5.2.52
  ```sh
  pip install opencv-python
  ```
* Pillow 8.2.0
  ```sh
  pip install Pillow 
  ```
* scikit-image 0.18.1
  ```sh
  pip install scikit-image
  ```
  

## Usage:
 
1. Install the Python packages described in the prerequisites section of this README file.
2. Clone the repository:
   ```sh
   git clone https://github.com/MATS64664-2021-Group-2/Hydride_Connection.git
   ```
3. Open the demo notebook called "Workflow_Group2" with Jupyter.

     This demo notebook is in: Hydride_Connection --> Workflow --> Workflow_Group2.ipynb

4. Run all the cells and see the result

## Functions:

The Gaussian thresholding consists of three functions:

### image_count:

Count the number of images within the specified folder.

Input:

path - folder path that will be counted.

Output:

len(images) - the number of files within the directory specified in "path". (Counts all images, so the folder must be empty of other files.)

### Gaussian_thresholding:

Thresholds images to binary for ease of processing.

Input:

path - directory path for images

Outputs:

imagelist - list of thresholded images (list of numpy arrays)

pure_image_list - list of unthresholded images (for subsequent plotting and comparison of results)

### image_clean_up:

Cleans up the images to display connected hydrides and plots them side-by-side for comparison.

Inputs:

image_list - list of thresholded (binary images).

pure_image_list - list of non-thresholded images (for the sake of comparison).

Output:

None - (visual representation is enough in this case, as the results could not be used for further analysis).
            
##Testing:

Tests were created to make sure the main functions were working properly.
Input files were manually made with known outputs.

## Test Function:

    parameters_test.py 

    HCC2():
        Description:
            HCC2 calculates the Hydride Continuity co-efficient values using the Otsu and Kmeans methods
        Input: 
            Images manually sliced with known HCC values. 
           
        Method:
            HCC value was calculated by looking at the ratio of height of hydrides at slice boundaries to length total height of micrograph

#Test Functions:

##processing_test.py
    
    vertical_strips():
        Description: 
            Vertical strips splits the image into sections which are then transformed in consequent processes.
        Input: 
            Initial number of strips for loop and Test image
        Output:
            Number which the length of image is divisible by
            
       
## thresholding_test.py
       
    otsu():
        Description:
            Checking the threshold when image is transformed to black and white form grey scale
        Input:
            Grey scale image saved as individual strips in test folder 
        Output: 
            Numpy D-Array which can be compared to the final image
