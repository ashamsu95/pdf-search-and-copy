import os
import shutil
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def find_pdfs(start_dirs):
    pdf_files = []
    for start_dir in start_dirs:
        if os.path.exists(start_dir):
            for root, dirs, files in os.walk(start_dir):
                for file in files:
                    if file.lower().endswith('.pdf'):
                        pdf_files.append(os.path.join(root, file))
    return pdf_files

def search_keyword_in_pdf(pdf_path, keyword):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                if text and keyword.lower() in text.lower():
                    return True
    except Exception as e:
        log_message(f"Could not read {pdf_path}: {e}")
    return False

def copy_pdfs_with_keyword(pdf_files, keyword, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    copied_files = []
    for pdf in pdf_files:
        if search_keyword_in_pdf(pdf, keyword):
            base_name = os.path.basename(pdf)
            destination_path = os.path.join(destination_dir, base_name)
            counter = 1
            
            # Check for existing files and modify the name if necessary
            while os.path.exists(destination_path):
                name, ext = os.path.splitext(base_name)
                destination_path = os.path.join(destination_dir, f"{name}_{counter}{ext}")
                counter += 1
            
            shutil.copy(pdf, destination_path)
            copied_files.append(pdf)
            log_message(f"Copied: {pdf} to {destination_path}")
        else:
            log_message(f"Keyword '{keyword}' not found in: {pdf}")
    return copied_files

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        dest_dir_var.set(directory)

def log_message(message, color=None):
    log_text.configure(state=tk.NORMAL)  # Allow editing the log text box
    if color:
        log_text.insert(tk.END, message + '\n', color)  # Append message with color
    else:
        log_text.insert(tk.END, message + '\n')  # Append message without color
    log_text.see(tk.END)  # Scroll to the end
    log_text.configure(state=tk.DISABLED)  # Make it read-only again

def search_and_copy():
    keyword = keyword_entry.get().strip()
    directories = dir_entry.get("1.0", tk.END).strip().splitlines()
    destination_dir = dest_dir_var.get().strip()
    
    log_message("")  # Clear the log before new search

    if not keyword or not destination_dir or not directories:
        log_message("Input Error: Please enter a keyword, select a destination directory, and provide directories to search.")
        return
    
    pdf_files = []
    for directory in directories:
        pdf_files.extend(find_pdfs([directory]))
    
    if pdf_files:
        log_message(f"Found {len(pdf_files)} PDF files. Searching for keyword '{keyword}'...")
        copied_files = copy_pdfs_with_keyword(pdf_files, keyword, destination_dir)
        
        if copied_files:
            log_message(f"Success: Keyword '{keyword}' found in {len(copied_files)} PDF files and copied to:\n{destination_dir}")
        else:
            log_message(f"Result: Keyword '{keyword}' not found in any PDF files.")
    else:
        log_message("Result: No PDF files found in the specified directories.")

    # Log "Done" message in green
    log_message("Done.", color='green')

# GUI Setup
root = tk.Tk()
root.title("PDF Keyword Search and Copy")

# Configure text tags for colored output
log_text = tk.Text(root, height=10, width=80, state=tk.DISABLED)
log_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
log_text.tag_configure('green', foreground='green')  # Define a green tag for logging

tk.Label(root, text="Enter keyword to search:").grid(row=0, column=0, padx=10, pady=10)
keyword_entry = tk.Entry(root, width=50)
keyword_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter directories to search (one per line):").grid(row=1, column=0, padx=10, pady=10)
dir_entry = tk.Text(root, height=5, width=50)
dir_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Select destination directory:").grid(row=2, column=0, padx=10, pady=10)
dest_dir_var = tk.StringVar()
dest_dir_entry = tk.Entry(root, textvariable=dest_dir_var, width=50)
dest_dir_entry.grid(row=2, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=2, column=2, padx=10, pady=10)

search_button = tk.Button(root, text="Search and Copy", command=search_and_copy)
search_button.grid(row=3, column=1, pady=20)

root.mainloop()
