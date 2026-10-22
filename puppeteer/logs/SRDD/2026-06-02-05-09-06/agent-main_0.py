import tkinter as tk
from tkinter import messagebox
import os

class StickyNote:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Notes")
        self.root.geometry("300x400")
        self.notes = {}

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create note frame
        self.note_frame = tk.Frame(self.main_frame)
        self.note_frame.pack(fill="both", expand=True)

        # Create button frame
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(fill="x")

        # Create add button
        self.add_button = tk.Button(self.button_frame, text="Add Note", command=self.add_note)
        self.add_button.pack(side="left")

        # Create delete button
        self.delete_button = tk.Button(self.button_frame, text="Delete Note", command=self.delete_note)
        self.delete_button.pack(side="left")

        # Create save button
        self.save_button = tk.Button(self.button_frame, text="Save Notes", command=self.save_notes)
        self.save_button.pack(side="left")

        # Create load button
        self.load_button = tk.Button(self.button_frame, text="Load Notes", command=self.load_notes)
        self.load_button.pack(side="left")

    def add_note(self):
        # Create new note frame
        self.note = tk.Frame(self.note_frame)
        self.note.pack(fill="x")

        # Create note text box
        self.text_box = tk.Text(self.note, width=40, height=5)
        self.text_box.pack(fill="both", expand=True)

        # Create note title label
        self.title_label = tk.Label(self.note, text="Note Title:")
        self.title_label.pack(side="left")

        # Create note title entry
        self.title_entry = tk.Entry(self.note, width=20)
        self.title_entry.pack(side="left")

        # Create save button
        self.save_button = tk.Button(self.note, text="Save", command=lambda: self.save_note(self.note))
        self.save_button.pack(side="left")

        # Add note to dictionary
        self.notes[self.note] = {"title": self.title_entry, "text": self.text_box}

    def delete_note(self):
        # Get selected note
        for widget in self.note_frame.winfo_children():
            if widget != self.button_frame:
                self.note_frame.pack_forget()
                widget.destroy()

    def save_notes(self):
        # Save notes to file
        with open("notes.txt", "w") as f:
            for note in self.notes:
                f.write(f"Title: {self.notes[note]['title'].get()}\n")
                f.write(self.notes[note]['text'].get("1.0", "end") + "\n\n")

    def load_notes(self):
        # Load notes from file
        try:
            with open("notes.txt", "r") as f:
                lines = f.readlines()
                for i in range(0, len(lines), 3):
                    title = lines[i].strip()
                    text = lines[i+1].strip()
                    note = tk.Frame(self.note_frame)
                    note.pack(fill="x")
                    tk.Label(note, text=title).pack(side="left")
                    tk.Text(note, width=40, height=5, text=text).pack(fill="both", expand=True)
        except FileNotFoundError:
            messagebox.showinfo("Error", "No notes found.")

    def save_note(self, note):
        # Save note to dictionary
        self.notes[note] = {"title": self.title_entry, "text": self.text_box}

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNote(root)
    root.mainloop()