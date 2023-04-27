import os
import csv
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

# Initialize tkinter app
root = tk.Tk()
root.title("Image Renaming App")

# Define global variables
image_folder = ""
completed_renaming = []

# Define input variables
vendor_var = tk.StringVar(root)
vendor_options = ["Vendor 1", "Vendor 2", "Vendor 3", "Vendor 4"]
product_type_var = tk.StringVar(root)
product_type_options = ["Type 1", "Type 2", "Type 3", "Type 4"]
title_var = tk.StringVar(root)
option_name_var = tk.StringVar(root)
option_name_options = ["Option 1", "Option 2", "Option 3", "Option 4"]
option_value_var = tk.StringVar(root)


# Define input labels and fields
vendor_label = tk.Label(root, text="Vendor:")
vendor_dropdown = tk.OptionMenu(root, vendor_var, *vendor_options)
product_type_label = tk.Label(root, text="Product Type:")
product_type_dropdown = tk.OptionMenu(root, product_type_var, *product_type_options)
title_label = tk.Label(root, text="Title:")
title_entry = tk.Entry(root, textvariable=title_var, width=100)
option_name_label = tk.Label(root, text="Option Name:")
option_name_dropdown = tk.OptionMenu(root, option_name_var, *option_name_options)
option_value_label = tk.Label(root, text="Option Value:")
option_value_entry = tk.Entry(root, textvariable=option_value_var)

# Define listbox to display image filenames
image_listbox = tk.Listbox(root, width=50, height=20)

# Define image panel to display selected image
image_panel = tk.Label(root, width=200, height=200)

# Define buttons
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_image_button = tk.Button(root, text="Select Image", command=select_image)
rename_button = tk.Button(root, text="Rename Image", command=rename_image)
quit_button = tk.Button(root, text="Quit", command=root.quit)
create_csv_button = tk.Button(root, text="Create CSV", command=create_csv)

# Define functions
def select_folder():
    global image_folder
    image_folder = filedialog.askdirectory()
    image_files = os.listdir(image_folder)
    image_listbox.delete(0, tk.END)
    for file in image_files:
        image_listbox.insert(tk.END, file)

# Define function to rename selected image
def rename_image():
    # Get input values
    title = title_entry.get()
    vendor = vendor_var.get()
    product_type = product_type_var.get()
    option_name = option_name_var.get()
    option_value = option_value_entry.get()

    # Construct new filename
    old_name = image_paths_listbox.get(image_paths_listbox.curselection())
    new_name = f"{vendor}--{product_type}--{title}--{option_name}-{option_value}{os.path.splitext(old_name)[1]}"
    
    # Rename file and update lists
    rename_file(old_name, new_name)
    
    # Update CSV file
    with open("renamed_files.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["", title, "", vendor, product_type, "", "", "TRUE", option_name, option_value, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])


# Get selected image
selected_image = image_listbox.get(image_listbox.curselection())

# Rename file
new_file_name = f"{vendor}--{product_type}--{title}--{option_name}-{option_value}"
os.rename(os.path.join(image_folder, selected_image), os.path.join(image_folder, new_file_name))

# Remove renamed file from listbox and add to completed files list
image_listbox.delete(image_listbox.curselection())
completed_files.append(new_file_name)

# Update CSV row
row = [
    '',
    title_var.get(),
    '',
    vendor_var.get(),
    '',
    product_type_var.get(),
    '',
    'TRUE',
    option_name_var.get(),
    option_value_var.get(),
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    ''
]
image_dict = {
    'Handle': new_file_name,
    'Title': title_var.get(),
    'Body (HTML)': '',
    'Vendor': vendor_var.get(),
    'Product Category': '',
    'Type': product_type_var.get(),
    'Tags': '',
    'Published': 'TRUE',
    'Option1 Name': option_name_var.get(),
    'Option1 Value': option_value_var.get(),
    'Option2 Name': '',
    'Option2 Value': '',
    'Option3 Name': '',
    'Option3 Value': '',
    'Variant SKU': '',
    'Variant Grams': '',
    'Variant Inventory Tracker': '',
    'Variant Inventory Qty': '',
    'Variant Inventory Policy': '',
    'Variant Fulfillment Service': '',
    'Variant Price': '',
    'Variant Compare At Price': '',
    'Variant Requires Shipping': '',
    'Variant Taxable': '',
    'Variant Barcode': '',
    'Image Src': '',
    'Image Position': '',
    'Image Alt Text': '',
    'Gift Card': '',
    'SEO Title': '',
    'SEO Description': '',
    'Google Shopping / Google Product Category': '',
    'Google Shopping / Gender': '',
    'Google Shopping / Age Group': '',
    'Google Shopping / MPN': '',
    'Google Shopping / AdWords Grouping': '',
    'Google Shopping / AdWords Labels': '',
    'Google Shopping / Condition': '',
    'Google Shopping / Custom Product': '',
    'Google Shopping / Custom Label 0': '',
    'Google Shopping / Custom Label 1': '',
    'Google Shopping / Custom Label 2': '',
    'Google Shopping / Custom Label 3': '',
    'Google Shopping / Custom Label 4': '',
    'Variant Image': '',
    'Variant Weight Unit': '',
    'Variant Tax Code': '',
    'Cost per item': '',
    'Included / United Arab Emirates': '',
    'Included / International': '',
    'Price / International': '',
    'Compare At Price / International': '',
    'Status': ''
}
csv_rows.append(row)
image_dicts.append(image_dict)

# Update preview panel
update_preview()


import os
import csv
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Renaming Application")

# Define variables
title_var = tk.StringVar()
vendor_var = tk.StringVar()
product_type_var = tk.StringVar()
option_name_var = tk.StringVar()
option_value_var = tk.StringVar()

# Define dropdown options
vendor_options = ['Vendor 1', 'Vendor 2', 'Vendor 3', 'Vendor 4']
product_type_options = ['Type 1', 'Type 2', 'Type 3', 'Type 4']
option_name_options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

# Define image preview panel
preview_panel = tk.Label(root, width=200, height=200)
preview_panel.grid(row=0, column=0, rowspan=10)

# Define input labels and fields
title_label = tk.Label(root, text="Title:")
title_entry = tk.Entry(root, textvariable=title_var, width=100)
title_label.grid(row=0, column=1, padx=5, pady=5)
title_entry.grid(row=0, column=2, padx=5, pady=5)

vendor_label = tk.Label(root, text="Vendor:")
vendor_dropdown = tk.OptionMenu(root, vendor_var, *vendor_options)
vendor_label.grid(row=1, column=1, padx=5, pady=5)
vendor_dropdown.grid(row=1, column=2, padx=5, pady=5)

product_type_label = tk.Label(root, text="Product Type:")
product_type_dropdown = tk.OptionMenu(root, product_type_var, *product_type_options)
product_type_label.grid(row=2, column=1, padx=5, pady=5)
product_type_dropdown.grid(row=2, column=2, padx=5, pady=5)

option_name_label = tk.Label(root, text="Option Name:")
option_name_dropdown = tk.OptionMenu(root, option_name_var, *option_name_options)
option_name_label.grid(row=3, column=1, padx=5, pady=5)
option_name_dropdown.grid(row=3, column=2, padx=5, pady=5)

option_value_label = tk.Label(root, text="Option Value:")
option_value_entry = tk.Entry(root, textvariable=option_value_var, width=50)
option_value_label.grid(row=4, column=1, padx=5, pady=5)
option_value_entry.grid(row=4, column=2, padx=5, pady=5)

# Define listbox to display image paths
image_paths_listbox = tk.Listbox(root, width=50, height=10)
image_paths_listbox.grid(row=5, column=3, padx=5, pady=5)

# Define label for error messages
error_label = tk.Label(root, fg='red')
error_label.grid(row=6, column=3, padx=5, pady=5)

# Define button to select image folder
def select_folder():
    # Open file dialog to select folder
    global image_folder
    image_folder = filedialog.askdirectory()
    
    # Get list of image files in folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    
    # Display image file names in listbox
    image_paths_listbox.delete(0, tk.END)
    for f in image_files:
        image_paths_listbox.insert(tk.END, f)


# Run the main event loop
root.mainloop()

# Destroy the GUI window and exit the application
root.destroy()

