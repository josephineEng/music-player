from tkinter.constants import ACTIVE, END, GROOVE, VERTICAL
from pygame import mixer
import tkinter as tk
from tkinter import LabelFrame, Scrollbar, StringVar, Tk
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

play_list = tk.Listbox(master, font=("Helvetica", 12, "bold"), bg="green", selectmode=tk.SINGLE)

for song in song_list:
  pos = 0
  if pos == 0:
    play_list.insert(pos, song)
    pos += 1

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

Button1 = tk.Button(master, text="Play", font=("calibri",12),command=play_song)
Button2 = tk.Button(master, text="pause", font=("calibri",12), command=pause)
Button3 = tk.Button(master, text="resume", font=("calibri",12), command=unpause)
Button4 = tk.Button(master, text="-", font=("calibri",12),width=5, command=reduce_volume)
Button5 = tk.Button(master, text="+", font=("calibri",12),width=5, command=increase_volume)

Label1 = tk.Label(master,text="CUSTOM MUSIC PLAYER",font=("calibri",15),fg="green")
Label2 = tk.Label(master,text="Select your music track please",font=("calibri",16),fg="blue")
Label3 = tk.Label(master,text="VOLUME",font=("calibri",11),fg="red")

song_title_label=Label(master,font=("calibri",12))
# song_title_label.grid(stick="N",row=3)
volume_label=Label(master,font=("calibri",12))
# volume_label.grid(sticky="N",row=5)

song_title.pack()
Label1.pack(fill="y")
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Label3.pack(fill="y")
Button5.pack(fill="x")
Button4.pack(fill="x")
Label2.pack(fill="y")
play_list.pack(fill="both", expand="yes")

master.mainloop()
