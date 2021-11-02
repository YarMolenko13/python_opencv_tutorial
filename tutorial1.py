# introduction
import cv2

img_jpg = cv2.imread('assets/Java_logo.jpg', 0)
img_png = cv2.imread('assets/logo.png', -1)

# resizing the image 
img_cropped = cv2.resize(img_png, (500, 400)) # pixels
img_scaled = cv2.resize(img_png, (0,0), fx=0.5, fy=0.3) # procent

# rotating the image
img_rotated = cv2.rotate(img_cropped, cv2.cv2.ROTATE_90_CLOCKWISE)

# writing the image
cv2.imwrite('output/modified_logo.png', img_rotated)

cv2.imshow('Java logo', img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()