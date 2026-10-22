import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import json

class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Note App")
        self.notes = []
        self.note_index = 0
        self.create_widgets()

    def create_widgets(self):
        # Create note list
        self.note_list = tk.Listbox(self.root, width=50)
        self.note_list.pack(padx=10, pady=10)

        # Create buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        self.create_button = tk.Button(self.button_frame, text="Create Note", command=self.create_note)
        self.create_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Note", command=self.delete_note)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save Notes", command=self.save_notes)
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Create note editing widgets
        self.note_edit_frame = tk.Frame(self.root)
        self.note_edit_frame.pack(padx=10, pady=10)

        self.note_text = tk.Text(self.note_edit_frame, width=50, height=10)
        self.note_text.pack(padx=10, pady=10)

        self.priority_label = tk.Label(self.note_edit_frame, text="Priority:")
        self.priority_label.pack(padx=5, pady=5)

        self.priority_var = tk.StringVar()
        self.priority_var.set("Low")
        self.priority_menu = ttk.OptionMenu(self.note_edit_frame, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.pack(padx=5, pady=5)

        self.due_date_label = tk.Label(self.note_edit_frame, text="Due Date:")
        self.due_date_label.pack(padx=5, pady=5)

        self.due_date_entry = tk.Entry(self.note_edit_frame, width=20)
        self.due_date_entry.pack(padx=5, pady=5)

        self.search_label = tk.Label(self.note_edit_frame, text="Search:")
        self.search_label.pack(padx=5, pady=5)

        self.search_entry = tk.Entry(self.note_edit_frame, width=20)
        self.search_entry.pack(padx=5, pady=5)

        self.search_button = tk.Button(self.note_edit_frame, text="Search", command=self.search_notes)
        self.search_button.pack(padx=5, pady=5)

    def create_note(self):
        # Create new note
        note = tk.Toplevel(self.root)
        note.title("New Note")

        # Create note text
        note_text = tk.Text(note, width=50, height=10)
        note_text.pack(padx=10, pady=10)

        # Create save button
        save_button = tk.Button(note, text="Save", command=lambda: self.save_note(note_text.get("1.0", tk.END), note))
        save_button.pack(padx=10, pady=10)

    def save_note(self, note_text, note):
        # Save note to list
        self.notes.append(note_text)
        self.note_list.insert(tk.END, note_text)

        # Close note window
        note.destroy()

    def delete_note(self):
        # Delete selected note
        try:
            index = self.note_list.curselection()[0]
            self.notes.pop(index)
            self.note_list.delete(index)
        except IndexError:
            messagebox.showinfo("Error", "No note selected")

    def save_notes(self):
        # Save notes to file
        with open("notes.json", "w") as f:
            notes = [{"text": note, "priority": self.priority_var.get(), "due_date": self.due_date_entry.get()} for note in self.notes]
            json.dump(notes, f, indent=4)

    def search_notes(self):
        # Search for notes
        search_term = self.search_entry.get().lower()
        matching_notes = [note for note in self.notes if search_term in note.lower()]
        self.note_list.delete(0, tk.END)
        for note in matching_notes:
            self.note_list.insert(tk.END, note)

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.mainloop()