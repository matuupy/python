from tkinter import *
from tkinter.ttk import *
from Reproductor import *

musica =  Reproductor('badbunny.mp3')

def play_musica():
    musica.volume (1)
    display.config(text= musica.play())


def pause_musica():
    display.config(text= musica.pause())

master = Tk()
master.geometry("200x200")

display = Label (master, text = "Reproductor de música")

display.pack(pady = 10)

btn_play = Button(master,text = "▶", command=play_musica)
btn_play.pack(pady = 10)

btn_pause = Button(master,text = "⏸", command=pause_musica)
btn_pause.pack(pady = 10)
mainloop()

