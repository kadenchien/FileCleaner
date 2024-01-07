import os
from os.path import splitext
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class main:
    def clean(self, event):
        for file in os.listdir(source_dir):
            temp = file
            extension = 'none'
            try:
                extension = splitext(source_dir+'/'+file)[1]
            except Exception:
                extension = 'none'
            
            destination_path = extensions[extension ]

            duplicate = os.path.isfile(destination_path + "/" + temp)
            while(duplicate):
                i += 1
                temp = temp + str('(i)')
                duplicate = os.path.isfile(destination_path + "/" + temp)
            src = source_dir + "/" + file
            new_name = destination_path + "/" + temp
            os.rename(src, new_name)

source_dir = "/Users/kadenchien/Downloads"
music_dir = "/Users/kadenchien/Downloads/Music"
image_dir = "/Users/kadenchien/Downloads/Images"
pres_dir = "/Users/kadenchien/Downloads/Presentations"
doc_dir = "/Users/kadenchien/Downloads/Documents"
sheet_dir = "/Users/kadenchien/Downloads/Spreadsheets"
extensions = {
#music
',mp3' : music_dir,
'.wav' : music_dir,
'.m4a' : music_dir,

#images
'.jpg' : image_dir,
'.jpeg' : image_dir,
'.png' : image_dir,
'.jif' : image_dir,
'.jfif' : image_dir,
'.webp' : image_dir,

#presentations
'.pptx' : pres_dir,
'.ppt' : pres_dir,
'.pptm' : pres_dir,

#documents
'.pdf' : doc_dir,
'.docx' : doc_dir,
'.doc' : doc_dir,

#spreadsheets
'.xls' : doc_dir,
'.csx' : doc_dir,
'.xlsx' : doc_dir
}

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, source_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    observer.stop()
observer.join()