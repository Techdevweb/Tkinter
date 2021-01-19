import tkinter

window=tkinter.Tk()
window.title("Hello World")

# def say_hi():
#     tkinter.Label(window,text='Hey').pack()

def left(event):#event is simply a parameter
    tkinter.Label(window,text='Left mouse button').pack()

def right(event):
    tkinter.Label(window,text='Right mouse button').pack()


btn = tkinter.Button(window,text='Say hi')
btn.bind("<Button-1>",left)#bind function simply takes two parameters, event and it's function
btn.bind("<Button-3>",right)
btn.pack()
#b.bind("<Button-1>",left)

window.mainloop()