"""
    Author: AaronTook (https://AaronTook.github.io)
    File Last Modified: 2/10/2024
    File Name: utils.py
    Project Name: PyFileTransfer
"""

# Python Standard Library Imports.
from tkinter import *
from tkinter import filedialog
import os

def gui_get_file(initial_directory="", limit_filetypes=[]): # Open file explorer (using tkinter) to select a file
    root = Tk()
    root.withdraw()
    complete_file_path = filedialog.askopenfilename(title="File Select", initialdir = os.getcwd() + "/" + initial_directory, filetypes = limit_filetypes) # Select the file.
    root.destroy()
    file_path, file_name = os.path.split(complete_file_path) # Get the filepath and filename to return to the user.
    return complete_file_path, file_name