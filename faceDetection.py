import cv2

# Face Captures -
faceCap = cv2.CascadeClassifier("C:/Users/HP/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Video Capctures -
videoCap = cv2.VideoCapture(0)

while(True):
  ret, videoData = videoCap.read()
  if not ret:
    break
  color = cv2.cvtColor(videoData, cv2.COLOR_BGR2GRAY)



 # Detect faces -
  faces = faceCap.detectMultiScale(
    color,
    scaleFactor= 1.1,
    minNeighbors= 5,
    minSize= (30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
  )

  for (x,y,w,h) in faces :
    cv2.rectangle(videoData, (x, y), (x + w, y + h), (0, 255, 0), 2)
    

  cv2.imshow('liveVideo', videoData)
  if(cv2.waitKey(10) == ord("q")):
    break

videoCap.release()
cv2.destroyAllWindows()