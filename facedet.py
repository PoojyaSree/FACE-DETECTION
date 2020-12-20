import cv2

imagePath=r'C:\Users\user\Desktop\CV\faces.jpg'
cascadeClassifierPath='C:/Program Files/opencv-4.5.0/data/haarcascades/haarcascade_frontalface_alt.xml'

cascadeClassifier=cv2.CascadeClassifier(cascadeClassifierPath)
image=cv2.imread(r'C:\Users\user\Desktop\CV\faces.jpg')
grayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

detectedFaces=cascadeClassifier.detectMultiScale(grayImage)

for(x,y, width, height) in detectedFaces:
    cv2.rectangle(image, (x,y), (x+width,y+height), (255,0,0), 3)
cv2.imwrite('result.jpg',image)
