#Import Libraries
import cv2
import sqlite3
import numpy as np   

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainningData.yml")
id=0

def getProfile(id):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str (id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
        
    conn.close()
    return profile


font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
while (True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h , x:x+w])
        profile=getProfile(id)

        if (profile!=None):
           cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y+h+30),font,250);
           cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[2]),(x,y+h+60),font,250);
           cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[3]),(x,y+h+90),font,250);
           cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[4]),(x,y+h+120),font,250);
        
    cv2.imshow("Face",img);
    if (cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
    
    
