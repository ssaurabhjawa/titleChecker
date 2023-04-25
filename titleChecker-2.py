import os
import csv
import tkinter as tk
from tkinter import filedialog, ttk, Listbox, Canvas, NW, END
from PIL import Image, ImageTk
import csv


# Initialize tkinter app
root = tk.Tk()
root.title("Image Renaming App")

# Define global variables
image_folder = ""
completed_renaming = []
renamed_files = []






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



# Create the renamed_listbox
renamed_listbox = tk.Listbox(root, width=50)
renamed_listbox.pack(side=tk.BOTTOM, padx=10, pady=10)

def rename_file():
    # Get selected image filename
    selected_file = image_listbox.get(image_listbox.curselection())

    # Create new filename
    new_filename = f"{vendor_var.get()}--{product_type_var.get()}--{title_var.get()}--{option_name_var.get()}-{option_value_var.get()}"
    
    # Rename file
    os.rename(os.path.join(image_folder, selected_file), os.path.join(image_folder, new_filename))

    # Update image_listbox
    image_listbox.delete(image_listbox.curselection())

    # Add new filename to renamed_files array
    renamed_files.append(new_filename)

    # Update renamed_listbox
    renamed_listbox.delete(0, END)
    for file in renamed_files:
        renamed_listbox.insert(END, file)

rename_button = tk.Button(root, text="Rename File", command=rename_file)
rename_button.pack()


import csv
import tkinter as tk
from tkinter import filedialog

def create_csv():
    # Prompt user for save location
    file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files', '*.csv')])

    # Define fields for CSV file
    fieldnames = [
        'Handle',
        'Title',
        'Body (HTML)',
        'Vendor',
        'Product Category',
        'Type',
        'Tags',
        'Published',
        'Option1 Name',
        'Option1 Value',
        'Option2 Name',
        'Option2 Value',
        'Option3 Name',
        'Option3 Value',
        'Variant SKU',
        'Variant Grams',
        'Variant Inventory Tracker',
        'Variant Inventory Qty',
        'Variant Inventory Policy',
        'Variant Fulfillment Service',
        'Variant Price',
        'Variant Compare At Price',
        'Variant Requires Shipping',
        'Variant Taxable',
        'Variant Barcode',
        'Image Src',
        'Image Position',
        'Image Alt Text',
        'Gift Card',
        'SEO Title',
        'SEO Description',
        'Google Shopping / Google Product Category',
        'Google Shopping / Gender',
        'Google Shopping / Age Group',
        'Google Shopping / MPN',
        'Google Shopping / AdWords Grouping',
        'Google Shopping / AdWords Labels',
        'Google Shopping / Condition',
        'Google Shopping / Custom Product',
        'Google Shopping / Custom Label 0',
        'Google Shopping / Custom Label 1',
        'Google Shopping / Custom Label 2',
        'Google Shopping / Custom Label 3',
        'Google Shopping / Custom Label 4',
        'Variant Image',
        'Variant Weight Unit',
        'Variant Tax Code',
        'Cost per item',
        'Included / United Arab Emirates',
        'Included / International',
        'Price / International',
        'Compare At Price / International',
        'Status'
    ]

    # Create CSV file and write header row
    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Write data from renamed files to CSV file
        for file_name in renamed_files:
            # Split file name into data fields using '--' delimiter
            data = file_name.split('--')

            # Write data fields to CSV file
            writer.writerow({
                'Handle': data[0],
                'Title': data[2],
                'Vendor': data[0],
                'Product Category': '',
                'Type': data[1],
                'Option1 Name': data[3],
                'Option1 Value': data[4],
                'Image Src': '',
                'Image Position': '',
                'Image Alt Text': '',
            })

    # Notify user that file was created
    tk.messagebox.showinfo('CSV Created', 'CSV file created successfully.')


create_csv_button = tk.Button(root, text='Create CSV', command=create_csv)
create_csv_button.pack(side=tk.LEFT, padx=10, pady=10)




























# Run the main event loop
root.mainloop()

# Destroy the GUI window and exit the application
root.destroy()
