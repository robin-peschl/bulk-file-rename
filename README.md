# 📁 bulk-file-rename

A lightweight Python script to rename all files in a selected folder with a consistent naming pattern and padded numbering.

## ✨ Features

- 🗂 Select any folder interactively via a GUI dialog  
- 📝 Automatically renames all files in the folder with:
  - A custom base name  
  - Sequential numbering with leading zeros for consistent file name length  
- 📦 Supports any file extension  
- 🔢 Padding adapts automatically based on the number of files and start number  

## 🛠️ How It Works

1. The user is prompted to select a directory using a GUI file dialog.  
2. All files in that directory are listed and sorted alphabetically.  
3. The user provides:
   - A base name for the new files  
   - A starting number for numbering  
4. The script calculates the padding needed based on the total number of files and starting number.  
5. Each file is renamed to follow the pattern:

```
basenameNNN.ext
```

Where:  
- `basename` is the user-defined name  
- `NNN` is a zero-padded number  
- `.ext` is the original file extension  

## 📌 Example

**Original files:**
```
apple.jpg  
banana.jpg  
carrot.jpg
```

**User input:**
- Base name: `fruit_`  
- Start number: `1`  

**Renamed files:**
```
fruit_1.jpg  
fruit_2.jpg  
fruit_3.jpg
```

## 🚀 Getting Started

### Requirements
- Python 3.x  
- `tkinter` (comes pre-installed with most Python distributions)

### Run the script

```bash
python rename_files.py
```

You will be prompted to select a folder, then provide a base name and a starting number via the terminal.

## ⚠️ Notes

- The script modifies file names in-place. Be sure to back up your files if needed.  
- Files are renamed in alphabetical order.

## 🧑‍💻 Author

Created by **Robin Peschl**  
for  
- [Fullsize Events UG (haftungsbeschränkt)](https://fullsize.events)  
- [petuja Systems UG (haftungsbeschränkt)](https://petuja.net)  
- and for **you** 💙

Contributions and suggestions welcome!

## 📄 License

This project is licensed under the **MIT License** – free to use, modify, and distribute.
