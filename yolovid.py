import numpy as np
import torch
import cv2
import time
import os
#
cap=cv2.VideoCapture("/home/pi/Downloads/vid.mp4")
#cap=cv2.VideoCapture(0)
path='/usr/local/lib/python3.9/dist-packages/yolov5/yolov5s-int8.tflite'
count=0
#model = torch.hub.load('ultralytics/yolov5','custom',path,cfg,force_reload=True)
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model = torch.hub.load('/usr/local/lib/python3.9/dist-packages/yolov5', 'custom', path,source='local')
#model.names[1] = 'NoMask'
b=model.names[2] = 'car'

size=416

count=0
counter=0

area2=[(121,244),(594,245),(593,257),(121,260)]
color=(0,0,255)

cy1=214
offset=6
os.system('rm -rf file.txt')
os.system('touch file.txt')
while True:
    ret,img=cap.read()

    count += 1
    if count % 4 != 0:
        continue
    img=cv2.resize(img,(600,500))
    results = model(img,size)
    cv2.line(img,(146,214),(590,214),(color),3)
    a=results.pandas().xyxy[0]['name'].to_list()
  
  
   
    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        d=(row['class'])
        
       
       
        if d==2:
         
           cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,255), 2)
           rect1x, rect1y = ((x1+x2)/2, (y1+y2)/2)
           rect1center = int(rect1x),int(rect1y)
           cx=rect1center[0]
           cy=rect1center[1]
           cv2.putText(img,str(b),(x1,y1),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
           cv2.circle(img,(cx,cy),1,(255,0,0),-1)
           if cy<(cy1+offset) and cy>(cy1-offset):
              cv2.line(img,(146,214),(590,214),(0,255,0),3)
              counter+=1
              print(counter)   
                
              
               
              
               
               
            
        
 
      
    cv2.imshow("IMG",img)
    
    if cv2.waitKey(1)&0xFF==27:
        break