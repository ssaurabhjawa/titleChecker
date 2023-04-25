import os
import csv
import tkinter as tk
from tkinter import filedialog, ttk, Listbox, Canvas, NW
from PIL import Image, ImageTk

# Initialize tkinter app
root = tk.Tk()
root.title("Image Renaming App")

# Define global variables
image_folder = ""
completed_renaming = []





def select_folder():
    global image_folder, image_files
    image_folder = filedialog.askdirectory()
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    # Display list of image files in listbox
    for image in image_files:
        image_listbox.insert(tk.END, image)

# Create button to select folder
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack(side="right", padx=5, pady=5, anchor="ne")

# Create listbox to display image files
image_listbox = tk.Listbox(root,width=70)
image_listbox.pack(side="right", padx=5, pady=5, anchor="ne")

# Create Canvas to display image
image_canvas = tk.Canvas(root, width=400, height=400)
image_canvas.pack(side="right", padx=5, pady=5, anchor="ne")

# Function to display selected image
def show_image(event):
    # Get selected file name
    selected_file = image_listbox.get(image_listbox.curselection())

    # Load and display image on canvas
    img = Image.open(os.path.join(image_folder, selected_file))
    img.thumbnail((400, 400))
    img_tk = ImageTk.PhotoImage(img)
    image_canvas.create_image(0, 0, anchor=NW, image=img_tk)
    image_canvas.image = img_tk

# Bind Listbox selection event to show_image function
image_listbox.bind('<<ListboxSelect>>', show_image)

# Define input variables
vendor_var = tk.StringVar(root)
vendor_options = ["Vendor 1", "Vendor 2", "Vendor 3", "Vendor 4"]
product_type_var = tk.StringVar(root)
product_type_options = ["Type 1", "Type 2", "Type 3", "Type 4"]
title_var = tk.StringVar(root)
option_name_var = tk.StringVar(root)
option_name_options = ["Option 1", "Option 2", "Option 3", "Option 4"]
option_value_var = tk.StringVar(root)


vendor_label = tk.Label(root, text="Vendor:")
vendor_dropdown = tk.OptionMenu(root, vendor_var, *vendor_options)
vendor_label.pack(side="top", padx=5, pady=5, anchor="nw")
vendor_dropdown.pack(side="top", padx=5, pady=5, anchor="nw")

product_type_label = tk.Label(root, text="Product Type:")
product_type_dropdown = tk.OptionMenu(root, product_type_var, *product_type_options)
product_type_label.pack(side="top", padx=5, pady=5, anchor="nw")
product_type_dropdown.pack(side="top", padx=5, pady=5, anchor="nw")

title_label = tk.Label(root, text="Title:")
title_entry = tk.Entry(root, textvariable=title_var, width=100)
title_label.pack(side="top", padx=5, pady=5, anchor="nw")
title_entry.pack(side="top", padx=5, pady=5, anchor="nw")

option_name_label = tk.Label(root, text="Option Name:")
option_name_dropdown = tk.OptionMenu(root, option_name_var, *option_name_options)
option_name_label.pack(side="top", padx=5, pady=5, anchor="nw")
option_name_dropdown.pack(side="top", padx=5, pady=5, anchor="nw")

option_value_label = tk.Label(root, text="Option Value:")
option_value_entry = tk.Entry(root, textvariable=option_value_var)
option_value_label.pack(side="top", padx=5, pady=5, anchor="nw")
option_value_entry.pack(side="top", padx=5, pady=5, anchor="nw")



































# Run the main event loop
root.mainloop()

# Destroy the GUI window and exit the application
root.destroy()
