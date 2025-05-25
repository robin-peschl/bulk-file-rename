import os
from tkinter.filedialog import askdirectory

# Let user select a directory
renamePath = askdirectory(title='Select directory')
print(renamePath)

# Get and sort list of files in the selected directory
filesInPath = sorted(os.listdir(renamePath))
print(f"{len(filesInPath)} files found.")

# Ask user for the base name of the files
print("Type the name of the files")
rename_string = input()

# Ask user for the starting number
print("Type the starting number")
fileNumberCounter = int(input())

# Calculate padding based on total number of files and starting number
total_files = len(filesInPath)
padding = len(str(total_files + fileNumberCounter - 1))  # Ensures consistent width

# Rename files with leading zeros
for filename in filesInPath:
    fileName, fileExtension = os.path.splitext(filename)
    padded_number = str(fileNumberCounter).zfill(padding)
    new_name = f"{rename_string}{padded_number}{fileExtension}"

    os.rename(
        os.path.join(renamePath, filename),
        os.path.join(renamePath, new_name)
    )

    fileNumberCounter += 1
