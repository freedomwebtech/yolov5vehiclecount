import numpy as np
import torch
import cv2

#
cap=cv2.VideoCapture("tvid.mp4")

path='/usr/local/lib/python3.9/dist-packages/yolov5/yolov5s-int8.tflite'
#count=0

model = torch.hub.load('/usr/local/lib/python3.9/dist-packages/yolov5', 'custom', path,source='local')

b=model.names[2] = 'car'


size=416

count=0
counter=0


color=(0,0,255)

cy1=250
offset=6
while True:
    ret,img=cap.read()

    count += 1
    if count % 4 != 0:
        continue
    img=cv2.resize(img,(600,500))
    cv2.imshow("IMG",img)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
