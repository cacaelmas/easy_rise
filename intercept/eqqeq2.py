import cv2
import os
from tensorflow.keras.models import load_model
import numpy as np

# Load the trained model
model = load_model('mnist_cnn_model.h5')

# Function to preprocess images
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = 255 - img
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

# Folder containing the images
folder_path = 'C:\\Users\\pFFed\\PycharmProjects\\easyko\\intercept\\Interception\\imgs'  # Replace with your folder path

# Predict and print the digit for each image in the folder
for image_name in os.listdir(folder_path):
    image_path = os.path.join(folder_path, image_name)
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    predicted_digit = np.argmax(prediction)
    print(f"Predicted Digit for {image_name}: {predicted_digit}")


