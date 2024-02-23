import numpy as np
import cv2 
img = cv2.imread('./opencv/samples/data/aero1.jpg', 0)
img = cv2.line(img, (0,0), (255, 255), (255, 0, 0), 1)
img = cv2.arrowedLine(img, (0,255),(255,255),(255,0,0),10)
img = cv2.rectangle(img, (384,0),(510,128),(0,0,255),-1)
img = cv2.circle(img, (447, 63), 63, (0, 25, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Farhad Dubey', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

