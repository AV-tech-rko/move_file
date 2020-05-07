# move_file
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class Myhandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(folder_from):
            source = folder_from + "/" + filename
            destination = folder_to + "/" + filename
            os.rename(source,destination)

folder_from = "/Users/auriday/Desktop/from"
folder_to = "/Users/auriday/Desktop/to"
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler,folder_from, recursive=True) 
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()        
observer.join()    
