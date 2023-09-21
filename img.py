import tkinter as tk
from tkinter import Button, Label, PhotoImage, Scale, HORIZONTAL
from PIL import Image, ImageTk
import os

# Directory where images are saved
directory = "captured_images"

# Get list of all images in the directory
image_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
image_files.sort()  # Sort the images
current_image_index = 0

# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# Load and display the first image
image_path = os.path.join(directory, image_files[current_image_index])
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = Label(root, image=photo)
image_label.pack(pady=20)

def update_image(val):
    global photo
    current_image_index = int(val)
    image_path = os.path.join(directory, image_files[current_image_index])
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

# Add a slider to navigate through images
slider = Scale(root, from_=0, to=len(image_files)-1, orient=HORIZONTAL, command=update_image)
slider.set(current_image_index)
slider.pack(fill="x", padx=20, pady=10)

root.mainloop()
