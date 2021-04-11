# cartoonize-images
A program which filters images into cartoon. Build using python

This program uses Opencv library and also Pillow library.

Image processed by Canny Edge algorithm and then Morphological operations are performed to transform the edges such that small holes are covered.
Blurred orginal image is placed as background and the processed image with edges is overlaid.
Since opencv uses NumPy arrays, the array image had to be converted into into RGB image hence used Pillow library
