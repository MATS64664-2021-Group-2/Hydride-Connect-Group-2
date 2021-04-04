# -*- coding: utf-8 -*-

"Loading an image grom GitHub"

import requests

url_image= "https://github.com/MATS64664-2021-Group-2/Hydride-Connect-Group-2/tree/main/Sample-Micrographs-main/Example%20Micrographs%20Python%20Course%20Pratheek"


def image(image_name):
    img = requests.get(url_image).content
    with open(image_name, 'wb') as img_file:
        img_file.write(img)
    return img