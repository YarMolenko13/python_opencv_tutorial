# modifying image
import cv2
import random

img = cv2.imread('assets/logo.png')
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.28)

# number of rows, columns, channels
img.shape

# changing pixels colors
img_c = img.copy()
for i in range(img.shape[0] // 2):
	for j in range(img.shape[1] // 2, img.shape[1]):
		img_c[i, j] = [random.randint(0, 255) for _ in range(3)]

# copying and pasting
img_w = img.shape[1]
cup = img[20:800, 50:500] # img[rows, columns]
cup_w = cup.shape[1]
img[20:800, img_w-cup_w:img_w] = cup

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()