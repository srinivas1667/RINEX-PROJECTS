import cv2


cap = cv2.VideoCapture('test_cat_video.mp4')

catfaces_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

while True:
    ret,image = cap.read()
    if(type(image)==type(None)):
        break
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    cf = catfaces_cascade.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in cf:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),4)

    cv2.imshow('VIDEO',image)


    if cv2.waitKey(1)==13:
        break




cv2.destroyAllWindows()    
    
