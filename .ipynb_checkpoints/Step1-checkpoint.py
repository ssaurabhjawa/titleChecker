import cloudinary
import cloudinary.uploader
import cloudinary.api
import tkinter as tk
from tkinter import filedialog
import os

# configure Cloudinary with your account credentials
cloudinary.config(
  cloud_name = "djqvqmqe2",
  api_key = "215651395579232",
  api_secret = "gAA9lxku5Idr4AZNOTaLHnROghk"
)

# create a tkinter window to select the images
root = tk.Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames()

# create an empty array to store the uploaded image URLs
uploaded_urls = []

# iterate through each image path and upload to Cloudinary with the original filename
for path in file_paths:
  filename = os.path.basename(path)
  response = cloudinary.uploader.upload(path, public_id=filename)
  # append the uploaded image URL to the array
  uploaded_urls.append(response["secure_url"])

# print the array of uploaded image URLs
print(uploaded_urls)



