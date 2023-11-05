# watcher.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f'File {event.src_path} has been changed. Reloading...')
            subprocess.run(['python', 'Second.py'])

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='E:\Downloads\DBMS\DBMS Project\Main\watcher2.py', recursive=True)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
