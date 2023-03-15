from flask import Flask,render_template,request,jsonify
import time
import os
from Analyzer import Processor

inputPropcessor=Processor.InputPropcessor()
modelProcessor=Processor.ModelProcessor()
modelProcessor.setModel("../Model/DefinedModel.h5")

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

file_name=""

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getresult',methods=['POST','GET'])
def getresult():
    global file_name
    print("getresult is requested")
    if request.method=='POST':
        print("Post Method")
        if file_name!="":
            print("File Found")
            image_array=inputPropcessor.preprocessInput(os.path.dirname(__file__)+f"\\static\\images\\data\\{file_name}")
            response_value=modelProcessor.predictClass(image_array)
            print(response_value)
            return jsonify({
                "data":response_value
            })
        else:
            return "ERROR"
    else:
        return "ERROR"


@app.route('/upload',methods=['POST','GET'])
def upload():
    global file_name
    if request.method=='POST':
        print(request.files['file'])
        # print(request.files)
        
        file=request.files['file']
        file_name=file.filename
        extension=file_name.split(".")[-1]
        print(extension)
        miliseconds_value=round(time.time()*1000)
        file_name=f"{miliseconds_value}.{extension}"
        print(file_name)
        file_path=f"/static/images/data/{file_name}"
        file.filename=file_name
        print(file)
        file.save(os.path.dirname(__file__)+f"\\static\\images\\data\\{file_name}")
        return jsonify({'image_path':file_path})
    else:
        return "error"




