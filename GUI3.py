import tkinter

window=tkinter.Tk()
window.title('Login page')

tkinter.Label(window,text='Username').grid(row=0)
tkinter.Entry(window).grid(row=0,column=1)

tkinter.Label(window,text='Password').grid(row=1)
tkinter.Entry(window).grid(row=1,column=1)

tkinter.Checkbutton(window,text='Keep me logged in').grid(columnspan=2)#columnspan takes the width of two columns

window.mainloop()