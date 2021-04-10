import tkinter as tk
from tkinter import filedialog
import os

# File that u want to copy
FILE_EXAMPLE = "file_example"
# File extension
FILE_EXAMPLE_EXT = "txt"
FULL_EXAMPLE_FILE = FILE_EXAMPLE + "." + FILE_EXAMPLE_EXT
ASCII_ART_HEADER = '''
 ----------------------------------------
< Choose the directory to save the file! >
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\ ______)\/
                ||    w||
                ||     ||
'''


def main():
    os.system("color 5")
    print(ASCII_ART_HEADER)
    root = tk.Tk()
    root.withdraw()

    FILE_PATH = filedialog.askdirectory()
    if (not FILE_PATH):
        print("\n Directory not choosed")
        return
    FILE_PYTHON_PATH = os.path.dirname(__file__)
    os.system("dir")
    os.system(
        f'copy "{FILE_PYTHON_PATH}\\{FULL_EXAMPLE_FILE}" "{FILE_PATH}"\\')


main()
