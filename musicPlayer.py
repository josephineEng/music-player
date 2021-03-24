from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)

#functions
def play_song():
    filename=filedialog.askopenfilename(initialdir="C:/",title="please select a file")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green",text="Now playing :"+str(song_title))
        volume_label.config(fg="green",text="vloume:"+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Error playing truck")

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

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e) 
        song_title_label.config(fg="red",text="track hasn't been selected yet")

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e) 
        song_title_label.config(fg="red",text="track hasn't been selected yet")

#Main Screen
master=Tk()
master.title("MUSIC PLAYER")




#labels
Label(master,text="CUSTOME MUSIC PLAYER",font=("calibri",15),fg="green").grid(sticky="N",row=0,padx=120)
Label(master,text="Select your music truck please",font=("calibri",11),fg="blue").grid(sticky="N",row=1)
Label(master,text="VOLUME",font=("calibri",11),fg="red").grid(sticky="N",row=4)

song_title_label=Label(master,font=("calibri",12))
song_title_label.grid(stick="N",row=3)
volume_label=Label(master,font=("calibri",12))
volume_label.grid(sticky="N",row=5)

#buttons
Button(master,text="select your song",font=("calibri",12),command=play_song).grid(row=2,sticky="N")
Button(master,text="pause",font=("calibri",12),command=pause).grid(row=3,sticky="E")
Button(master,text="resume",font=("calibri",12),command=resume).grid(row=3,sticky="W")
Button(master,text="-",font=("calibri",12),width=5,command=reduce_volume).grid(row=5,sticky="W")
Button(master,text="+",font=("calibri",12),width=5,command=increase_volume).grid(row=5,sticky="E")


master.mainloop()
