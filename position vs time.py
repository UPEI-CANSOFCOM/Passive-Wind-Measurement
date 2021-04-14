 #import library
import cv2
import matplotlib.pyplot as plt
import time
st = time.time()

cap = cv2.VideoCapture('7 kph.avi')

tracker = cv2.TrackerMIL_create() #built-in tracker
success, img = cap.read() #frame
x ,y,w,h =100, 1200, 10, 10 #preselect video
bbox = x ,y,w,h
tracker.init(img,bbox) #initialize tracker using bbox



def drawBox(img,bbox):

    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Pixel Displacement Tracking", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

while True:
    timer = cv2.getTickCount()
    success, img = cap.read() #frames

    fps = cap.get(cv2.CAP_PROP_FPS) #get fps of video


    success,bbox = tracker.update(img)
    print(bbox, "%.2f"%(time.time()-st))
    #print(fps)
    if success:
        drawBox(img,bbox)


    else:
        cv2.putText(img, "Lost", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)


    #fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7,(0,0,255),2) #display frames per second
    #cv2.putText(img, str(int(fpcount)), (100, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
    #cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_COMPLEX, 0.7,(0,0,255),2)
    #
    img2 = cv2.resize(img, (700, 800))
    cv2.imshow("Tracking", img2) #show frames
    #
    # x_values = [x,x+w]
    # y_values = [y,y+h]
    #
    #
    #
    # plt.plot(x_values,y_values)
    # plt.show()
    #print ("----%.2f----"%(time.time()-st))

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break #break/end program if q key is pressed

