import sys
from pathlib import Path
from PyInstaller.__main__ import run


main_script = "main.py"

# Specify additional PyInstaller options
pyinstaller_options = [
    "--name=BAR1C",
    "--onefile",
    "--windowed",
    "--icon=icon.ico",
    # customtkinter
    "--add-data=.venv/Lib/site-packages/customtkinter;customtkinter",
    # tkinterdnd2
    "--add-data=.venv/Lib/site-packages/tkinterdnd2;tkinterdnd2",
]

# Add any additional files or resources required by your application
additional_files = [("icon.ico", ".")]  # Add any additional files or resources here

# Build the executable using PyInstaller
run([*pyinstaller_options, main_script])

# Copy additional files to the output directory
for filename, directory in additional_files:
    path = Path(directory) / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((Path(".") / filename).read_bytes())
