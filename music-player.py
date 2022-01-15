import pygame
import os
import tkinter as tk
from tkinter.filedialog import askdirectory


music_player = tk.Tk()
music_player.title("Music Player")
directory = askdirectory()
music_player.geometry("450x350")
os.chdir(directory)
song_list = os.listdir()

play_list = tk.Listbox(music_player, font="Helvetica 10 bold", bg='white', selectmode=tk.SINGLE)
for item in song_list:
   pos = 0
   play_list.insert(pos, item)
   pos += 1
pygame.init()
pygame.mixer.init()

def play():
   pygame.mixer.music.load(play_list.get(tk.ACTIVE))
   var.set(play_list.get(tk.ACTIVE))
   pygame.mixer.music.play()
def stop():
   pygame.mixer.music.stop()
def pause():
   pygame.mixer.music.pause()
def unpause():
   pygame.mixer.music.unpause()
Button1 = tk.Button(music_player, width=4, height=2, font="Helvetica 10 bold", text="PLAY", command=play,)
Button2 = tk.Button(music_player, width=4, height=2, font="Helvetica 10 bold", text="STOP", command=stop,)
Button3 = tk.Button(music_player, width=4, height=2, font="Helvetica 10 bold", text="PAUSE", command=pause,)
Button4 = tk.Button(music_player, width=4, height=2, font="Helvetica 10 bold", text="UNPAUSE", command=unpause,)
var = tk.StringVar()
song_title = tk.Label(music_player, font="Helvetica 10 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")
music_player.mainloop()