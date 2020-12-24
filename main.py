import cv2
import  numpy as np
from collections import deque

#   using the red color as the marker
red_lower_bound = np.array([0,100,100])
red_upper_bound = np.array([20,255,255])

#   defining the color palette
color_list = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (0, 255, 255), (255, 255, 255)]
color_palette_colors = [(255,0,0), (0,0,255)]

# index for the colors in our palette
color_index = 0



