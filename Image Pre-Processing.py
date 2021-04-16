
import numpy as np
import cv2
import matplotlib.pyplot as plt



cap = cv2.VideoCapture('Original.mp4') #Robinsons Island v6

_, first_frame = cap.read()
img1 = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
img1_rot = cv2.rotate(img1, cv2.ROTATE_90_CLOCKWISE)

##RESIZING
scale_percent = 60  # percent of original size
width1 = int(img1_rot.shape[1] * scale_percent / 100)
height1 = int(img1_rot.shape[0] * scale_percent / 100)
dim1 = (width1, height1)
Original_resized = cv2.resize(img1_rot, dim1, interpolation=cv2.INTER_AREA)
img_gray = cv2.medianBlur(Original_resized, 5)
edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
ret,mask =cv2.threshold(edges,100,255,cv2.THRESH_BINARY_INV)
image2 = cv2.bitwise_and(Original_resized, Original_resized, mask=mask)
image2 = cv2.medianBlur(image2, 3)

count =1
while True:
    _, frame = cap.read()
    blur = cv2.medianBlur(frame, 5)
    img2 = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    img2_rot = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)

    ##RESIZING
    scale_percent = 60  # percent of original size
    width2 = int(img2_rot.shape[1] * scale_percent / 100)
    height2 = int(img2_rot.shape[0] * scale_percent / 100)
    dim2 = (width2, height2)
    FocalChange_resized = cv2.resize(img2_rot, dim2, interpolation=cv2.INTER_AREA)

    img2_gray = cv2.medianBlur(FocalChange_resized, 5)
    edges2 = cv2.Laplacian(img2_gray, cv2.CV_8U, ksize=5)
    ret, mask2 = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    image3 = cv2.bitwise_and(FocalChange_resized, FocalChange_resized, mask=mask2)
    image3 = cv2.medianBlur(image3, 3)

    #difference = cv2.absdiff(first_gray, gray_frame)
    difference2 = cv2.absdiff(Original_resized,FocalChange_resized)
    #difference2 = cv2.absdiff(Original_resized, FocalChange_resized)
    cv2.imshow("difference",difference2)

    #cv2.imwrite("image"+str(count)+".jpg", difference2)
    count = count +1



    key = cv2.waitKey(35)
    if key == 27:
        break


cap.release()
