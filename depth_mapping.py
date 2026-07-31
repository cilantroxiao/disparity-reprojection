import cv2
import numpy as np

path = "/Users/cilantro/Downloads/Adirondack-imperfect/"
img = path + "im0.png"
dmap = path + "disp0.pfm"
calib_data = path + "calib.txt"

# Copy-pasted from doc directly.
# Later will replace with parsing code
baseline = 176.252
f = 4152.073 
doffs = 213.084

# Load PFM file 
darray = cv2.imread(dmap, cv2.IMREAD_UNCHANGED)
# print("Array Shape: ", darray.shape)
# print("Data Type: ", darray.dtype)
# depth = disp_array[1900, 2800]

# Z = baseline * f / (d + doffs) 
# From https://vision.middlebury.edu/stereo/data/scenes2014/: 
Z_left = baseline * f / (darray + doffs)

img_array = cv2.imread(img)
'''
print("Array Shape: ", img_array.shape)
print("Data Type: ", img_array.dtype)
print(img_array)

if image is None:
	print("Error: Image could not be loaded")
else:
	cv2.imshow("Window Title", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
'''

# forward warp implement









