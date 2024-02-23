import cv2
img = cv2.imread('./opencv/samples/data/aero1.jpg',1)
print(img)
#gna print the bit value of images
cv2.imshow('image',img)
#It gonna show the image
cv2.waitKey(5000)
#Now the image gonna wait for 50 seconds
cv2.imwrite('new.png',img)
#Now img is saved as new.png file
# cv2.destroyWindow
# #it 'll destory the ceated image window
# cv2.destoryAllWindows()
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('new1.png', img)
    cv2.destroyAllWindows()
    