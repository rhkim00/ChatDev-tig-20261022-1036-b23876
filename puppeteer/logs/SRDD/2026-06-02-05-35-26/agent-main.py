import tkinter as tk
from tkinter import messagebox
import random

class MusicNoteTrainer:
    def __init__(self):
        print("Initializing MusicNoteTrainer...")
        self.root = tk.Tk()
        self.root.title("Music Note Trainer")
        self.notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.current_note = ''
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        print("Creating widgets...")
        self.note_label = tk.Label(self.root, text="Note:")
        self.note_label.pack()

        self.note_display = tk.Label(self.root, text="")
        self.note_display.pack()

        self.generate_note_button = tk.Button(self.root, text="Generate Note", command=self.generate_note)
        self.generate_note_button.pack()

    def generate_note(self):
        print("Generating note...")
        self.current_note = random.choice(self.notes)
        self.note_display.config(text=self.current_note)
        messagebox.showinfo("Note Generated", f"The current note is: {self.current_note}")

if __name__ == "__main__":
    print("Starting MusicNoteTrainer...")
    app = MusicNoteTrainer()