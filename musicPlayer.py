import tkinter as tk
from tkinter.constants import END
from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os

import pygame

current_volume = float(0.5)

#main screen
master=Tk()
master.title("MUSIC PLAYER")
master.geometry("500x450")

var = tk.StringVar()
song_title = tk.Label(master, font="Helvetica 12 bold", textvariable=var)

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

# song_list = []
index = 0
count = 0

play_list = tk.Listbox(master, font=("Helvetica", 12, "bold"), bg="green", selectmode=tk.SINGLE)

for song in song_list:
  play_list.insert(END, song)

pygame.init()
pygame.mixer.init()

#functions
def play_song():
  pygame.mixer.music.load(play_list.get(tk.ACTIVE))
  var.set(play_list.get(tk.ACTIVE))
  pygame.mixer.music.play()

def stop():
  pygame.mixer.music.stop()

def pause():
  pygame.mixer.music.pause()

def unpause():
  pygame.mixer.music.unpause()

def increase_volume():
  try:
    global current_volume 
    if current_volume >=1: 
      volume_label.config(fg="green",text="volume : Max") 
      return
    current_volume= current_volume + float(0.1)  
    current_volume=round(current_volume,1) 
    mixer.music.set_volume(current_volume)
    volume_label.config(fg="green",text="volume:"+str(current_volume))
  except Exception as e: 
    print(e)
    song_title_label.config(fg="red",text="track hasn't been selected yet")

def reduce_volume():
  try:
    global current_volume 
    if current_volume <=0: 
      volume_label.config(fg="red",text="volume : Muted") 
      return
    current_volume= current_volume-float(0.1)  
    current_volume=round(current_volume,1) 
    mixer.music.set_volume(current_volume)
    volume_label.config(fg="green",text="volume:"+str(current_volume))
  except Exception as e: 
    print(e)  
    song_title_label.config(fg="red",text="track hasn't been selected yet")

def updatelabel():
  global index
  var.set(song_list[index])

def nextsong():
  global index
  index += 1
  if (count < index):
    pygame.mixer.music.load(song_list[index])
    pygame.mixer.music.play()
  else:
    index = 0
    pygame.mixer.music.load(song_list[index])
    pygame.mixer.music.play()
  try:
    updatelabel()
  except NameError:
    print("")

def previous():
  global index
  index -= 1
  if (index < count):
    pygame.mixer.music.load(song_list[index])
    pygame.mixer.music.play()
  else:
    index = 0
    pygame.mixer.music.load(song_list[index])
    pygame.mixer.music.play()
  try:
    updatelabel()
  except NameError:
    print("")

Button1 = tk.Button(master, text="Play", font=("calibri",12),command=play_song,activebackground="blue")
Button2 = tk.Button(master, text="Pause", font=("calibri",12), command=pause,activebackground="red")
Button3 = tk.Button(master, text="Resume", font=("calibri",12), command=unpause,activebackground="green")
Button4 = tk.Button(master, text="Stop", font=("calibri",12), command=stop,activebackground="green")
Button5 = tk.Button(master, text="-", font=("calibri",12),width=5, command=reduce_volume,activebackground="orange")
Button6 = tk.Button(master, text="+", font=("calibri",12),width=5, command=increase_volume,activebackground="orange")
Button7 = tk.Button(master, text="NEXT SONG", font=("calibri",12), command=nextsong,activebackground="blue")
Button8 = tk.Button(master, text="PREVIOUS SONG", font=("calibri",12), command=previous,activebackground="blue")

Label1 = tk.Label(master,text="CUSTOM MUSIC PLAYER",font=("calibri",15),fg="green")
Label2 = tk.Label(master,text="Select your music track please",font=("calibri",16),fg="blue")
Label3 = tk.Label(master,text="VOLUME",font=("calibri",11),fg="red")

song_title_label=Label(master,font=("calibri",12))
volume_label=Label(master,font=("calibri",12))

song_title.pack()
Label1.pack(fill="y")
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button7.pack(fill="x")
Button8.pack(fill="x")
Label3.pack(fill="y")
Button6.pack(fill="x")
Button5.pack(fill="x")
Label2.pack(fill="y")
play_list.pack(fill="both", expand="yes")

master.mainloop()
