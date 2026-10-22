import tkinter as tk
from tkinter import ttk
import webbrowser

class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Note App")
        self.root.geometry("300x200")

        # Create a notebook with two tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create a tab for notes
        self.notes_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.notes_tab, text="Notes")

        # Create a tab for links
        self.links_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.links_tab, text="Links")

        # Create a text box for notes
        self.notes_text = tk.Text(self.notes_tab)
        self.notes_text.pack(fill="both", expand=True)

        # Create a button to save notes
        self.save_button = ttk.Button(self.notes_tab, text="Save Notes", command=self.save_notes)
        self.save_button.pack()

        # Create a text box for links
        self.links_text = tk.Text(self.links_tab)
        self.links_text.pack(fill="both", expand=True)

        # Create a button to open links
        self.open_button = ttk.Button(self.links_tab, text="Open Links", command=self.open_links)
        self.open_button.pack()

    def save_notes(self):
        # Save the notes to a file
        with open("notes.txt", "w") as f:
            f.write(self.notes_text.get("1.0", "end-1c"))

    def open_links(self):
        # Open the links in the browser
        links = self.links_text.get("1.0", "end-1c").splitlines()
        for link in links:
            webbrowser.open(link)

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.mainloop()