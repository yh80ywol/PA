import numpy as np
import cv2

fileName='video.mp4'  # change the file name if needed

cap = cv2.VideoCapture(fileName)          # load the video
while(cap.isOpened()):                    # play the video by reading frame by frame
    ret, frame = cap.read()
    if ret==True:
        # optional: do some image processing here 
    
        cv2.imshow('frame',frame)              # show the video
        if cv2.waitKey(25) & 0xFF == ord('q'): #Frames einstellen
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()