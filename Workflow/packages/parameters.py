# We import the packages we need
import numpy as np
import cv2


def HCC1(HydrideOtsu,HydrideKmeans):
    """
    

    Parameters
    ----------
    HydrideOtsu : int
        starting value for the hydride counting
    HydrideKmeans : int
        starting value for the hydride counting

    Returns
    -------
    AVG_HCC_Otsu : int
        HCC mean value when Otsu thresholding was applied
        
    K-means HCC : int
        HCC mean value when K-means thresholding was applied
    """
    
    imgO = cv2.imread("./ImageStates/Edges/CannyOtsu.png", 0)
    imgK = cv2.imread("./ImageStates/Edges/CannyKmeans.png", 0)

    HCC_Otsu =[]
    HCC_Kmeans = []

    for i in range(np.size(imgO,1)):
        for j in range(np.size(imgO,0)):
            if imgO[j,i] > 0:
                HydrideOtsu += 1
        HCC_Otsu.append(HydrideOtsu/(np.size(imgO,0)))
        HydrideOtsu = 0
    
    for i in range(np.size(imgK,1)):
        for j in range(np.size(imgK,0)):
            if imgK[j,i] > 0:
                HydrideKmeans += 1
        HCC_Kmeans.append(HydrideKmeans/(np.size(imgK,0)))
        HydrideKmeans = 0

    AVG_HCC_Otsu = sum(HCC_Otsu)/len(HCC_Otsu)
    AVG_HCC_Kmeans = sum(HCC_Kmeans)/len(HCC_Kmeans)

    return print("Otsu HCC: ", AVG_HCC_Otsu,"\n K-means HCC: ", AVG_HCC_Kmeans)

def HCC2(strips):
    """
    

    Parameters
    ----------
    strips :  int
        number of strips in which the image was split

    Returns
    -------
    ContOtsu : numpy.ndarray
        data of Otsu-thresholded image after merging all the srtips
    ContKmeans : numpy.ndarray
        data of k-means-thresholded image after merging all the srtips
    OtsuHCC : int
        HCC mean value when Otsu threshold was applied
    kmeansHCC : int
        HCC mean value when K-means threshold was applied

    """
    
    HCCrun_Otsu = []
    HCCrun_Kmeans = []

    for i in range(strips):
    
        image_src_Otsu = cv2.imread("./ImageStates/Edges/Otsu/" + str(i) + ".png")

        gray = cv2.cvtColor(image_src_Otsu, cv2.COLOR_BGR2GRAY)
        ret, gray = cv2.threshold(gray, 250, 255,0)

        contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros(image_src_Otsu.shape, np.uint8)
        largest_areas = sorted(contours, key=cv2.contourArea)
        cv2.drawContours(mask, [largest_areas[-1]], 0, (255,255,255,255), -1)
        removed = cv2.add(image_src_Otsu, mask)
    
        cv2.imwrite("ImageStates/Edges/ContOtsu/" + str(i) + ".png",removed) 
    
        cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    
        y5 = []
        h5 = []
    
        for c in cnts:
            x,y,w,h = cv2.boundingRect(c)
            y5.append(y)
            h5.append(h)
     
        for r in range(len(y5)):
            q = y5[r] + h5[r]
            for j in range(len(y5)):
                if r < j:
                    q = y5[j] + h5[j]
                    if q > y5[r]:
                        z = q - y5[r]
                        q = q-z
                        h5[j] = h5[j] - z
    
        HCCrun_Otsu.append((sum(h5))/(np.size(image_src_Otsu,0)))
    
        del cnts
    
        image_src_Kmeans = cv2.imread("./ImageStates/Edges/Kmeans/" + str(i) + ".png")

        gray_k = cv2.cvtColor(image_src_Kmeans, cv2.COLOR_BGR2GRAY)
        ret, gray_k = cv2.threshold(gray_k, 250, 255,0)

        contours, hierarchy = cv2.findContours(gray_k, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros(image_src_Kmeans.shape, np.uint8)
        largest_areas = sorted(contours, key=cv2.contourArea)
        cv2.drawContours(mask, [largest_areas[-1]], 0, (255,255,255,255), -1)
        removed = cv2.add(image_src_Kmeans, mask)
    
        cv2.imwrite("ImageStates/Edges/ContKmeans/" + str(i) + ".png",removed) 
    
        cnts = cv2.findContours(gray_k, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    
        y5 = []
        h5 = []
    
        for c in cnts:
            x,y,w,h = cv2.boundingRect(c)
            y5.append(y)
            h5.append(h)
     
        for r in range(len(y5)):
            for j in range(len(y5)):
                if r < j:
                    q = y5[j] + h5[j]
                    if q > y5[r]:
                        z = q - y5[r]
                        q = q-z
                        h5[j] = h5[j] - z
    
        HCCrun_Kmeans.append((sum(h5))/(np.size(image_src_Kmeans,0))) 
    
        if i > 0:
            if i == 1:
                ImgL = cv2.imread("./ImageStates/Edges/ContOtsu/" + str(i-1) + ".png")
                ImgR = cv2.imread("./ImageStates/Edges/ContOtsu/" + str(i) + ".png")
                ContOtsu = np.concatenate((ImgL, ImgR), axis=1)
            
                ImgL = cv2.imread("./ImageStates/Edges/ContKmeans/" + str(i-1) + ".png")
                ImgR = cv2.imread("./ImageStates/Edges/ContKmeans/" + str(i) + ".png")
                ContKmeans = np.concatenate((ImgL, ImgR), axis=1)
            else:
                ImgR = cv2.imread("./ImageStates/Edges/ContOtsu/" + str(i) + ".png")
                ContOtsu = np.concatenate((ContOtsu, ImgR), axis=1)
            
                ImgR = cv2.imread("./ImageStates/Edges/ContKmeans/" + str(i) + ".png")
                ContKmeans = np.concatenate((ContKmeans, ImgR), axis=1)
        OtsuHCC=sum(HCCrun_Otsu)/len(HCCrun_Otsu)
        kmeansHCC=sum(HCCrun_Kmeans)/len(HCCrun_Kmeans)
    return ContOtsu, ContKmeans, OtsuHCC, kmeansHCC