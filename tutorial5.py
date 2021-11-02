# bitwise, mask
import numpy as np
import cv2

def nothing():
	pass

cv2.namedWindow('image')
 
cv2.createTrackbar('lowH','image',0,179,nothing)
cv2.createTrackbar('lowS','image',0,255,nothing)
cv2.createTrackbar('lowV','image',0,255,nothing)

cv2.createTrackbar('highH','image',179,179,nothing)
cv2.createTrackbar('highS','image',255,255,nothing)
cv2.createTrackbar('highV','image',255,255,nothing)

capture = cv2.VideoCapture(0)

while True:
	_, frame = capture.read()
	width = int(capture.get(3))
	height = int(capture.get(4))

	ilowH = cv2.getTrackbarPos('lowH', 'image')
	ihighH = cv2.getTrackbarPos('highH', 'image')
	ilowS = cv2.getTrackbarPos('lowS', 'image')
	ihighS = cv2.getTrackbarPos('highS', 'image')
	ilowV = cv2.getTrackbarPos('lowV', 'image')
	ihighV = cv2.getTrackbarPos('highV', 'image')

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_hsv = np.array([ilowH, ilowS, ilowV])
	higher_hsv = np.array([ihighH, ihighS, ihighV])
	# ... hsv(0-179, 0-255, 0-255)
	mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

	img = cv2.bitwise_and(frame, frame, mask=mask)
	
	cv2.imshow('image', img)
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()


# convert color
# BGR_color = np.array([[[179, 92, 41]]])
# c = print(cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV))
# c[0][0]

