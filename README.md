# Batch Application Runner 1 Click (BAR1C)

_Pronounced as "baric"_

![image](https://github.com/omid3098/BAR1C/assets/6388730/aa3771eb-22aa-4234-b659-7c3ee703ea3c)

## Description

Sometimes (like When I want to play games), I need to open multiple apps. like the game itself, discord, camera app, streaming softwares, etc. So I made this tool to make it easier to open multiple apps at once using one batch file.

I also wanted to learn how to use CustomTkinter, so... yeah.

## Usage:

- Drag and drop apps to the drop area
- Choose a file name for the batch file
- Click on "Create" button
  A batch file will be created in your desktop. Double click on it to run the apps.

## Build:

- Install requirements with `pip install -r requirements.txt`
- Find CustomTkinter installation path: `pip show customtkinter`
- If you are using venv, Build with `pyinstaller --noconfirm --onefile --windowed --icon "/icon.ico" --add-data ".venv/Lib/site-packages/customtkinter;customtkinter/" --add-data ".venv/Lib/site-packages/tkinterdnd2;tkinterdnd2/" "main.py"`

  Or use auto-py-to-exe and add required dependencies (dnd2 and customtkinter)

  More info: [Packaging CustomTkinter](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging)
