#!/usr/bin/bash/python3
import cv2 as cv

cascade = cv.CascadeClassifier('cascade/cascade.xml')

cap = cv.VideoCapture('videos/poresp.mp4')
if not cap.isOpened:
    print("Error opening video")

def detect(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    
    detected = cascade.detectMultiScale(frame)
    for(x,y,w,h) in detected:
        frame = cv.rectangle(frame, (x, y), (x+h, y+w), (0, 255, 0), 2)



while True:
    ret, frame = cap.read()
    if frame is None:
        break
    detect(frame)
    cv.imshow('Video', frame)
    
    if cv.waitKey(10) == 27:
        break

cap.release()
cv.destroyAllWindows()
