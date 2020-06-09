import cv2
import numpy as np

# Read images : src image will be cloned into dst
bg = cv2.imread("C:\\Users\\lauvi\\Downloads\\300272624.jpg")
obj = cv2.imread("pic/Mask3.png")

# Create an all white mask
mask = 255 * np.ones(obj.shape, obj.dtype)

# The location of the center of the src in the dst
width, height, channels = bg.shape
center = (int(height / 2), int(width / 2))

# Seamlessly clone src into dst and put the results in output
normal_clone = cv2.seamlessClone(obj, bg, mask, center, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(obj, bg, mask, center, cv2.MIXED_CLONE)

# Write results
cv2.imwrite("pic/opencv-normal-clone-example.jpg", normal_clone)
cv2.imwrite("pic/opencv-mixed-clone-example.jpg", mixed_clone)