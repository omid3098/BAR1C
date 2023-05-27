# Bulk Runner

## Description

A simple tool to create a .bat file to run multiple applications at once!

## Build:

- Install requirements with `pip install -r requirements.txt`
- Find CustomTkinter installation path: `pip show customtkinter`
- If you are using venv, Build with `pyinstaller --noconfirm --onefile --windowed --icon "{project-path}/src/icon.ico" --add-data "{project-path}/.venv/Lib/site-packages/customtkinter;customtkinter/" --add-data "{project-path}/.venv/Lib/site-packages/tkinterdnd2;tkinterdnd2/" "{project-path}/main.py"`

  Or use auto-py-to-exe and add required dependencies (dnd2 and customtkinter)

  More info: [Packaging CustomTkinter](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging)
