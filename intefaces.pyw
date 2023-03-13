from tkinter import *
import tkvideo
import os

window=Tk()
window.geometry('1080x620+300+200')
window.configure(bg="black")
window.resizable(False,False)

my_label = Label(window)
my_label.pack()
player = tkvideo.tkvideo("background.mp4", my_label, loop = 0, size = (1080,620))
player.play()

def inter1():
    os.startfile('interface1.pyw')
    window.destroy()
def inter2():
    os.startfile('interface2.pyw')
    window.destroy()
def inter3():
    os.startfile('interface3.pyw')
    window.destroy()


Button(window,width=35,pady=5,text='Interface 1',bg='#FFFFE0',fg='Brown',border=0,command=inter1).place(x=300,y=190)
Button(window,width=35,pady=5,text='Interface 2',bg='#FFFFE0',fg='Brown',border=0,command=inter2).place(x=300,y=350)
Button(window,width=35,pady=5,text='Interface 3',bg='#FFFFE0',fg='Brown',border=0,command=inter3).place(x=300,y=510)

window.mainloop()