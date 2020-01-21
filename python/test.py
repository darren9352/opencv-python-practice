import os
import sys
import requests
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
url = "https://naveropenapi.apigw.ntruss.com/vision/v1/face" 
files = {'image': open('test.jpg', 'rb')}
headers = {'X-NCP-APIGW-API-KEY-ID': 'ad7ueq9hal', 'X-NCP-APIGW-API-KEY': 'Ov83nJAvffDEYEhKPDiSt1JAEz9OBkJ9IXZhIgln' }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)