# cartoonize-images
A program which filters images into cartoon. Built using python

This program uses Opencv library and also Pillow library.

Image processed by Canny Edge algorithm and then Morphological operations are performed to transform the edges such that small holes are covered.
Blurred orginal image is placed as background and the processed image with edges is overlaid.
Since opencv uses NumPy arrays, the array image had to be converted into into RGB image hence used Pillow library

Please paste file location in 'filename' variable for successful execution.

NOTE: Opencv should be installed. When program is executed succesfully, a window will pop with processed result image.

Code written using Jupyter notebook
