#!/usr/bin/python3

import tkinter
top = tkinter.Tk()

color1 = "#00A0B1"

p_bck = tkinter.PhotoImage(file="res/previous.png")
p_fwd = tkinter.PhotoImage(file="res/next.png")
p_ply = tkinter.PhotoImage(file="res/play.png")
p_pse = tkinter.PhotoImage(file="res/pause.png")

l_bck = tkinter.Label(top, image=p_bck, bg=color1)
l_fwd = tkinter.Label(top, image=p_fwd, bg=color1)
l_ply = tkinter.Label(top, image=p_ply, bg=color1)
l_pse = tkinter.Label(top, image=p_pse, bg=color1)

l_bck.place(x=0, y=25)
l_fwd.place(x=100, y=25)
l_ply.place(x=50, y=25)
l_pse.place(x=50, y=25)


top.geometry("150x100+1945+540")
top.configure(background=color1)
top.overrideredirect(True)
top.mainloop()
