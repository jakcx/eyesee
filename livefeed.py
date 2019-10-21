import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorMOG2()

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    fgmask = fgbg.apply(frame)
    # Display the resulting frame
    cv.imshow('frame',fgmask)
    if cv.waitKey(1) == ord('q'):
        break