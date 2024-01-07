from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move
import logging

source_dir = "/Users/kadenchien/Downloads"
music_dir = "/Users/kadenchien/Downloads/Music"
image_dir = "/Users/kadenchien/Downloads/Images"
pres_dir = "/Users/kadenchien/Downloads/Presentations"
doc_dir = "/Users/kadenchien/Downloads/Documents"
sheet_dir = "/Users/kadenchien/Downloads/Spreadsheets"


music_types = [".mp3", ".wav", ".m4a"]
image_types = [".jpg", ".jpeg", ".png", ".jif", ".jfif", ".webp"]
pres_types = [".pptx", "ppt", ".pptm"]
doc_types = [".pdf", ".docx", ".doc"]
sheet_types = [".xls", ".csx", ".xlsx"]

class main:
    def clean(self, event):
        for file in os.listdir(source_dir):
            temp = file
            extension = 'none'
            try:
                extension = splitext(source_dir+'/'+file)[1]
            except Exception:
                extension = 'none'
            