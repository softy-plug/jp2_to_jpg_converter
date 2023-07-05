import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Prompt user for folders
Tk().withdraw()
jp2_folder = askdirectory(title='Choose the folder with JP2 images:')
jpg_folder = askdirectory(title='Choose the folder to save converted JPG images:')

# Check if folders exist, create if they don't
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# Loop through all files in JP2 folder
for file_name in os.listdir(jp2_folder):
    if file_name.endswith('.jp2'):
        # Open JP2 image and convert to JPG
        jp2_file_path = os.path.join(jp2_folder, file_name)
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)
        jp2_image = Image.open(jp2_file_path)

        # Save JPG image with maximum quality
        jp2_image.save(jpg_file_path, 'JPEG', quality=100)

print(f"All JP2 images in {jp2_folder} converted to JPG and saved in {jpg_folder}.")

#softy_plug