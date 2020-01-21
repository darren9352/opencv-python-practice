# -*- coding: utf8 -*-
import cv2
import socket
import numpy as np
import requests
import asyncio
import multiprocessing
import time
import base64
## TCP 사용
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## server ip, port
s.connect(('localhost', 5000))
 
 
## webcam 이미지 capture
cam = cv2.VideoCapture(0)
 
## 이미지 속성 변경 3 = width, 4 = height
cam.set(3, 320)
cam.set(4, 240)
 
## 0~100에서 90의 이미지 품질로 설정 (default = 95)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
 

def get(frame):
    # url = 'https://naveropenapi.apigw.ntruss.com/vision/v1/face'
    url = 'http://localhost:3000/route'
    headers = {'X-NCP-APIGW-API-KEY-ID': 'ad7ueq9hal', 'X-NCP-APIGW-API-KEY': 'Ov83nJAvffDEYEhKPDiSt1JAEz9OBkJ9IXZhIgln'}
    files = {'image': frame}
    #print(type(frame))
    try:
        response = requests.post(url, files=files, headers=headers, timeout=0.00000001)
    except:
        pass

def process():
    while True:
        # 비디오의 한 프레임씩 읽는다.
        # 제대로 읽으면 ret = True, 실패면 ret = False, frame에는 읽은 프레임
        ret, frame = cam.read()
        # cv2. imencode(ext, img [, params])
        # encode_param의 형식으로 frame을 jpg로 이미지를 인코딩한다.
        result, frame = cv2.imencode('.jpg', frame, encode_param)
        # frame을 String 형태로 변환
        
        data = np.array(frame)
        stringData = data.tostring()


        # url = 'https://naveropenapi.apigw.ntruss.com/vision/v1/face'
        # headers = {'X-NCP-APIGW-API-KEY-ID': 'ad7ueq9hal', 'X-NCP-APIGW-API-KEY': 'Ov83nJAvffDEYEhKPDiSt1JAEz9OBkJ9IXZhIgln' }
        # files = {'image': frame}
        # response = requests.post(url, files=files, headers=headers)
        # print(response.status_code)
        # print(response.text)

        # get(frame)

        #서버에 데이터 전송
        #(str(len(stringData))).encode().ljust(16)
        s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
    
    cam.release()    

process()