import numpy as np
import tensorflow as tf
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()  # ret = 1 if the video is captured; frame is the image
    
    # Our operations on the frame come here    
    img = cv2.flip(frame,1)   # flip up(1) and down (0)

    
    # Display the resulting image
    cv2.imshow('Video Capture',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()