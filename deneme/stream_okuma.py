import cv2
import requests
import numpy as np
import pickle
import base64

while True:
    istek = requests.get("http://127.0.01:5000/video_feed")
    txt = istek.text
    jpg_original = base64.b64decode(txt)
    filename = 'some_image.jpg'
    
    with open(filename, 'wb') as f:
        f.write(jpg_original)

    img = cv2.imread(filename)
    cv2.imshow("xx",img)
    cv2.waitKey(1)
    
