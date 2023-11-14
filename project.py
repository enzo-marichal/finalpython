import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
import pandas as pd


# Function to capture screen
def capture_screen(region=None):
    screen = ImageGrab.grab(bbox=region)
    screen_np = np.array(screen)
    screen_np = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)
    return screen_np


# Function to detect faces
def detect_faces(image):
    face_cascade = cv2.CascadeClassifier('C:\Users\eliot\OneDrive\Documents\ESSEC\3A\Python for Business\project\dataset\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces


# Function to recognize text
def recognize_text(image):
    text = pytesseract.image_to_string(image)
    return text.strip()


# Main function
def take_attendance():
    # Capture the screen where the Zoom grid is displayed
    screen = capture_screen(region='region_of_zoom_grid')

    # Assume we have a way to divide the screen into a 4x4 grid and coordinates for each cell
    grid_coordinates = determine_grid_coordinates(screen)

    attendance_list = []

    for cell in grid_coordinates:
        # Extract cell image
        cell_image = screen[cell["y"]:cell["y2"], cell["x"]:cell["x2"]]

        # Detect faces in the cell
        faces = detect_faces(cell_image)

        # Check presence
        presence = "present" if len(faces) > 0 else "absent"

        # Extract the name label region based on expected location
        name_label_region = cell_image[cell["name_label_y"]:cell["name_label_y2"],
                            cell["name_label_x"]:cell["name_label_x2"]]

        # Recognize name
        name = recognize_text(name_label_region)

        # Append to list
        attendance_list.append({"name": name, "presence": presence})

    # Convert to dataframe
    df = pd.DataFrame(attendance_list)

    # Save to CSV
    df.to_csv('attendance.csv', index=False)


# Define the coordinates for the grid and name labels based on the Zoom interface layout
def determine_grid_coordinates(screen):
    # You will need to calculate these coordinates based on the size and layout of your Zoom grid
    return [
        {"x": 0, "y": 0, "x2": 100, "y2": 100, "name_label_x": 10, "name_label_y": 90, "name_label_x2": 100,
         "name_label_y2": 100},
        # ... add coordinates for each cell
    ]


# Run the program
take_attendance()
