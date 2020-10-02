# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:35:21 2020

@author: PRIYESH
"""

import cv2,time
#to trigger camera
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

a=1
while True:
    a=a+1
    check,frame=video.read()
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("capturing",gray)
    key=cv2.waitKey(1)
    if key== ord("q"):
        break

print(a)

#reading and checking the camera
'''check,frame=video.read()
print(check)
print(frame)
#webcam ON duration
time.sleep(3)
#captures first image/frame of the video
cv2.imshow("capture", frame)
cv2.waitKey(0)'''
#releasing the camera
video.release()
cv2.destroyAllWindows()