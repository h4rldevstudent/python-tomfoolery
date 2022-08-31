import tkinter as tk
import pygame
import time
import os



root = tk.Tk()

audio_file = os.path.dirname(__file__) + '/assets/audio.mp3'
message = tk.Label(root, text="You just got sussied!")
root.title("Amogus")
root.wm_iconbitmap('./assets/amogus.ico')
root.geometry("1200x800")

pygame.mixer.init()# initialise the pygame

frame = tk.PhotoImage(file='./assets/amogus.png')

def play():
    pygame.mixer.music.load("./assets/audio.mp3")
    pygame.mixer.music.play(loops=1)

image_label = tk.Label(
    root,
    image=frame,
)

message.pack()
image_label.pack()
play()
tk.mainloop()


