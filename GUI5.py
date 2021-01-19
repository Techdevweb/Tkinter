import tkinter

window=tkinter.Tk()
window.title("Hello World")

icon=tkinter.PhotoImage(file="Blackjack.png")

img=tkinter.Label(window,image=icon)
img.pack()

window.mainloop()