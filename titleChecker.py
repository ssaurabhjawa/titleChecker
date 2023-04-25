import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Define root window
root = tk.Tk()
root.title("Image Renamer")

# Define variables to store user input
title_var = tk.StringVar()
vendor_var = tk.StringVar()
product_type_var = tk.StringVar()
option_name_var = tk.StringVar()
option_value_var = tk.StringVar()

# Define function to handle renaming of files
def rename_files():
    # Get user input
    title = title_var.get()
    vendor = vendor_var.get()
    product_type = product_type_var.get()
    option_name = option_name_var.get()
    option_value = option_value_var.get()

    # Get list of files in current folder
    files = os.listdir()

    # Iterate through each file
    for filename in files:
        # Check if file is an image
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Construct new filename based on user input
            new_filename = f"{vendor}--{product_type}--{title}--{option_name}-{option_value}" + os.path.splitext(filename)[1]
            
            # Rename file
            os.rename(filename, new_filename)

    # Show success message
    tk.messagebox.showinfo("Success", "Files renamed successfully.")

# Define function to handle selecting an image file
def select_image():
    # Open file dialog to select image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    # Display image in left panel
    img = Image.open(file_path)
    img.thumbnail((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    image_panel.configure(image=img_tk)
    image_panel.image = img_tk

# Define function to handle clearing user input
def clear_input():
    title_var.set("")
    vendor_var.set("")
    product_type_var.set("")
    option_name_var.set("")
    option_value_var.set("")

# Define input labels and fields
title_label = tk.Label(root, text="Title:")
title_entry = tk.Entry(root, textvariable=title_var)

vendor_label = tk.Label(root, text="Vendor:")
vendor_dropdown = tk.OptionMenu(root, vendor_var, "Vendor 1", "Vendor 2", "Vendor 3")

product_type_label = tk.Label(root, text="Product Type:")
product_type_dropdown = tk.OptionMenu(root, product_type_var, "Type 1", "Type 2", "Type 3")

option_name_label = tk.Label(root, text="Option Name:")
option_name_dropdown = tk.OptionMenu(root, option_name_var, "Option 1", "Option 2", "Option 3")

option_value_label = tk.Label(root, text="Option Value:")
option_value_entry = tk.Entry(root, textvariable=option_value_var)

# Define buttons
select_image_button = tk.Button(root, text="Select Image", command=select_image)
rename_files_button = tk.Button(root, text="Rename Files", command=rename_files)
clear_input_button = tk.Button(root, text="Clear Input", command=clear_input)

# Define image panel
image_panel = tk.Label(root, width=200, height=200)

# Position input labels and fields
title_label.grid(row=0, column=0, sticky="E")
title_entry.grid(row=0, column=1)

vendor_label.grid(row=1, column=0, sticky="E")
vendor_dropdown.grid(row=1,
