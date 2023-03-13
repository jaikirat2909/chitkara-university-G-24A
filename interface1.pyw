from tkinter import *
from new import main
import tkvideo
from tkinter import messagebox

window=Tk()
window.geometry('1080x620+300+200')
window.configure(bg="black")
window.resizable(False,False)

my_label = Label(window)
my_label.pack()
player = tkvideo.tkvideo("inteface1.mp4", my_label, loop = 0, size = (1080,620))
player.play()

def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'How many times you want to use this porgram')

user=Entry(window,width=40,fg='red',font=('Microsoft YaHei UI Light',11))
user.place(x=700,y=240)
user.insert(0,'How many times you want to use this porgram')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Enter the text you want to translate')


code=Entry(window,width=40,fg='red',font=('Microsoft YaHei UI Light',11))
code.place(x=700,y=320)
code.insert(0,'Enter the text you want to translate')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

  
def tts():
    times=user.get()
    word=code.get()
    ans=main(times,word)
    messagebox.showinfo("Output", ans)
    


Button(text='Translate',width=10,bg='red',fg='white',command=tts).place(x=930,y=400)

window.mainloop()