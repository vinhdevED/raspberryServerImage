# from flask import Flask, request, jsonify, render_template
# import torch
# import torchvision.transforms as transforms
# from PIL import Image
#
# app = Flask(__name__)
#
# # Load pre-trained PyTorch model
# model = torch.load("fruit_model_state_dict.pth", map_location=torch.device('cpu'))
#
#
# # Define transformation to apply to incoming images
# preprocess = transforms.Compose([
#     transforms.Resize(256),
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
# ])
#
# # Function to preprocess image
# def preprocess_image(image):
#     image = preprocess(image).unsqueeze(0)
#     return image
#
# # Function to predict
# def predict(image):
#     with torch.no_grad():
#         outputs = model(image)
#         _, predicted = torch.max(outputs, 1)
#         return predicted.item()
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/predict', methods=['POST'])
# def prediction():
#     if 'file' not in request.files:
#         return jsonify({'error': 'no file provided'})
#
#     file = request.files['file']
#     if not file:
#         return jsonify({'error': 'no file provided'})
#
#     try:
#         image = Image.open(file)
#         image = preprocess_image(image)
#         prediction = predict(image)
#         return jsonify({'prediction': prediction})
#     except Exception as e:
#         return jsonify({'error': str(e)})
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
from inference import get_flower_name

import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        try:
            file = request.files['file']
            image = file.read()
            flower_name = get_flower_name(image_bytes=image)
            return render_template('result.html', flower=flower_name)
        except:
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', 5000))