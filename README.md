# Example

<pre>
from watcher import Watcher
import argparse

watcher = Watcher()

argparse = argparse.ArgumentParser(prog = "watcher")
argparse.add_argument("-p", "--folder_path", help="folder to watch")
args = argparse.parse_args()

@watcher.on_created(args.folder_path, ["*.log"])
def do(file_path):
    print(file_path)

watcher.start()
</pre>