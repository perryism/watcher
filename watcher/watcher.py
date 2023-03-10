from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def on_created(self, folder, patterns):
        p = PatternMatchingEventHandler(patterns=patterns)
        self.observer.schedule(p, folder, recursive=True)

        def wrap(func):
            p.on_created = func

            #<FileCreatedEvent: event_type=created, src_path='', is_directory=False>
            def handler(file):
                func(file)
            return handler
        return wrap

    def start(self):
        self.observer.start()

        try:
            while True:
                # Set the thread sleep time
                time.sleep(0)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()