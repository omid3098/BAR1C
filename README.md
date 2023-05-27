# Bulk Runner

## Description

A simple tool to create a .bat file to run multiple applications at once!

## Build:

- Install requirements with `pip install -r requirements.txt`
- Show CustomTkinter installation path: `pip show customtkinter`
- Build with `pyinstaller --noconfirm --onefile --windowed --icon "D:/w/Python/tkinter/src/icon.ico" --add-data "D:/w/Python/tkinter/.venv/Lib/site-packages/customtkinter;customtkinter/" --add-data "D:/w/Python/tkinter/.venv/Lib/site-packages/tkinterdnd2;tkinterdnd2/" "D:/w/Python/tkinter/main.py"`

Note: read this for [packaging CustomTkinter](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging)
