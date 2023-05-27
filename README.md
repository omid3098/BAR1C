# Bulk Runner

## Description

Sometimes (like When I want to play games), I need to open multiple apps. like the game itself, discord, camera app, streaming softwares, etc. So I made this tool to make it easier to open multiple apps at once.

## Build:

- Install requirements with `pip install -r requirements.txt`
- Find CustomTkinter installation path: `pip show customtkinter`
- If you are using venv, Build with `pyinstaller --noconfirm --onefile --windowed --icon "{project-path}/src/icon.ico" --add-data "{project-path}/.venv/Lib/site-packages/customtkinter;customtkinter/" --add-data "{project-path}/.venv/Lib/site-packages/tkinterdnd2;tkinterdnd2/" "{project-path}/main.py"`

  Or use auto-py-to-exe and add required dependencies (dnd2 and customtkinter)

  More info: [Packaging CustomTkinter](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging)
