from flask import Flask, send_from_directory, jsonify
from os.path import join
from os import listdir
import win32api


app = Flask(__name__)


def getPathFromParameter(parameter):
    for i in range(len(parameter.split("_"))):
        if i == 0:
            path = parameter.split("_")[i] + "://"
        else:
            path = join(path, parameter.split("_")[i])
    return path

@app.route("/")
def index():
    return "Server Running"

@app.route("/get/<path>/<filename>")
def getFile(path, filename):
    return send_from_directory(getPathFromParameter(path), filename)

@app.route("/listdir/<path>")
def listDir(path):
    return jsonify(listdir(getPathFromParameter(path)))

@app.route("/listdrives")
def listDrives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return jsonify(drives)

app.run(debug=True)