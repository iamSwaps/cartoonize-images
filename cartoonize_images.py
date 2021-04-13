#!/usr/bin/env python
# coding: utf-8

# In[176]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

filename= r'C:\Users\Admin\Desktop\angelina-jolie-1280x720-wallpaper-7683.jpg'


def filterr(image1):
    plt.subplot(231)
    plt.imshow(image1)
    
    blured = cv2.blur(image1,(3,3))  #blur image
    
    plt.subplot(232)
    plt.imshow(blured)
    
    sigma=0.33
    v = np.median(image1)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    
    image_with_edges = cv.Canny(image1 , lower, upper) #auto canny algorithm to find edges
    
    plt.subplot(233)
    plt.imshow(image_with_edges, cmap='gray')
    
    kernel = np.ones((3,3),np.uint8)
    closing = cv.morphologyEx(image_with_edges, cv.MORPH_CLOSE, kernel) #thickening and cleansing edges
    
    plt.subplot(234)
    plt.imshow(closing, cmap='gray')
    
    close_neg = cv.bitwise_not(closing) #inverting color b2w & w2b
    
    plt.subplot(235)
    plt.imshow(close_neg, cmap='gray')
    
    edged = cv.cvtColor(close_neg, cv.COLOR_GRAY2RGB) #converted gray image to rgb image
    
    dst = cv.bitwise_and(blured,edged) #add both blur and edged images
    
    PIL_image = Image.fromarray(np.uint8(dst)).convert('RGB')
    PIL_image = Image.fromarray(dst.astype('uint8'), 'RGB')
    PIL_image.show()
    
    
    plt.subplot(236)
    plt.imshow(dst)
    
    
image = plt.imread(filename, 0)
filterr(image)
