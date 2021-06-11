# We import the packages we need
import numpy as np
import cv2
#from packages import Edge

def otsu(strips):
    """

    Parameters
    ----------
    strips : int
        number of strips in which the image was split

    Returns
    -------
    OtsuThresh : numpy.ndarray
            data of the image after Otsu thresholding
            
    """
#knowing the number of strips, any actions can be repeated across the entirety of the slices easily
    for i in range(strips):
        Blur = cv2.imread("./ImageStates/ImagePrep/Blurs/" + str(i) + ".png", 0)
#Using the inbuilt opencv otsu thresholding method and defining it as a binary threshold, aka only black and white, 
# both a thresholded image is produced and the automatically detected thresholding value is found.   
        ThreshValue, ThreshOtsu = cv2.threshold(Blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
        cv2.imwrite("ImageStates/Thresholding/Otsu/" + str(i) +".png",ThreshOtsu)
        np.save("ImageStates/Thresholding/Otsu/" + str(i), ThreshOtsu)
    
#As earlier, the individual slices are saved to their own directory and an overall image is made from reattaching the slices.
        if i > 0:
            if i == 1:
                ImgL = cv2.imread("./ImageStates/Thresholding/Otsu/" + str(i-1) + ".png")
                ImgR = cv2.imread("./ImageStates/Thresholding/Otsu/" + str(i) + ".png")
                OtsuThresh = np.concatenate((ImgL, ImgR), axis=1)
            else:
                ImgR = cv2.imread("./ImageStates/Thresholding/Otsu/" + str(i) + ".png")
                OtsuThresh = np.concatenate((OtsuThresh, ImgR), axis=1)
    return OtsuThresh


def kmeans(strips):
    
    """
    

    Parameters
    ----------
    strips : int
        number of strips in which the image was split

    Returns
    -------
    KThresh : numpy.ndarray
            data of the image after k-means thresholding

    """

    for i in range(strips):
        ImgIn = cv2.imread("./ImageStates/ImagePrep/Blurs/" + str(i) + ".png",1)
    
        Blur = cv2.cvtColor(ImgIn, cv2.COLOR_BGR2GRAY)

        reshapedImage = np.float32(Blur.reshape(-1, 3))

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)

    #The number of channels is defined for the k-means method, as it's black and white "2" is chosen
        k = 2

        ret, labels, clusters = cv2.kmeans(reshapedImage, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        clusters = np.uint8(clusters)
    
        Sec = cv2.imread("./ImageStates/ImagePrep/Sections/" + str(i) + ".png")
        Sec = cv2.cvtColor(Sec,cv2.COLOR_BGR2GRAY)

        intermediateImage = clusters[labels.flatten()]
        clusteredImage = intermediateImage.reshape((Sec.shape))
    
        cv2.imwrite("ImageStates/Thresholding/Kmeans/" + str(i) +".png",clusteredImage)
    
    #As earlier, the individual slices are saved to their own directory and an overall image is made from reattaching the slices.
        if i > 0:
            if i == 1:
                ImgL = cv2.imread("./ImageStates/Thresholding/Kmeans/" + str(i-1) + ".png")
                ImgR = cv2.imread("./ImageStates/Thresholding/Kmeans/" + str(i) + ".png")
                KThresh = np.concatenate((ImgL, ImgR), axis=1)
            else:
                ImgR = cv2.imread("./ImageStates/Thresholding/Kmeans/" + str(i) + ".png")
                KThresh = np.concatenate((KThresh, ImgR), axis=1)
    return KThresh



def edges(strips):
    """
    

    Parameters
    ----------
    strips : int
        number of strips in which the image was split

    Returns
    -------
    EdgesO : umpy.ndarray
            data of the connectivity of the hydrides after Otsu thresholding
    EdgesK : numpy.ndarray
            data of the connectivity of the hydrides after k-means thresholding

    """
    for i in range(strips):
    
        imgO = cv2.imread("./ImageStates/Thresholding/Otsu/" + str(i) + ".png", 0)
        imgK = cv2.imread("./ImageStates/Thresholding/Kmeans/" + str(i) + ".png", 0)
    
        CannyImgO = auto_canny(imgO)
        CannyImgK = auto_canny(imgK)
    
        cv2.imwrite("ImageStates/Edges/Otsu/" + str(i) +".png",CannyImgO) 
        cv2.imwrite("ImageStates/Edges/Kmeans/" + str(i) +".png",CannyImgK) 
    
        if i > 0:
            if i == 1:
                ImgL = cv2.imread("./ImageStates/Edges/Otsu/" + str(i-1) + ".png")
                ImgR = cv2.imread("./ImageStates/Edges/Otsu/" + str(i) + ".png")
                EdgesO = np.concatenate((ImgL, ImgR), axis=1)
            
                ImgL = cv2.imread("./ImageStates/Edges/Kmeans/" + str(i-1) + ".png")
                ImgR = cv2.imread("./ImageStates/Edges/Kmeans/" + str(i) + ".png")
                EdgesK = np.concatenate((ImgL, ImgR), axis=1)
            else:
                ImgR = cv2.imread("./ImageStates/Edges/Otsu/" + str(i) + ".png")
                EdgesO = np.concatenate((EdgesO, ImgR), axis=1)
            
                ImgR = cv2.imread("./ImageStates/Edges/Kmeans/" + str(i) + ".png")
                EdgesK = np.concatenate((EdgesK, ImgR), axis=1)
    return EdgesO, EdgesK

def auto_canny(image, sigma=0.33):
	"""
    
    This function gets rid off the edges of the image to not be counted as
    hydride's edges
    
    Parameters
    ----------
    image : numpy.ndarray
        data of the processed image so far
    sigma : int
        The default is 0.33.

    Returns
    -------
    edged : numpy.ndarray
        data of the processed image without the external edges of the picture

    """
    
    # compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged