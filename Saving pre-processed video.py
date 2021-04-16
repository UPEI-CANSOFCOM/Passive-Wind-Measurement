import cv2
import numpy as np
cap = cv2.VideoCapture('7 kph.MOV')
_, first_frame = cap.read()


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('your_video.avi', fourcc, 20.0, size)


while True:
    _, frame = cap.read()
    difference = cv2.absdiff(first_frame, frame)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    ret, gray = cv2.threshold(gray ,60, 250, 0) #127,255,0
    gray2 = gray.copy()
    mask = np.zeros(gray.shape, np.uint8)
    complete = cv2.bitwise_and(gray2, gray2, mask)



    out.write(difference) #saving difference (subtraction of consecutive frames from initial frame)


    key = cv2.waitKey(35)
    if key == 27:
        break


cap.release()
out.release()