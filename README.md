# bulk-file-rename

A lightweight Python script to rename all files in a selected folder with a consistent naming pattern and padded numbering.

## Features

- 🗂 Select any folder interactively via a GUI dialog
- 📝 Automatically renames all files in the folder with:
  - A custom base name
  - Sequential numbering with leading zeros for consistent file name length
- 📦 Supports any file extension
- 🔢 Padding adapts automatically based on the number of files and start number

## How It Works

1. The user is prompted to select a directory using a file dialog.
2. All files in that directory are listed and sorted.
3. The user provides a base name and starting number for renaming.
4. The script calculates the required number padding.
5. Each file is renamed to match the pattern: `basenameNNN.ext`, where `NNN` is the zero-padded number.

## Example

If you have the following files:

