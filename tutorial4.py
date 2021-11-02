# drawing on webcam capt
import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
	ret, frame = capture.read()
	frame = cv2.flip(frame, 1) # cv2.flip(img, "x-0, y-1")
	width = int(capture.get(3))
	height = int(capture.get(4))

	# ...line(img, (start_coords), (finish_coords), (BGR), thickness)
	img = cv2.line(frame, ((width//3)+(width//3), height), ((width//3)+(width//3), 0), (0, 128, 255), 4)
	img = cv2.line(img, (width//3, 0), (width//3, height), (0, 128, 255), 4)
	img = cv2.rectangle(img, (0, 0), (width, height), (0, 128, 255), 4)
	# ...circle(img, (coord_x, coord_y), radius, (BGR), thickness)
	img = cv2.circle(img, (75, 75), 75, (0, 0, 128), -1)
	font = cv2.FONT_HERSHEY_SIMPLEX
	# ...put_text(img, text, center_position, font, font_scale, color, line_thickness, line_type)
	img = cv2.putText(img,'OpenCV is awesome!', (20, height-20), 
		font, 1.5, (0, 128, 128), 2, cv2.LINE_AA)

	cv2.imshow('frame', img)

	if cv2.waitKey(1) == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()
