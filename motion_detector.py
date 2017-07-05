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



    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta frame",delta_frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()    
cv2.destroyAllWindows