#Function to load and plot images

""" This function will show all the images within a folder that have the 
format we want"""

"""
When we call the function from the Jypiter notebook, 
we need to introduce the inputs image_path and valid_images
as in the example:
     - images_path="C:\\Users\...etc"   
     - valid_images = [".jpg",".gif",".png",".tga"] """
     
from PIL import Image
import os, os.path


imgs = []

def plotim(images_path, valid_images):
    
    for f in os.listdir(images_path):
     
        #imgs[n].show()
        ext = os.path.splitext(f)[1]
        
        if ext.lower() not in valid_images:
            continue
        if ext.lower() in valid_images:
            imgs.append(Image.open(os.path.join(images_path,f)))
        
            print("Plotting image", len(imgs))
            imgs[len(imgs)-1].show()

        