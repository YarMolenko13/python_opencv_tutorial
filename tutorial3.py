# webcam capturing
import numpy as np
import cv2

capture = cv2.VideoCapture(0) # or "filename" for video

while True:
	# ret - is capture working 
	# frame - numpy array (image)
	ret, frame = capture.read()
	width = int(capture.get(3))
	height = int(capture.get(4))
	frame = np.flip(frame, axis=1) # flip vertically (0 - horizontally)

	image = np.zeros(frame.shape, np.uint8) 
	smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
	smaller_frame_fliped = np.flip(smaller_frame, axis=1)

	image[:height//2, :width//2] = smaller_frame
	image[height//2:, :width//2] = smaller_frame
	image[:height//2, width//2:] = smaller_frame_fliped
	image[height//2:, width//2:] = smaller_frame_fliped

	cv2.imshow('frame', image)

	if cv2.waitKey(1) == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()
