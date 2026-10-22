import tkinter as tk
from tkinter import messagebox
import random

class MusicNoteTrainer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Note Trainer")
        self.difficulty_level = tk.StringVar()
        self.difficulty_level.set("Easy")
        self.exercise_type = tk.StringVar()
        self.exercise_type.set("Individual Notes")
        self.score = 0
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Difficulty Level:").grid(row=0, column=0)
        tk.OptionMenu(self.root, self.difficulty_level, "Easy", "Medium", "Hard").grid(row=0, column=1)
        tk.Label(self.root, text="Exercise Type:").grid(row=1, column=0)
        tk.OptionMenu(self.root, self.exercise_type, "Individual Notes", "Intervals").grid(row=1, column=1)
        self.start_button = tk.Button(self.root, text="Start", command=self.start_exercise)
        self.start_button.grid(row=2, column=0, columnspan=2)
        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.grid(row=3, column=0, columnspan=2)

    def start_exercise(self):
        self.start_button.config(state="disabled")
        self.exercise_type_label = tk.Label(self.root, text="Exercise Type: " + self.exercise_type.get())
        self.exercise_type_label.grid(row=4, column=0, columnspan=2)
        self.note_label = tk.Label(self.root, text="")
        self.note_label.grid(row=5, column=0, columnspan=2)
        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.grid(row=6, column=0, columnspan=2)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.grid(row=7, column=0, columnspan=2)

    def check_answer(self):
        try:
            answer = self.answer_entry.get()
            if self.exercise_type.get() == "Individual Notes":
                if answer == str(random.randint(1, 12)):
                    self.score += 1
                    self.score_label.config(text="Score: " + str(self.score))
                    self.note_label.config(text="Correct! Next note: " + str(random.randint(1, 12)))
                    self.answer_entry.delete(0, tk.END)
                else:
                    self.score_label.config(text="Score: " + str(self.score))
                    self.note_label.config(text="Incorrect. Next note: " + str(random.randint(1, 12)))
                    self.answer_entry.delete(0, tk.END)
            elif self.exercise_type.get() == "Intervals":
                if answer == str(random.randint(1, 12)):
                    self.score += 1
                    self.score_label.config(text="Score: " + str(self.score))
                    self.note_label.config(text="Correct! Next interval: " + str(random.randint(1, 12)))
                    self.answer_entry.delete(0, tk.END)
                else:
                    self.score_label.config(text="Score: " + str(self.score))
                    self.note_label.config(text="Incorrect. Next interval: " + str(random.randint(1, 12)))
                    self.answer_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.start_button.config(state="normal")
            self.submit_button.config(state="disabled")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MusicNoteTrainer()
    app.run()