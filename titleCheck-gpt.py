import os
import tkinter as tk
import shutil
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

root = ThemedTk(theme="equilux")
root.title("Image Renamer")
root.geometry("900x500")

# Define variables
image_folder = ""
output_folder_path = ""
product_type_options = ["Poster", "Canvas"]
product_type_var = tk.StringVar()
product_type_var.set(product_type_options[0])
title_var = tk.StringVar()
aspect_ratio_var = tk.StringVar()
highest_image_position_var = tk.StringVar()


# Create listbox to display image files
image_listbox = tk.Listbox(root, width=100, height=20)
image_listbox.grid(row=0, column=0, columnspan=4, padx=5, pady=1, sticky="w")

# Create label for output folder path
output_folder_path_label = tk.Label(root, text="Output Folder Path:")
output_folder_path_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

# Create label for selected image filename
selected_label = tk.Label(root, text="Selected Image:")
selected_label.grid(row=1, column=1, padx=5, pady=5, sticky="e")

# Create new Listbox widget to hold current selection
current_selection_listbox = tk.Listbox(root, height=1, width=100)
current_selection_listbox.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Create Canvas to display image
image_canvas = tk.Canvas(root, width=400, height=400)
image_canvas.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Create listbox to display output files
output_listbox = tk.Listbox(root, width=100, height=20)
output_listbox.grid(row=0, column=5, columnspan=4, padx=5, pady=1, sticky="w")

# Create entry box for highest image position
highest_image_position_entry = tk.Entry(root, width=10)
highest_image_position_entry.grid(row=1, column=5, padx=5, pady=5, sticky="w")

# Create variable to store image position
image_position_var = tk.StringVar()
image_position_var.set("1")


# Define functions
def browse_image_folder():
    global image_folder
    image_folder = filedialog.askdirectory()
    if image_folder:
        # Clear the image listbox
        image_listbox.delete(0, tk.END)
        
        # Add all files in the selected folder to the image listbox
        files = os.listdir(image_folder)
        for f in files:
            if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
                image_listbox.insert(tk.END, f)

def browse_output_folder():
    global output_folder_path
    output_folder_path = filedialog.askdirectory()
    if output_folder_path:
        output_folder_path_label.config(text=f"Output Folder: {output_folder_path}")

def update_selected_image(event):
    # Get the selected image filename from the image_listbox
    selected_image = image_listbox.get(image_listbox.curselection())

    # Update the selected image label
    selected_label.config(text=f"Selected Image: {selected_image}")

def update_current_selection(event):
    # Get selected file name
    selected_file = image_listbox.get(image_listbox.curselection())
    
    # Update current selection Listbox
    current_selection_listbox.delete(0, tk.END)
    current_selection_listbox.insert(0, selected_file)

def show_image(event):
    # Get selected file name
    selected_file = image_listbox.get(image_listbox.curselection())

    # Load and display image on canvas
    img = Image.open(os.path.join(image_folder, selected_file))
    img.thumbnail((400, 400))
    img_tk = ImageTk.PhotoImage(img)
    image_canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    image_canvas.image = img_tk

    # Update the selected image label
    updated_selected_image(event)

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
    image_positions = [int(f.split("--")[3]) for f in output_files if f.split("--")[3].isdigit()]
    if len(image_positions) == 0:
        next_image_position = 1
    else:
        next_image_position = max(image_positions) + 1

    # Update the title_entry with the next available image position
    highest_image_position_entry.delete(0, tk.END)
    highest_image_position_entry.insert(0, str(next_image_position))

    # Set the focus on the option_value_entry for easy editing
    highest_image_position_entry.focus()

def rename_file():
    # Get the selected image and output file names
    selected_file = image_listbox.get(image_listbox.curselection())
    output_file = output_listbox.get(output_listbox.curselection())

    # Extract product type, title, and aspect ratio from selected file
    parts = selected_file.split("--")
    product_type = parts[0]
    title = parts[1]
    aspect_ratio = parts[2]

    # Extract image position and file extension from output file
    parts = output_file.split("--")
    image_position = parts[3].split(".")[0]
    file_extension = os.path.splitext(selected_file)[1]

    # Generate new filename using the updated image position
    new_image_position = image_position_var.get()
    new_filename = f"{product_type}--{title}--{aspect_ratio}--{new_image_position}{file_extension}"
    new_filepath = os.path.join(output_folder_path, new_filename)

    # Check if new filename already exists in output folder
    if os.path.exists(new_filepath):
        messagebox.showerror("Error", "File with the same name already exists in output folder.")
        return

    # Copy the selected file with the new filename to output folder
    shutil.copy2(os.path.join(image_folder, selected_file), new_filepath)

    # Add new file to output listbox
    output_listbox.insert(tk.END, new_filename)

    # Remove old file from output listbox
    output_listbox.delete(output_listbox.curselection())

    # Set image position entry to next available image position
    next_image_position = int(new_image_position) + 1
    image_position_var.set(str(next_image_position))

    # Update the selected image label
    selected_label.config(text=f"Selected Image: {selected_file}")

    # Clear current selection listbox
    current_selection_listbox.delete(0, tk.END)

    # Show success message
    messagebox.showinfo("Success", "File has been successfully renamed and saved to output folder.")


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
    image_positions = [int(f.split("--")[3]) for f in output_files if len(f.split("--")) >= 4]
    if len(image_positions) == 0:
        next_image_position = 1
    else:
        next_image_position = max(image_positions) + 1

    # Update the highest_image_position_entry with the next available image position
    highest_image_position_entry.delete(0, END)
    highest_image_position_entry.insert(0, next_image_position)

    # Set the focus on the highest_image_position_entry for easy editing
    highest_image_position_entry.focus()

def rename_file_with_position():
    # Get the selected image filename from the image_listbox
    selected_file = image_listbox.get(image_listbox.curselection())

    # Get the new image position from highest_image_position_entry
    new_image_position = highest_image_position_entry.get()

    # Create the new filename with the updated image position
    new_filename = f"{os.path.splitext(selected_file)[0].split('--')[0]}--{os.path.splitext(selected_file)[0].split('--')[1]}--{os.path.splitext(selected_file)[0].split('--')[2]}--{new_image_position}{os.path.splitext(selected_file)[1]}"

    # Check if the new filename already exists in the output folder
    if new_filename in os.listdir(output_folder_path):
        messagebox.showerror("Error", "A file with this name already exists in the output folder. Please choose a different name.")
    else:
        # Rename the file and update the output listbox
        os.rename(os.path.join(image_folder, selected_file), os.path.join(output_folder_path, new_filename))
        image_listbox.delete(image_listbox.curselection())
        output_listbox.insert(tk.END, new_filename)

        # Clear the selected image label and highest_image_position_entry
        selected_label.config(text="")
        highest_image_position_entry.delete(0, tk.END)

def update_output_listbox():
    # Clear the output listbox
    output_listbox.delete(0, tk.END)

    # Get a list of all files in the output folder
    output_files = os.listdir(output_folder_path)

    # Loop through the files and add them to the output listbox
    for file in output_files:
        # Skip any files that are not images
        if not file.endswith(".jpg") and not file.endswith(".jpeg") and not file.endswith(".png"):
            continue

        # Add the file to the output listbox
        output_listbox.insert(tk.END, file)


def update_current_selection(event=None):
    # Get selected file name
    selected_file = image_listbox.get(image_listbox.curselection())
    
    # Update current selection Listbox
    current_selection_listbox.delete(0, tk.END)
    current_selection_listbox.insert(0, selected_file)


def update_selected_image(event):
    # Get the selected image filename from the image_listbox
    selected_image = image_listbox.get(image_listbox.curselection())

    # Update the selected image label
    selected_label.config(text=f"Selected Image: {selected_image}")

    # Set the focus back to the previously selected item in image_listbox
    image_listbox.activate(image_listbox.curselection())
    
    # Move the selected image to the top of the image_listbox
    index = image_listbox.curselection()
    image_listbox.delete(index)
    image_listbox.insert(0, selected_image)
    image_listbox.selection_clear(0, tk.END)
    image_listbox.selection_set(0)
    image_listbox.activate(0)


# Create buttons
add_files_button = tk.Button(root, text="Add Files", command=add_files)
add_folder_button = tk.Button(root, text="Add Folder", command=add_folder)
remove_file_button = tk.Button(root, text="Remove File", command=remove_file)
remove_all_button = tk.Button(root, text="Remove All", command=remove_all)
find_name_button = tk.Button(root, text="Find Name", command=find_name)
rename_button = tk.Button(root, text="Rename File", command=rename_file_with_position)
current_selection_button = tk.Button(root, text="Move to Current Selection", command=current_selection)
update_output_button = tk.Button(root, text="Update Output Listbox", command=update_output_listbox)
help_button = tk.Button(root, text="Help", command=help)

# Position buttons in grid
add_files_button.grid(row=3, column=0, padx=5, pady=1, sticky="w")
add_folder_button.grid(row=3, column=1, padx=5, pady=1, sticky="w")
remove_file_button.grid(row=3, column=2, padx=5, pady=1, sticky="w")
remove_all_button.grid(row=3, column=3, padx=5, pady=1, sticky="w")
find_name_button.grid(row=2, column=2, padx=5, pady=1, sticky="w")
rename_button.grid(row=2, column=3, padx=5, pady=1, sticky="w")
current_selection_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")
update_output_button.grid(row=4, column=0, padx=5, pady=1, sticky="w")
help_button.grid(row=4, column=5, padx=5, pady=1, sticky="e")





# Run the main event loop
root.mainloop()

# Destroy the GUI window and exit the application
root.destroy()
