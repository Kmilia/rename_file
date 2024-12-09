# Python Script for Renaming PDF Files Based on Metadata

## Description
This script is designed to automate the renaming of PDF files in a specified directory based on their metadata. It reads metadata such as the title and author from each PDF file and uses it to create a structured and meaningful filename. This is particularly useful for organizing large collections of academic papers or articles.

## Features
- Extract Metadata: Reads metadata (e.g., title, author) from PDF files using PyPDF2 and pdftitle.
- Generate Author Name: Formats the author's name into a concise form, combining the last name and initials.
- Custom Filename Generation: Creates filenames in the format Author_LastName, I._Title.pdf.
- Handles Missing Metadata: Attempts to use the pdftitle library if the title is not available in the PDF metadata.
- Batch Processing: Recursively processes all PDF files in the specified directory and its subdirectories.
- Filename Sanitization: Ensures filenames are valid by removing problematic characters.

## Requirements
- Python version: Python 3.6 or higher
- Dependencies:
  - PyPDF2: For reading PDF metadata.
  - pdftitle: To extract the title from the PDF content if metadata is incomplete.
  - os: For file and directory manipulation.
  - string: For text processing.

## How to Use
Set the Directory Path: Update the _PATH variable to the directory containing your PDF files. Example:
```
_PATH = '/path/to/your/pdf/files'
```

Run the Script: Execute the script in your Python environment:
```
python rename_pdfs.py
```

The script will process all PDF files in the specified directory and subdirectories. Renamed files will appear in the same directory, retaining their original extension.

## Customization
File Extension: Change _EXTENSION to handle files other than .pdf.
Filename Length: Modify the new_name[0:100] slicing to adjust the maximum filename length.

## Limitations
- Encrypted Files: The script assumes an empty password for decryption; files with complex passwords won't be processed.
- Incomplete Metadata: Files without metadata or poorly formatted metadata may not yield meaningful filenames.
- Cross-Platform Compatibility: Ensure compatibility with your operating system’s filename restrictions.






