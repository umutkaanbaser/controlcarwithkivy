from flask import Flask, render_template, Response
import cv2
import base64
import pickle

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    ret,frame = camera.read()
    ret, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
