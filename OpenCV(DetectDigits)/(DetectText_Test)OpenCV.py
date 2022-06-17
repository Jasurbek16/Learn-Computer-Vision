# Import the necessary packages
from turtle import width
import numpy as np
import cv2
import pickle

# Defining variables
width = 640
height = 480
threshold = 0.7 # depends on the epochs

# defining a function to pre-process an image
def pre_processing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img) # distribute the lightness of the image evenly
    img = img/255 # better for training processes
    return img

# Using the webcam object to capture
cap = cv2.VideoCapture(1)
# settign the width and height of the video by using id numbers
cap.set(3, width)
cap.set(4, height)

# Getting our trained model
pickle_in = open("trained_model.p", "rb")
model = pickle.load(pickle_in)

# Gtting images from the webcam
while True:
    success, original_image = cap.read()
    # converting the image to a numpy array of similar dimensions
    image = np.asarray(original_image)
    # Resize the image to a smaller size
    image = cv2.resize(image, (32, 32))
    image = pre_processing(image)
    cv2.imshow("Pre-processed image", image)
    image = image.reshape(1, 32, 32, 1)
    # Predicting the image's class_index
    class_index = model.predict_classes(image)
    # Getting the probabilities of the predictions in terms of all classe indcies
    predictions = model.predict(image)
    # Getting the highest probability of the prediction
    probabilty_value = np.amax(predictions)
    print("Index: " + '[' + class_index + ']' + '  ' + "Probability: " + '{' + probabilty_value + '}')

    # Neglect the values if the probability is low (a situation where webcam is not directed to a digit)
    if probabilty_value > threshold: 
       cv2.putText(
                   original_image, 
                   "Index: " + str(class_index) + '  ' + "Probabulity: " +  str(probabilty_value), 
                   (50, 50), 
                   cv2.FONT_HERSHEY_COMPLEX, 
                   1, 
                   (0, 0, 255), 
                   1
                  )
    # Show the real time image with other details included
    cv2.imshow("Detect Digit", original_image)
    # A condition to stop reading the image from the webcam
    if cv2.waitKey(1) & 0xFF == ord('q'): # if the user presses q, the program will stop
        break



# Learned from the YouTube channel: Murtaza's Workshop
# Text Detection using Neural Networks | OPENCV Python