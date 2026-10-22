import json
import datetime
from dataclasses import dataclass
from typing import List

class TravelMemory:
    @dataclass
    class Album:
        @dataclass
        class Planner:
            def __init__(self):
                self.albums = {}

            def add_album(self, name: str):
                if name not in self.albums:
                    self.albums[name] = Album(name, [])

            def add_memory(self, album_name: str, location: str, date: datetime.date, description: str, photo: str = "Error"):
                if album_name in self.albums:
                    self.albums[album_name].memories.append(TravelMemory(location, date, description, photo))

            def get_album(self, name: str):
                return self.albums.get(name)

            def print_album(self, album: Album):
                print(f'Album Name: {album.name}')
                print('Album Memories:')
                for memory in album.memories:
                    print(f'Location: {memory.location}')
                    print(f'Date: {memory.date}')
                    print(f'Description: {memory.description}')
                    if memory.photo:
                        print(f'Photo: {memory.photo}')
                    print()

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Travel Memories Planner')
        self.planner = Planner()

    def upload_photo(self):
        self.planner.upload_photo(self.album_name_entry.get())

    def add_memory(self):
        self.planner.add_memory(self.album_name_entry.get(), self.location_entry.get(), datetime.date(int(self.date_entry.get().split('-')[0]), int(self.date_entry.get().split('-')[1]), int(self.date_entry.get().split('-')[2])), self.description_entry.get())

    def print_album(self):
        album = self.planner.get_album(self.album_name_entry.get())
        if album:
            self.planner.print_album(album)
        else:
            print('Album not found.')

    def run(self):
        self.root.mainloop()

gui = GUI()
gui.run()