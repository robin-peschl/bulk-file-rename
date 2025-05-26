import os
from tkinter.filedialog import askdirectory

while True:
    # wait for user input or exit command
    user_input = input("Press Enter to select a directory or type EXIT/STOP/E to quit: ").strip().upper()
    if user_input in ("EXIT", "STOP", "E"):
        print("Exiting...")
        break

    # open directory selection dialog
    renamePath = askdirectory(title='Select directory')
    if not renamePath:
        print("No directory selected. Try again.\n")
        continue

    # get and sort files in directory
    filesInPath = sorted(os.listdir(renamePath))
    if not filesInPath:
        print("No files in selected directory. Try again.\n")
        continue

    print(f"{len(filesInPath)} files found in:\n{renamePath}")

    # get base name
    rename_string = input("Enter base name: ")

    # get starting number
    while True:
        try:
            fileNumberCounter = int(input("Enter starting number: "))
            break
        except ValueError:
            print("Invalid number. Try again.")

    # calculate number padding
    total_files = len(filesInPath)
    padding = len(str(total_files + fileNumberCounter - 1))

    # rename files
    for filename in filesInPath:
        fileName, fileExtension = os.path.splitext(filename)
        padded_number = str(fileNumberCounter).zfill(padding)
        new_name = f"{rename_string}{padded_number}{fileExtension}"

        os.rename(
            os.path.join(renamePath, filename),
            os.path.join(renamePath, new_name)
        )

        fileNumberCounter += 1

    print("Files renamed successfully.\n")