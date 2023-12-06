import os
from flask import Flask, url_for, request, redirect, flash, render_template, jsonify
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './db'
app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'wav', 'ogg'}
app.secret_key = 'your-secret-key'

@app.route("/list/", methods=['GET'])
def index_list():
    if request.method == 'GET':
        response = {'files': os.listdir(app.config['UPLOAD_FOLDER'])}
    return jsonify(response)


def AllowFile(filename: str)-> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected', 'error')
            return redirect(url_for('index'))
        file = request.files['file']
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('index'))
        if file and AllowFile(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully', 'success')
            return redirect(request.url)

    files=os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)


if __name__ == '__main__':
    app.run(host='localhost', port=8888, debug=True)