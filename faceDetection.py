#this module is to detect the faces in front of the camera
import cv2,time

video=cv2.VideoCapture(cv2.CAP_DSHOW)
time.sleep(10)
a=1
face_cascade=cv2.CascadeClassifier("cascade.xml") #object od cascade classifier, it stores the feature of face. 

while(True):
    a+=1
    check, frame= video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5) #to detect the region of face
    for x, y, w, h in faces: #to draw the rectangle around face
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    print(frame)
    cv2.imshow("Capturing", frame)
    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #to convert the frame into gray scale
    #cv2.imshow("Capturing",frame) 
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(a) #to print the number of frames captures by th camera
video.release()
cv2.destroyAllWindows()

