import tkinter as tk
import os
from tkinter.constants import END
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import pygame
from pygame import mixer
from tkinter import messagebox
from tkinter import Canvas


current_volume = float(0.5) # setting the default volume

#main screen
master=Tk()

master.title("MUSIC PLAYER") # main title
master.geometry("600x550") # Size of the player


# title for current song playing
var = tk.StringVar()
song_title = tk.Label(master, font="Helvetica 12 bold", textvariable=var, bg="blue")

# selecting the file to play songs from
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

# setting the playlist
play_list = tk.Listbox(master, font=("Helvetica", 12, "bold"), bg="sky blue", selectmode=tk.SINGLE)

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

def set_vol(val):
      volume=int(val)/100 # we divide by 100 to chieve the range from 0-1 used in the mixer
      mixer.music.set_volume(volume)
      

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

index = 0
count = 0
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



#volume scale
scale = tk.Scale(master, from_=0, to=100, orient="horizontal", resolution=1,bg="sky blue",command=set_vol)
scale.set(50)
scale.pack


#display attributes
'''
canvas = Canvas(master,width=500,height=200,bg="sky blue")
canvas.pack(fill="both", expand="yes")

my_image = tk.PhotoImage(file='C:\\Users\\josephine\\music-player\\music-player\\music_gif.gif')
canvas.create_image(600,0,anchor ="n", image=my_image)
'''


photo = tk.PhotoImage(file="C:\\Users\\josephine\\music-player\\music-player\\music_gif.gif")

gif_index = 0
def next_frame():
    global gif_index
    try:
        #XXX: Move to the next frame
        photo.configure(format="gif -index {}".format(gif_index))
        gif_index += 1
    except tk.TclError:
        gif_index = 0
        return next_frame()
    else:
        master.after(100, next_frame) # XXX: Fixed animation speed
label = tk.Label(master, image=photo,anchor="n")
label.pack(fill="x", padx="0",pady="0")
master.after_idle(next_frame)


Button1 = tk.Button(master, text="Play", font=("calibri",12),command=play_song,activebackground="blue")
Button2 = tk.Button(master, text="Pause", font=("calibri",12), command=pause,activebackground="red")
Button3 = tk.Button(master, text="Resume", font=("calibri",12), command=unpause,activebackground="green")
Button4 = tk.Button(master, text="Stop", font=("calibri",12), command=stop,activebackground="red")
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
Button1.pack(side="left")
Button2.pack(side="right")
Button3.pack(side="left")
Button4.pack(side="right")
Button7.pack(side="left")
Button8.pack(side="right")

Label3.pack(fill="y")
scale.pack(fill="x")
#Button6.pack(fill="x")
#Button5.pack(fill="x")
Label2.pack(fill="y")

play_list.pack(fill="both", expand="yes")


master.mainloop()
