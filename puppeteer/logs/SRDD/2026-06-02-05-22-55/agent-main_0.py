import json
import datetime
from dataclasses import dataclass
from typing import List
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Define a data class for TravelMemory
@dataclass
class TravelMemory:
    location: str
    date: datetime.date
    description: str
    photo: str = None

# Define a data class for Album
@dataclass
class Album:
    name: str
    memories: List[TravelMemory]

# Define a class for Planner
class Planner:
    def __init__(self):
        self.albums = {}

    def add_album(self, name: str):
        if name not in self.albums:
            self.albums[name] = Album(name, [])

    def add_memory(self, album_name: str, location: str, date: datetime.date, description: str, photo: str = None):
        if album_name in self.albums:
            self.albums[album_name].memories.append(TravelMemory(location, date, description, photo))
        else:
            print(f"Album '{album_name}' does not exist.")

    def get_album(self, name: str):
        return self.albums.get(name)

    def print_album(self, album: Album):
        print(f"Album Name: {album.name}")
        print("Album Memories:")
        for memory in album.memories:
            print(f"Location: {memory.location}")
            print(f"Date: {memory.date}")
            print(f"Description: {memory.description}")
            if memory.photo:
                print(f"Photo: {memory.photo}")
            print()

    def upload_photo(self, album_name: str):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        self.albums[album_name].memories[-1].photo = file_path

# Define a class for GUI
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Travel Memories Planner")
        self.planner = Planner()

        self.album_name_label = tk.Label(self.root, text="Album Name:")
        self.album_name_label.pack()
        self.album_name_entry = tk.Entry(self.root)
        self.album_name_entry.pack()

        self.location_label = tk.Label(self.root, text="Location:")
        self.location_label.pack()
        self.location_entry = tk.Entry(self.root)
        self.location_entry.pack()

        self.date_label = tk.Label(self.root, text="Date:")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        self.description_label = tk.Label(self.root, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()

        self.upload_button = tk.Button(self.root, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack()

        self.add_memory_button = tk.Button(self.root, text="Add Memory", command=self.add_memory)
        self.add_memory_button.pack()

        self.print_album_button = tk.Button(self.root, text="Print Album", command=self.print_album)
        self.print_album_button.pack()

    def upload_photo(self):
        self.planner.upload_photo(self.album_name_entry.get())

    def add_memory(self):
        self.planner.add_memory(self.album_name_entry.get(), self.location_entry.get(), datetime.date(int(self.date_entry.get().split('-')[0]), int(self.date_entry.get().split('-')[1]), int(self.date_entry.get().split('-')[2])), self.description_entry.get())

    def print_album(self):
        album = self.planner.get_album(self.album_name_entry.get())
        if album:
            self.planner.print_album(album)
        else:
            print("Album not found.")

    def run(self):
        self.root.mainloop()

# Create a GUI instance
gui = GUI()
gui.run()
