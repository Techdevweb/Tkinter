import tkinter

window=tkinter.Tk()
window.title("Hello World")

tkinter.Label(window,text='Surface width',fg='white',bg='purple').pack()
tkinter.Label(window,text='X direction',fg='white',bg='green').pack(fill='x')
tkinter.Label(window,text='Y direction',fg='white',bg='black').pack(fill='y',side='left')

window.mainloop()