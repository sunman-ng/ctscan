import os

directory = "C:/Users/user/ctscan/captured29/white_fd"  # Replace with the path to your directory
#directory ="C:/Users/user/ctscan/cwhite_fd"

files = sorted(os.listdir(directory))
i = 0

for file in files:
    if file.endswith(".jpg"):  # Replace with your file extension if different
        new_name = f"raw_image_{i}.jpg"
        source = os.path.join(directory, file)
        destination = os.path.join(directory, new_name)
        os.rename(source, destination)
        i += 1
