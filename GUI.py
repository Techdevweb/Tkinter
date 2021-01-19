#Tkinter is inbuilt module which is used to create apps
#It is one of the most commnly used module for GUI apps
#Steps:
#1.We import tkinter
#2.Create GUI application main window
#3.Add widgets
#4.Enter main event loop
#A widget is an element of a GUI which displays information or provides
#a specific way to interact with the OS
import tkinter

window=tkinter.Tk()
window.title("Eduraka")

top_frame = tkinter.Frame(window).pack()
bottom = tkinter.Frame(window).pack(side='bottom')

btn1=tkinter.Button(top_frame,text='Button 1',fg='red').pack()#fg is used to colour the text
btn2=tkinter.Button(top_frame,text='Button 2',fg='green').pack()
btn3=tkinter.Button(bottom,text='Button 1',fg='purple').pack(side='left')
btn4=tkinter.Button(bottom,text='Button 2',fg='orange').pack(side='left')
window.mainloop()