import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import pydub
from gtts import gTTS
import os

class StoryReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Bedtime Story Reader")
        self.root.geometry("800x600")

        # Story library
        self.story_library = {
            "story1": {"text": "Once upon a time...", "images": ["image1.jpg", "image2.jpg"], "audio": "audio1.mp3"},
            "story2": {"text": "The sun was shining...", "images": ["image3.jpg", "image4.jpg"], "audio": "audio2.mp3"}
        }

        # User interface
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = tk.Frame(self.notebook)
        self.frame2 = tk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="Story 1")
        self.notebook.add(self.frame2, text="Story 2")

        # Interactive features
        self.button1 = tk.Button(self.frame1, text="Play Audio", command=self.play_audio)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.frame2, text="Show Images", command=self.show_images)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self.frame1, text="Voice-Over", command=self.voice_over)
        self.button3.pack(pady=10)

    def play_audio(self):
        # Play audio file
        pygame.init()
        pygame.mixer.music.load(self.story_library["story1"]["audio"])
        pygame.mixer.music.play()

    def show_images(self):
        # Show images
        image1 = Image.open(self.story_library["story1"]["images"][0])
        image2 = Image.open(self.story_library["story1"]["images"][1])

        image1_tk = ImageTk.PhotoImage(image1)
        image2_tk = ImageTk.PhotoImage(image2)

        label1 = tk.Label(self.frame1, image=image1_tk)
        label1.pack(pady=10)

        label2 = tk.Label(self.frame2, image=image2_tk)
        label2.pack(pady=10)

    def voice_over(self):
        # Voice-over narration
        tts = gTTS(text=self.story_library["story1"]["text"], lang="en")
        tts.save("voice_over.mp3")
        pygame.init()
        pygame.mixer.music.load("voice_over.mp3")
        pygame.mixer.music.play()

root = tk.Tk()
app = StoryReader(root)
root.mainloop()