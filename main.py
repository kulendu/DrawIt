import cv2
import  numpy as np
import imutils 
from collections import deque

# using the red color as the marker
red_lower_bound = np.array([0,100,100])
red_upper_bound = np.array([20,255,255])

# defining the color palette
color_list = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (0, 255, 255), (255, 255, 255)]
color_palette_colors = [(255,0,0), (0,0,255)]

# index for the colors in our palette
color_index = 0

trace_blue = [deque(maxlen=15000)]
trace_red = [deque(maxlen=15000)]

# indeces
index_blue = 0
index_red = 0

# reading from the webcam feed

camera = cv2.VideoCapture(0)
while True:
    (cam_rec, cam_frame) = camera.read()
    cam_frame = cv2.flip(cam_frame, 1)  # flipping the feed.
    cam_frame = cv2.resize(cam_frame, (1500, 900))  # resizing the frame.
    feed = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2HSV)   # converting the color(BGR) to HSV.



    cv2.imshow("Canvas", cam_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()