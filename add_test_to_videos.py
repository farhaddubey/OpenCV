import cv2
# cap = cv2.VideoCapture(0)
# used to fetch from device camera
cap = cv2.VideoCapture('./opencv/samples/data/Megamind.avi')
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 3 is for Width and 4 is for height
# set takes height & weight arguments 
cap.set(3, 4)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
            break

cap.release()
cv2.destroyAllWindows()