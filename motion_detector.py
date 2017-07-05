import cv2,time

#regarded as the first static frame
first_frame=None

#capturing video through webcam
video=cv2.VideoCapture(0)

while True:
    check, frame=video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #removing noise
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue
    
    #comparing the first frame with the current frame
    delta_frame=cv2.absdiff(first_frame,gray)

    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    #finding contours
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        #creating a rectangle
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta frame",delta_frame)
    cv2.imshow("Threshold frame",thresh_frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()    
cv2.destroyAllWindows