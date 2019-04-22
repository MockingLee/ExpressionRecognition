import os
import cv2
from flask import Flask, render_template, request, url_for, send_file
from werkzeug.utils import secure_filename
import time
import keras
import numpy as np

import tensorflow as tf


app = Flask(__name__)

UPLOAD_FOLDER = 'fileDir'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


global graph
graph = tf.get_default_graph()
model = keras.models.load_model(filepath="../model_file/Model.299-0.6065.hdf5")

@app.route('/index')
def hello_world():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/getPre', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #print(request.files)
        file = request.files['file']
        print(type(file))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            new_filename = str(time.time()) + "_" + filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            #res = getPrediction(model , os.path.join(r"C:\Users\18140\Documents\GitHub\ExpressionRecognition\WebService\fileDir" , new_filename))

            face ,res_path  = getFace(UPLOAD_FOLDER + "/" + new_filename , "../haarcascade_frontalface_default.xml")
            if face.shape[0] > 0:

                #pic = cv2.imread(UPLOAD_FOLDER + "/" + new_filename)
                print(face[0].shape)
                pic = cv2.resize(face[0], (48, 48))
                # cv2.imshow("face" , pic)
                # cv2.waitKey(0)
                gray = np.array(cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY))
                X = gray
                X = X.reshape(1, 48, 48, 1)
                # print(X.shape)
                # print(model)
                with graph.as_default():
                    score = model.predict(X)
                li = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
                return li[np.argmax(score)]

    return "Wrong Request"

@app.route("/cameraPic")
def cameraPic():
    return render_template("pic.html")


def getFace(path, xml_path):
    faceCascade = cv2.CascadeClassifier(xml_path)
    image = cv2.imread(path)
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    res = []
    for (x, y, w, h) in faces:
        res.append(image[y:y + h, x:x + w])
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    res_path = "faceDetDir/" + path.split("/")[1]
    cv2.imwrite(res_path , image)
    return np.array(res) , res_path


@app.route("/faceDet", methods=['GET', 'POST'])
def getFaceDet():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            new_filename = str(time.time()) + "_" + filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            # res = getPrediction(model , os.path.join(r"C:\Users\18140\Documents\GitHub\ExpressionRecognition\WebService\fileDir" , new_filename))

            face , face_path = getFace(UPLOAD_FOLDER + "/" + new_filename, "../haarcascade_frontalface_default.xml")
            print(face.shape)
            return send_file(face_path)

            # if face.shape[0] > 0:
            #     # pic = cv2.imread(UPLOAD_FOLDER + "/" + new_filename)
            #     print(face[0].shape)
            #     pic = cv2.resize(face[0], (48, 48))
            #     # cv2.imshow("face" , pic)
            #     # cv2.waitKey(0)
            #     gray = np.array(cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY))
            #     X = gray
            #     X = X.reshape(1, 48, 48, 1)
            #     # print(X.shape)
            #     # print(model)
            #     with graph.as_default():
            #         score = model.predict(X)
            #     li = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
            #     return li[np.argmax(score)]

    return "?"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
