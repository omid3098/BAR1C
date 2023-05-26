# An app with these features:
# - It has a main window with one button "Run"
# - It has a drag and drop area that user can drag files into that area.
# - Has a text input field to name the file saved file
# - It uses customtkinter library to have a modern look and feel
# - when user drags multiple files into the drag area, the app shows the icons of those dropped files, and when they press the save button, the app will create a .bat file like this:
# @echo off

# REM Run Riot Client
# start "" "D:\Games\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live

# REM Run Blitz
# start "" "C:\Users\omid3\AppData\Local\Programs\Blitz\Blitz.exe"

import customtkinter as ctk
from tkinter import StringVar, TOP
from tkinterdnd2 import DND_FILES, TkinterDnD


class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)


class SideBar(ctk.CTkScrollableFrame):
    def __init__(self, master, values, title="Side Bar"):
        super().__init__(master)
        self.values = values
        self.grid_columnconfigure(0, weight=1)
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            # activate the checkbox by default
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class DragAndDrop(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text="Drag and Drop Files Here")
        self.label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Bulk Runner")
        self.geometry("400x180")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.files = []
        self.side_bar_l = SideBar(self, self.files, title="Selected Files:")
        self.side_bar_l.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.drag_and_drop = DragAndDrop(self)
        self.drag_and_drop.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.drag_and_drop.drop_target_register(DND_FILES)
        self.drag_and_drop.dnd_bind("<<Drop>>", self.drop)

        self.button = ctk.CTkButton(self, text="Run", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checked checkboxes:", self.side_bar_l.get())

    def drop(self, event):
        self.files.append(event.data)
        self.side_bar_l.destroy()
        self.side_bar_l = SideBar(self, self.files, title="Selected Files")
        self.side_bar_l.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")


app = App()
app.mainloop()
