# Readme file: Hydride_Connection

## Aim of the project: Characterize hydride connectivity in Zr alloys.

### Description of the project:
Hydrides are a major concern in Zr alloys due to their embrittling effect. Characterizing their connectivity would allow for the creation of tougher Zr alloys for nuclear applications. The project consists of loading up existing micrographs of Zr alloy microstructures, binarizing them using thresholding (otsu, k-means and adaptive Gauss thresholding) and devising a method to study their connectivity. The project is carried out using Python language and GitHub for sharing.


### Folders in Hydride_Connection:

- **test_images** --> In this folder there are images needed to apply code testing

- **tests** -->  This folder has .py files with code for code testing

- **Workflow** --> This folder has a Jupyter notebook and three subfolders described below:
     - _Workflow_Group2_ --> demo notebook to help the user to use the code
     - _packages_ --> subfolder with .py files with all the functions that are called from the demo notebook
     - _Micrographs_ --> subfolder in which there are images to be analysed
     - _ImageStates_ --> subfolder with images produced after running the code
     
         
### Prerequisites:

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
 
            

