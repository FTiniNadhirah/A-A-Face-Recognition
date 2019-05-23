import cv2
import sqlite3
import numpy as np

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml'); #Classifier file 
cam=cv2.VideoCapture(0);  #To open camera 


#Function to insert and update data inside the SQLite3

def insertOrUpdate(Id , Name):                
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(Name)+" WHERE ID=" +str(Id)
    else:
        cmd="INSERT INTO People(ID,Name) Values("+str(Id)+","+str(Name)+ ")"

    conn.execute(cmd)
    conn.commit()
    conn.close()

id=raw_input('Enter ID :')
name=raw_input ('Enter Name :')
insertOrUpdate(id , name)          #Function call
sampleNum=0 ; 
while (True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       #Convert colored image to Gray 
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1 ; 
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg", gray[y:y+h,x:x+w])   #Save image detect into folder and set the extension to .jpg
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100) ; 
    cv2.imshow("Face",img);       #Title of the windows 
    cv2.waitKey(1);
    if (sampleNum>20):            #Number of sample taken 
         break
cam.release()
cv2.destroyAllWindows()
    
    
