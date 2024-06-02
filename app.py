

from flask import Flask, render_template, request, redirect

import os
from commons import pred
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return render_template('index.html', image_url=file_path)
    return redirect('/')


@app.route('/predict', methods=['POST'])
def predict_file():
    image_url = request.form['image_url']

    label, confidence = pred(image_url)
    return render_template('result.html', image_url=image_url, label=label, confidence=confidence)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
