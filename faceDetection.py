#this module is to detect the faces in front of the camera
import cv2,time

video=cv2.VideoCapture(cv2.CAP_DSHOW)
time.sleep(10)
a=1
face_cascade=cv2.CascadeClassifier("C:\\Users\\prashant\\PycharmProjects\\object detection\\venv\\cascade.xml")

while(True):
    a+=1
    check, frame= video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    print(frame)
    cv2.imshow("Capturing", frame)
    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Capturing",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()

