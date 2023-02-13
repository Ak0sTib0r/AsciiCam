import cv2
import math
import numpy as np

vid = cv2.VideoCapture(0)

density = 'N@#W$9876543210?!abc;:+=-,._                                                                               '

arrayLength = len(density)

font = cv2.FONT_HERSHEY_PLAIN

def CalculateBrightness(x, y):
	red = frame[x,y,2]
	green = frame[x,y,1]
	blue = frame[x,y,0]

	alpha = math.floor((red + green + blue)/3)

	return alpha

imageSize = 400
pixelNumber = 40

imgpix = math.floor(imageSize/pixelNumber)

scale = pixelNumber/40

while True:
	ret, frame = vid.read()
	frame = cv2.resize(frame, (imageSize, imageSize))

	asciiWin = np.zeros((imageSize, imageSize, 3), dtype = "uint8")

	# Get input size
	height, width = frame.shape[:2]

	# Desired "pixelated" size
	w, h = (pixelNumber, pixelNumber)

	# Resize input to "pixelated" size
	temp = cv2.resize(frame, (w, h), interpolation = cv2.INTER_LINEAR)

	# Initialize output image
	frame = cv2.resize(temp, (width, height), interpolation = cv2.INTER_NEAREST)

	for i in range(0, frame.shape[0]):
		
		if i % imgpix == 0:
			for j in range(0, frame.shape[1]):

				if j % imgpix == 0:
					brightness = CalculateBrightness(i, j)

					index = math.floor(((arrayLength/255) * brightness))

					cv2.putText(img = asciiWin, text = density[index + 1], org = (j,i), fontFace = font, fontScale = scale, color = (255, 255, 255), thickness = 1, lineType = cv2.LINE_4)

	#cv2.putText(img = frame, text = "Hello", org = (15,30), fontFace = font, fontScale = 1, color = (0, 0, 0), thickness = 1, lineType = cv2.LINE_4)

	cv2.imshow('frame', frame)
	cv2.imshow('Ascii', asciiWin)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()