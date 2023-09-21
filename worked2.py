import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import serial
import cv2
import os
import time

# Global variables
ser = serial.Serial('COM12', 9600)  # Replace 'COM_PORT' with your Arduino's port
cap = cv2.VideoCapture(0)

# Directory to save images
directory = "captured_images"
if not os.path.exists(directory):
    os.makedirs(directory)

def check_for_signal():
    if ser.inWaiting():
        signal = ser.readline().decode('utf-8').strip()
        if signal == "CAPTURE":
            ret, frame = cap.read()
            if ret:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                filename = os.path.join(directory, f"image_{timestamp}.jpg")
                cv2.imwrite(filename, frame)
                print(f"Captured and saved image: {filename}")
                
                # Convert the captured frame to a format suitable for tkinter
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image=image)
                
                # Update the image label
                image_label.config(image=photo)
                image_label.image = photo

    # Schedule the function to run again after a short delay
    root.after(100, check_for_signal)

def start_process():
    ser.write(b'START')
    check_for_signal()

# Create the main window
root = tk.Tk()
root.title("Image Capturing Control")

# Add a button to start the process
start_button = tk.Button(root, text="Start", command=start_process)
start_button.pack(pady=20)

# Add a label to display the captured image
image_label = tk.Label(root)
image_label.pack(pady=20)

root.mainloop()
