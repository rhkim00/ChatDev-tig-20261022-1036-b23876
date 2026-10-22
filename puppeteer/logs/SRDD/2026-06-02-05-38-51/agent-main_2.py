import json
import tkinter as tk
from tkinter import ttk
import pyttsx3
import random

class BedtimeStoryReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Bedtime Story Reader")
        self.engine = pyttsx3.init()

        # Create a notebook with two tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create a frame for the story tab
        self.story_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.story_frame, text="Story")

        # Create a frame for the animation tab
        self.animation_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.animation_frame, text="Animation")

        # Create a label and text box for the story
        self.story_label = ttk.Label(self.story_frame, text="Story:")
        self.story_label.pack(pady=10)
        self.story_text = tk.Text(self.story_frame, width=50, height=10)
        self.story_text.pack(pady=10)

        # Create a button to start the story
        self.start_button = ttk.Button(self.story_frame, text="Start Story", command=self.start_story)
        self.start_button.pack(pady=10)

        # Create a label and text box for the animation
        self.animation_label = ttk.Label(self.animation_frame, text="Animation:")
        self.animation_label.pack(pady=10)
        self.animation_text = tk.Text(self.animation_frame, width=50, height=10)
        self.animation_text.pack(pady=10)

        # Create a button to start the animation
        self.animation_button = ttk.Button(self.animation_frame, text="Start Animation", command=self.start_animation)
        self.animation_button.pack(pady=10)

        # Create a frame for the settings tab
        self.settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_frame, text="Settings")

        # Create a label and text box for the voice
        self.voice_label = ttk.Label(self.settings_frame, text="Voice:")
        self.voice_label.pack(pady=10)
        self.voice_text = tk.Text(self.settings_frame, width=50, height=1)
        self.voice_text.pack(pady=10)

        # Create a label and text box for the speed
        self.speed_label = ttk.Label(self.settings_frame, text="Speed:")
        self.speed_label.pack(pady=10)
        self.speed_text = tk.Text(self.settings_frame, width=50, height=1)
        self.speed_text.pack(pady=10)

        # Create a label and text box for the pitch
        self.pitch_label = ttk.Label(self.settings_frame, text="Pitch:")
        self.pitch_label.pack(pady=10)
        self.pitch_text = tk.Text(self.settings_frame, width=50, height=1)
        self.pitch_text.pack(pady=10)

        # Create a button to save the settings
        self.save_button = ttk.Button(self.settings_frame, text="Save Settings", command=self.save_settings)
        self.save_button.pack(pady=10)

    def start_story(self):
        # Get the story text from the text box
        story_text = self.story_text.get("1.0", tk.END)

        # Split the story into sentences
        sentences = story_text.split(". ")

        # Create a list to store the sentences with animations
        animated_sentences = []

        # Loop through each sentence
        for sentence in sentences:
            # Get a random animation
            animation = random.choice(["*twinkle*", "*sparkle*", "*flash*"])

            # Add the sentence and animation to the list
            animated_sentences.append(f"{sentence} {animation}")

        # Join the animated sentences into a single string
        animated_story = ". ".join(animated_sentences)

        # Print the animated story
        print("Animated Story:")
        print(animated_story)

        # Speak the animated story
        self.engine.say(animated_story)
        self.engine.runAndWait()

    def start_animation(self):
        # Get the animation text from the text box
        animation_text = self.animation_text.get("1.0", tk.END)

        # Print the animation text
        print("Animation:")
        print(animation_text)

        # Create a tkinter window for the animation
        animation_window = tk.Toplevel(self.root)
        animation_window.title("Animation")

        # Create a label for the animation
        animation_label = ttk.Label(animation_window, text=animation_text)
        animation_label.pack(pady=10)

        # Create a button to close the animation window
        close_button = ttk.Button(animation_window, text="Close", command=animation_window.destroy)
        close_button.pack(pady=10)

    def save_settings(self):
        # Get the voice, speed, and pitch from the text boxes
        voice = self.voice_text.get("1.0", tk.END)
        speed = self.speed_text.get("1.0", tk.END)
        pitch = self.pitch_text.get("1.0", tk.END)

        # Save the settings to a file
        with open("settings.json", "w") as f:
            json.dump({"voice": voice, "speed": speed, "pitch": pitch}, f)

if __name__ == "__main__":
    root = tk.Tk()
    bedtime_story_reader = BedtimeStoryReader(root)
    root.mainloop()

class BedtimeStoryReader:
    # ...

    def start_storybook(self):
        # Create a new frame for the storybook
        self.storybook_frame = ttk.Frame(self.root)
        self.notebook.add(self.storybook_frame, text="Storybook")

        # Create a label and text box for the story
        self.story_label = ttk.Label(self.storybook_frame, text="Story:")
        self.story_label.pack(pady=10)
        self.story_text = tk.Text(self.storybook_frame, width=50, height=10)
        self.story_text.pack(pady=10)

        # Create a button to turn the page
        self.page_button = ttk.Button(self.storybook_frame, text="Turn Page", command=self.turn_page)
        self.page_button.pack(pady=10)

    def turn_page(self):
        # Get the current page number
        page_number = int(self.story_text.index("end-1c").split(".")[0])

        # Get the next page number
        next_page_number = page_number + 1

        # Get the next page text
        next_page_text = self.story_text.get(f"{next_page_number}.0", f"{next_page_number+1}.0")

        # Display the next page text
        self.story_text.delete("1.0", tk.END)
        self.story_text.insert("1.0", next_page_text)

import pygame

class BedtimeStoryReader:
    # ...

    def start_story(self):
        # Get the story text from the text box
        story_text = self.story_text.get("1.0", tk.END)

        # Split the story into sentences
        sentences = story_text.split(". ")

        # Create a list to store the sentences with animations
        animated_sentences = []

        # Loop through each sentence
        for sentence in sentences:
            # Get a random animation
            animation = random.choice(["*twinkle*", "*sparkle*", "*flash*"])

            # Add the sentence and animation to the list
            animated_sentences.append(f"{sentence} {animation}")

        # Join the animated sentences into a single string
        animated_story = ". ".join(animated_sentences)

        # Print the animated story
        print("Animated Story:")
        print(animated_story)

        # Speak the animated story
        self.engine.say(animated_story)
        self.engine.runAndWait()

        # Play a sound effect
        pygame.mixer.init()
        pygame.mixer.music.load("sound_effect.mp3")
        pygame.mixer.music.play()

import json

class BedtimeStoryReader:
    # ...

    def save_settings(self):
        # Get the voice, speed, and pitch from the text boxes
        voice = self.voice_text.get("1.0", tk.END)
        speed = self.speed_text.get("1.0", tk.END)
        pitch = self.pitch_text.get("1.0", tk.END)

        # Save the settings to a file
        with open("user_profiles.json", "w") as f:
            json.dump({"voice": voice, "speed": speed, "pitch": pitch}, f)

    def load_settings(self):
        # Load the settings from the file
        try:
            with open("user_profiles.json", "r") as f:
                settings = json.load(f)
                self.voice_text.delete("1.0", tk.END)
                self.voice_text.insert("1.0", settings["voice"])
                self.speed_text.delete("1.0", tk.END)
                self.speed_text.insert("1.0", settings["speed"])
                self.pitch_text.delete("1.0", tk.END)
                self.pitch_text.insert("1.0", settings["pitch"])
        except FileNotFoundError:
            pass