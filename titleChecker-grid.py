import os
import csv
import tkinter as tk
from tkinter import filedialog, ttk, Listbox, Canvas, NW, END, messagebox
from PIL import Image, ImageTk
import csv
import shutil
from PIL import Image

# Initialize tkinter app
root = tk.Tk()
root.title("Image Renaming App")

# Define global variables
image_folder = ""
completed_renaming = []
renamed_files = []


# Configure rows and columns with grid_columnconfigure and grid_rowconfigure
for i in range(10):
    root.grid_columnconfigure(i, weight=1, minsize=50)
    root.grid_rowconfigure(i, weight=1, minsize=50)

# Create widgets with grid
for i in range(10):
    for j in range(10):
        label = tk.Label(root, text=f"({i}, {j})", borderwidth=1, relief="solid")
        label.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

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

# Define input variables
product_type_var = tk.StringVar(root)
product_type_options = ["Canvas", "Acrylic", "Mugs", "T-Shirts","Wall Paper", "Poster", "NoteBook", "ArtBook"]
title_var = tk.StringVar(root)
# Create variable for image position
image_position_var = tk.IntVar(value=0)


product_type_label = tk.Label(root, text="Product Type:")
product_type_dropdown = tk.OptionMenu(root, product_type_var, *product_type_options)
product_type_label.grid(row=2, column=1, padx=5, pady=1, sticky="w")
product_type_dropdown.grid(row=3, column=1, padx=5, pady=1, sticky="w")

title_label = tk.Label(root, text="Title:")
title_entry = tk.Entry(root, textvariable=title_var, width=100)
title_label.grid(row=0, column=0, padx=5, pady=1, sticky="sw")
title_entry.grid(row=1, column=0, columnspan=4, padx=5, pady=1, sticky="w")

# Create the renamed_listbox
renamed_listbox = tk.Listbox(root, width=100)
renamed_listbox.grid(row=4, column=0,columnspan=4, padx=10, pady=10)

def create_output_folder():
    global output_folder_path
    output_folder_path = filedialog.askdirectory(title="Select output folder")
    if output_folder_path:
        os.makedirs(output_folder_path, exist_ok=True)
        tk.messagebox.showinfo("Success", f"Output folder created at {output_folder_path}")
        # Display list of image files in output_listbox
        output_files = [f for f in os.listdir(output_folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
        output_listbox.delete(0, tk.END)
        for file in output_files:
            output_listbox.insert(tk.END, file)
    else:
        tk.messagebox.showerror("Error", "No output folder selected")

# Create Output Folder button
create_output_folder_button = tk.Button(root, text="Select Output Folder", command=create_output_folder)
create_output_folder_button.grid(row=7, column=1, padx=10, pady=10)


def rename_file():
    # Get selected image filename
    selected_file = image_listbox.get(image_listbox.curselection())

    # Get image aspect ratio
    img_path = os.path.join(image_folder, selected_file)
    with Image.open(img_path) as img:
        width, height = img.size
        aspect_ratio = round(width / height, 2)

    # Create new filename with aspect ratio
    new_filename = f"{product_type_var.get()}--{title_var.get()}--{aspect_ratio}--{image_position_var.get()}{os.path.splitext(selected_file)[1]}"

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


# "Rename File" and binds it to the function 'rename_file'.
rename_button = tk.Button(root, text="Rename File", command=rename_file)
rename_button.grid(row=7, column=2, padx=5, pady=1)

# Listbox widget to display the output image files and set its width
output_listbox = tk.Listbox(root, width=70)
output_listbox.grid(row=0, column=6, padx=5, pady=1)

# Create a label to display the selected name
selected_label = tk.Label(root, text="Selected Name: ")
selected_label.grid(row=2, column=2, columnspan=5, padx=5, pady=5, sticky="w")

# Function to update the selected name label
def update_selected_name(event):
    # Get the selected name from the listbox
    selected_name = output_listbox.get(output_listbox.curselection())
    # Update the selected name label
    selected_label.config(text=f"Selected Name: {selected_name}")

# Bind the ListboxSelect event to the update_selected_name function
output_listbox.bind("<<ListboxSelect>>", update_selected_name)

# Create new Entry widget for highest image position
highest_image_position_entry = tk.Entry(root, width=50)
highest_image_position_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")


def find_name():
    # Get the selected filename from the output listbox
    selected_filename = output_listbox.get(output_listbox.curselection())

    # Split filename into its components
    parts = selected_filename.split("--")
    product_type = parts[0]
    title = parts[1]
    aspect_ratio = parts[2]

    # Find existing files with the same product type, title, and aspect ratio in output folder
    output_files = [f for f in os.listdir(output_folder_path) if f.startswith(f"{product_type}--{title}--{aspect_ratio}")]
    image_positions = [int(os.path.splitext(f.split("--")[3])[0]) for f in output_files]
    if len(image_positions) == 0:
        next_image_position = 1
    else:
        next_image_position = max(image_positions) + 1

    # Update the title_entry with the next available image position
    highest_image_position_entry.delete(0, END)
    highest_image_position_entry.insert(0, f"{product_type}--{title}--{aspect_ratio}--{next_image_position}")

    # Set the focus on the option_value_entry for easy editing
    highest_image_position_entry.focus()



find_name_button = tk.Button(root, text="Find Name", command=find_name)
find_name_button.grid(row=4, column=5, padx=5, pady=5, sticky="w")


def rename_file_with_position():
    # Get selected image filename
    selected_file = image_listbox.get(image_listbox.curselection())

    # Get the new filename with updated image position
    new_filename = f"{highest_image_position_entry.get()}{os.path.splitext(selected_file)[1]}"

    try:
        # Rename file
        os.rename(os.path.join(image_folder, selected_file), os.path.join(image_folder, new_filename))

        # Copy file to output folder with new filename
        shutil.copy(os.path.join(image_folder, new_filename), os.path.join(output_folder_path, new_filename))

        # Remove file from image_listbox
        image_listbox.delete(image_listbox.curselection())

        # Add new filename to renamed_files array
        renamed_files.append(new_filename)

        # Update renamed_listbox
        renamed_listbox.delete(0, END)
        for file in renamed_files:
            renamed_listbox.insert(END, file)

        # Update output_listbox
        output_listbox.insert(END, new_filename)

    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred while renaming the file: {e}")
        # Print error message to console for debugging
        print(f"Error occurred while renaming the file: {str(e)}")



# Button to rename selected image file with highest image position from entry box
rename_with_position_button = tk.Button(root, text="Rename File with Position", command=rename_file_with_position)
rename_with_position_button.grid(row=10, column=1, padx=10, pady=10)


# Run the main event loop
root.mainloop()

# Destroy the GUI window and exit the application
root.destroy()
