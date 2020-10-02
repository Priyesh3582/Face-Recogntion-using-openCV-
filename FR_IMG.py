# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:35:21 2020

@author: PRIYESH
"""

#facial recognition
import cv2
#create a CascodeClassifier Object
face_cascade=cv2.CascadeClassifier("C:/Users/priyesh/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#reading image as it is
img=cv2.imread(r"(path of the file")
#reading image as gray-scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#search the co-ordinate of image
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)
#to add rectangular facebox
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 3)
point1=[x, x+w]
point2=[y, y+h]
Re_size=cv2.resize(img, (int(img.shape[1]/5),  int(img.shape[0]/5)))
cv2.imshow("gray", Re_size)
cv2.waitKey(0)
cv2.destroyAllWindows()
