import os
from pathlib import Path
from datetime import datetime

p = Path.cwd()

for root, dirs, files in os.walk(p):
    for file in files:
        if file.endswith("ipynb"):
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path) / 1024
            t = os.path.getmtime(full_path)
            dt = datetime.fromtimestamp(t)
            formatted = dt.strftime("%d/%m/%Y %I:%M:%S %p")
            print(f"Path{full_path} || Size:{size: .2f} kb || Time: {formatted}")
