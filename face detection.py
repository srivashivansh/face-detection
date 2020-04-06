import cv2

#create a cascadeclasifier object
face_cascade = cv2.CascadeClassifier(r"F:\softwares\openCV\opencv\build\etc\haarcascades\haarcascade_frontalface_default.xml")

#Reading the image as it is
img = cv2.imread(r"C:\Users\Shivansh\Desktop\x1y1.jpg")

#Reading the image as grayscale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search the coordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

cv2.imshow("Gray", img)


cv2.waitKey(0)

cv2.destroyAllWindows()
