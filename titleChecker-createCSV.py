import os
import csv
import tkinter as tk
from tkinter import filedialog, ttk, Listbox, Canvas, NW, END, messagebox
from PIL import Image, ImageTk
import csv
import shutil


# Initialize tkinter app
root = tk.Tk()
root.title("Image Renaming App")

# Define global variables
image_folder = ""
completed_renaming = []
renamed_files = []


# # Configure rows and columns with grid_columnconfigure and grid_rowconfigure
# for i in range(5):
#     root.grid_columnconfigure(i, weight=1, minsize=50)
#     root.grid_rowconfigure(i, weight=1, minsize=50)

# # Create widgets with grid
# for i in range(5):
#     for j in range(5):
#         label = tk.Label(root, text=f"({i}, {j})", borderwidth=1, relief="solid")
#         label.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")


def select_folder():
    global image_folder, image_files
    image_folder = filedialog.askdirectory()
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    # Display list of image files in listbox
    for image in image_files:
        image_listbox.insert(tk.END, image)


count_label = tk.Label(root, text="")
count_label.grid(row=0, column=0, padx=5, pady=10, sticky="sw") 


# Create button to select folder
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.grid(row=7, column=0, padx=5, pady=5)


# Create listbox to display image files
image_listbox = tk.Listbox(root,width=100)
image_listbox.grid(row=0, column=0,columnspan=4, padx=5, pady=1, sticky="w")

# Create Canvas to display image
image_canvas = tk.Canvas(root, width=400, height=400)
image_canvas.grid(row=0, column=5, padx=5, pady=1, sticky="w")

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

# Create the renamed_listbox
renamed_listbox = tk.Listbox(root, width=100)
renamed_listbox.grid(row=4, column=0,columnspan=4, padx=10, pady=10)

from PIL import Image

def rename_file():
    # Get selected image filename
    selected_file = image_listbox.get(image_listbox.curselection())

    # Get image aspect ratio
    img_path = os.path.join(image_folder, selected_file)
    with Image.open(img_path) as img:
        width, height = img.size
        aspect_ratio = round(width / height, 2)

    # Create new filename with aspect ratio
    new_filename = f"{product_type_var.get()}--{title_var.get()}--{aspect_ratio}--0--{os.path.splitext(selected_file)[1]}"

    try:
        # Rename file
        os.rename(os.path.join(image_folder, selected_file), os.path.join(image_folder, new_filename))

        # Copy file to output folder with new filename
        shutil.copy(os.path.join(image_folder, new_filename), os.path.join(output_folder_path, new_filename))

        # Update image_listbox
        image_listbox.delete(image_listbox.curselection())

        # Add new filename to renamed_files array
        renamed_files.append(new_filename)

        # Update renamed_listbox
        renamed_listbox.delete(0, END)
        for file in renamed_files:
            renamed_listbox.insert(END, file)

    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred while renaming the file: {e}")
        # Print error message to console for debugging
        print(f"Error occurred while renaming the file: {str(e)}")


# "Rename File" and binds it to the function 'rename_raw_file'.
rename_button = tk.Button(root, text="Rename File", command=rename_file)
rename_button.grid(row=7, column=2, padx=5, pady=1)









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




# Create CSV button
create_csv_button = tk.Button(root, text='Create CSV', command=create_csv)
create_csv_button.grid(row=7, column=3, padx=10, pady=10)



def create_output_folder():
    global output_folder_path
    output_folder_path = filedialog.askdirectory(title="Select output folder")
    if output_folder_path:
        os.makedirs(output_folder_path, exist_ok=True)
        tk.messagebox.showinfo("Success", f"Output folder created at {output_folder_path}")
    else:
        tk.messagebox.showerror("Error", "No output folder selected")

# Create Output Folder button
create_output_folder_button = tk.Button(root, text="Create Output Folder", command=create_output_folder)
create_output_folder_button.grid(row=7, column=1, padx=10, pady=10)















# Run the main event loop
root.mainloop()

# Destroy the GUI window and exit the application
root.destroy()
