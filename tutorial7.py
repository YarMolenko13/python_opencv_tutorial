# template matching
import numpy as np
import cv2

img = cv2.imread('assets/soccer_practice.jpg', 0)
template = cv2.imread('assets/ball.png', 0)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
	img2 = img.copy()
	
	result = cv2.matchTemplate(img2, template, method)
