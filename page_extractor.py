import fileinput
import PyPDF2
import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

while True:
    try:
        input_file = select_file()
        start_page = int(input("Enter the start page number: "))
        end_page = int(input("Enter the end page number: "))
    except ValueError:
        print("Error: Invalid page numbers. Please enter positive integers.")
        continue

    try:
        # Open the input pdf file
        pdf_reader = PyPDF2.PdfReader(input_file)

        # Create an output pdf file
        pdf_writer = PyPDF2.PdfWriter()

        # Extract the specified pages and add them to the output pdf file
        for page_num in range(start_page-1, end_page):
            if page_num >= len(pdf_reader.pages) or page_num < 0:
                print("Error: Page number out of range.")
                continue
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Save the output pdf file
        output_file = input("Enter the name of the output pdf file: ")
        output_dir = r"F:\CFA Level 2\Questions"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        with open(os.path.join(output_dir, output_file +".pdf"), "wb") as output:
            pdf_writer.write(output)
        print("Operation completed successfully.")
    except FileNotFoundError:
        print("Error: Input file not found.")
        continue
    except Exception as e:
        print("Error:", e)
        continue

    repeat = input("Do you want to extract more pages from this document? (yes/no) ").strip().lower()
    if repeat != "yes":
        break
# repeat the process
