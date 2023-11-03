import cv2
from PIL import Image
import numpy as np

# im = cv2.imread('my_screenshot.png')

# color = [238,123,104]

# y, x = np.where(np.all(im==color,axis=2))

# print(x,y)

pim = Image.open('my_screenshot.png').convert('RGB')
# pim = Image.open('color_test.png').convert('RGB')
im = np.array(pim)
# print(im)

color = [123,104,238]
# color = [114,97,233]

y, x = np.where(np.all(im==color, axis=2))
# print(x,y)

screen_np = np.array(pim)
lower_bound = np.array([color[0] - 10, color[1] - 10, color[2] - 10])
upper_bound = np.array([color[0] + 10, color[1] + 10, color[2] + 10])
mask = cv2.inRange(screen_np, lower_bound, upper_bound)
result = cv2.findNonZero(mask)
print(result)