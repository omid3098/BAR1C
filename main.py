import os
import sys
import customtkinter as ctk
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
        self.grid_columnconfigure(1, weight=3)
        self.items = []

        self.title = ctk.CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            value = value.strip("{}")
            # show only the file name
            file_name = self.get_filename_without_ext(value)
            lable = ctk.CTkLabel(self, text=file_name)
            lable.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")

            self.items.append(value)

    def get(self):
        return self.items

    def get_filename_without_ext(self, filepath):
        filepath = filepath.strip("{}")
        basename = os.path.basename(filepath)
        filename, _ = os.path.splitext(basename)
        return filename


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
        self.title("BAR1C")
        self.geometry("900x480")
        # self.iconbitmap("/icon.ico")

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.files = []
        self.side_bar_l = SideBar(self, self.files, title="Selected Files:")
        self.side_bar_l.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.drag_and_drop = DragAndDrop(self)
        self.drag_and_drop.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.drag_and_drop.drop_target_register(DND_FILES)
        self.drag_and_drop.dnd_bind("<<Drop>>", self.drop)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.file_name_label = ctk.CTkLabel(self, text="File Name:")
        self.file_name_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.file_name_entry = ctk.CTkEntry(self)
        self.file_name_entry.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew")

        self.run_button = ctk.CTkButton(
            self, text="Create", command=self.run_button_callback
        )
        self.run_button.grid(
            row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2
        )

    def run_button_callback(self):
        links = self.side_bar_l.get()
        bat_file_contents = "@echo off\n\n"
        for link in links:
            bat_file_contents += f"PowerShell -Command \"Start-Process '{link}'\"\n"

        print(bat_file_contents)
        # save the bat file on the desktop with the name that user entered in self.file_name_entry
        file_name = self.file_name_entry.get()
        file_name = file_name.strip()
        if not file_name:
            file_name = "bulk_runner"
        file_name = file_name + ".bat"
        desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
        # if the directory does not exist, create it
        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)
        # TODO: In some cases in windows 11 the desktop path is in a OneDrive folder like: C:\Users\{username}\OneDrive\Desktop
        file_path = os.path.join(desktop_path, file_name)
        with open(file_path, "w") as f:
            f.write(bat_file_contents)

        # open windows explorer on the desktop
        os.startfile(desktop_path)

    def drop(self, event):
        self.files.append(event.data)
        self.side_bar_l.destroy()
        self.side_bar_l = SideBar(self, self.files, title="Selected Files")
        self.side_bar_l.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


app = App()
app.mainloop()
