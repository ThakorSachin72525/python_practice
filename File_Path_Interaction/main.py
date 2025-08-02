import os
from pathlib import Path
from datetime import datetime

p = Path.cwd()

t_date = datetime.strptime("2025-07-28 12:20:25 AM", "%Y-%m-%d %I:%M:%S %p")

for root, dirs, files in os.walk(p):
    for file in files:
        if file.endswith("ipynb"):
            full_path = os.path.join(root, file)
            mod_time = os.path.getmtime(full_path)
            mod_dt = datetime.fromtimestamp(mod_time)

            if mod_dt >= t_date:
                size_kb = os.path.getsize(full_path) / 1024
                formatted_time = mod_dt.strftime("%d %m %Y %I:%M:%S %p")
                print(f"Path: {full_path} | Size: {size_kb:.2f} KB | Time: {formatted_time}")
