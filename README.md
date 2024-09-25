# PDF Keyword Search and Copy

This is a Python script that allows users to search for PDF files in specified directories, find a keyword within those files, and copy matching PDFs to a destination directory.

## Description

This script provides a graphical user interface (GUI) that enables users to search for PDF files across specified directories on their computer. The script searches through the text content of each PDF file for a specified keyword and copies any PDF files containing that keyword to a designated destination directory. It also handles potential naming conflicts by appending a number to the file name if a file with the same name already exists in the destination directory.

## Features

- **Search Multiple Directories**: Specify multiple directories to search for PDF files, one per line.
- **Keyword Search**: Searches the text content of each PDF file for a specified keyword.
- **Copying Files**: Copies any PDF files containing the keyword to a specified destination directory.
- **Log Output**: Logs all actions and results in the GUI, with a "Done" message displayed in green upon completion.
- **Duplicate Handling**: Avoids overwriting by appending a number to duplicate filenames.

## How to Use

1. **Install Required Libraries**: Ensure you have Python installed on your computer. Use Poetry to manage dependencies:
   ```bash
   poetry add PyPDF2
   ```
2. **Run the Script**: Use Poetry to run the script:
   ```bash
   poetry run python pdf_keyword_search.py
   ```
3. **Input the Keyword**: In the GUI, enter the keyword you want to search for in the text box labeled "Enter keyword to search".

4. **Specify Directories**: Enter the directories you want to search for PDF files in the text box labeled "Enter directories to search (one per line)". Make sure to include valid paths.

5. **Select Destination Directory**: Click the "Browse" button to select a destination directory where the matching PDF files will be copied.

6. **Start the Search**: Click the "Search and Copy" button to start the process. The script will log its progress, including which files were copied and any files that did not contain the keyword.

7. **Check the Log**: View the log output in the GUI for details about the search process, including success messages and any errors encountered.

## Building the Executable

To convert the script into an executable (.exe) file, use PyInstaller:

1. Install PyInstaller if you haven't already:
   ```bash
   poetry add --dev pyinstaller
   ```
2. Navigate to the directory containing the script and run:
   ```bash
   poetry run pyinstaller --onefile --windowed pdf_keyword_search.py
   ```

## Download the Executable

You can also download the executable version [here](/dist/) to run the program without needing Python.

## Requirements

- Python 3.x

## Summary:

- This part includes instructions on downloading the executable and lists the requirements.
- If you need any further modifications or additional sections, just let me know!
