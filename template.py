import os
from pathlib import Path

list_of_files  = [
    
    f".env",
    f"setup.py",
    f"app.py",
    f"requirements.txt",
    f"src/__init__.py",
    f"src/helper.py",
    f"src/prompt.py",
    f"notebook/trigger.ipynb"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename  = os.path.split(filepath)
    print("filepath",filepath)
    print(filedir)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if not os.path.exists(filepath) or os.path.getsize == 0:
        with open(filepath,"w") as f:
            pass
    else:
        print("path already exists")

