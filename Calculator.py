from tkinter import *
import math
import re

if __name__=="__main__":#In this program __name__ is __main__excpet other programs
    window=Tk()
    window.geometry('480x430')
    window.resizable(0,0)
    window.title('Calculator')
    window.configure(bg='sky blue')



    def btn_clk(item):
        global expression
        expression=expression+str(item)
        input_text.set(expression)

    def btn_clear():
        global expression
        expression=''
        input_text.set("")

    def btn_equal():
        global expression

        if 'log' in expression:
            equation=re.findall(r"[-+]?\d*\.\d+|\d+", expression)
            if len(equation) == 2:
                if '.' in equation[0]:
                    num1=float(equation[0])
                else:
                    num1=int(equation[0])
                num2=int(equation[1])
                result = math.log(num1, num2)
                result2 = str(result)
                input_text.set(result2)
                expression = str(result2)

            else:
                if '.' in equation[0]:
                    num1=float(equation[0])
                else:
                    num1=int(equation[0])
                result=math.log(num1)
                result2=str(result)
                input_text.set(result2)
                expression=str(result2)

        elif 'hypo' in expression:
            equation=re.findall(r"[-+]?\d*\.\d+|\d+",expression)
            if '.' in equation[0]:
                num1=float(equation[0])
            else:
                num1=int(equation[0])

            if '.' in equation[1]:
                num2=float(equation[1])
            else:
                num2=int(equation[1])
            result=math.hypot(num1,num2)
            result2=str(result)
            input_text.set(result2)
            expression=str(result2)

        elif '^' in expression:
            equation=re.findall(r"[-+]?\d*\.\d+|\d+",expression)
            if '.' in equation[0]:
                num1=float(equation[0])
            else:
                num1=int(equation[0])
            num2 = int(equation[1])
            result=1
            for i in range(0,num2):
                result=result*num1
            result2=str(result)
            input_text.set(result2)
            expression=str(result)

        elif expression[-1]=='%':
            equation=re.findall(r"[-+]?\d*\.\d+|\d+",expression)
            if '.' in equation[0]:
                num1=float(equation[0])
            else:
                num1=int(equation[0])

            if '.' in equation[1]:
                num2=float(equation[1])
            else:
                num2=int(equation[1])

            result=num2/100
            result2=result*num1
            result3=str(result2)
            input_text.set(result3)
            expression=str(result3)


        elif '!' in expression:
            equation=re.findall(r"\d+",expression)
            num=int(equation[0])
            result=1
            for i in range(1,num+1):
                result=result*i
            result2=str(result)
            input_text.set(result2)
            expression=str(result)

        elif 'sin(' in expression:
            equation=re.findall(r"[-+]?\d*\.\d+|\d+",expression)
            if '.' in equation[0]:
                num=float(equation[0])
            else:
                num=int(equation[0])

            result=math.sin(math.pi/num)
            result2=str(result)
            input_text.set(result2)
            expression=str(result2)

        elif 'cos(' in expression:
            equation=re.findall(r"[-+]?\d*\.\d+|\d+",expression)
            if '.' in equation[0]:
                num=float(equation[0])
            else:
                num=int(equation[0])

            result=math.cos(math.pi/num)
            result2=str(result)
            input_text.set(result2)
            expression=str(result2)

        elif 'tan(' in expression:
            equation=re.findall(r"[-+]?\d*\.\d+|\d+",expression)
            if '.' in equation[0]:
                num=float(equation[0])
            else:
                num=int(equation[0])

            result=math.tan(math.pi/num)
            result2=str(result)
            input_text.set(result2)
            expression=str(result2)


        else:
            result = str(eval(expression))#eval() calculates the expression
            input_text.set(result)
            expression = str(result)

    def btn_sqr():
        global expression
        no=float(expression)
        result=no*no
        result2=str(result)
        input_text.set(result2)
        expression=str(result2)

    def btn_sqrt():
        global expression
        no=float(expression)
        result=math.sqrt(no)
        result2=str(result)
        input_text.set(result2)
        expression=str(result2)

    def btn_div():
        global expression
        no=float(expression)
        result=1/no
        result2=str(result)
        input_text.set(result2)
        expression=str(result2)

    def btn_degree():
        global expression
        no=float(expression)
        result=math.degrees(no)
        result2=str(result)
        input_text.set(result2)
        expression=str(result2)

    def btn_radians():
        global expression
        no=float(expression)
        result=math.radians(no)
        result2=str(result)
        input_text.set(result2)
        expression=str(result2)





    expression=''
    input_text=IntVar()

    input_frame=Frame(window,width=300,height=50)#Input field frame
    input_frame.pack(side=TOP,fill='x')

    input_field=Entry(input_frame,textvariable=input_text,width=50,font=('arial',20,'bold'),bg='white',relief='sunken')
    input_field.pack()

    btn_frame=Frame(window,width=400,height=400,bg='grey')
    btn_frame.pack()

    #Buttons
    colour='black'
    colour2='blue'
    clear=Button(btn_frame,text='Clear',fg=colour,bg=colour2,width=10,height=3,command=btn_clear).grid(row=0,column=0)
    divide=Button(btn_frame,text='/',fg=colour,width=10,bg='red',height=3,command=lambda:btn_clk("/")).grid(row=0,column=1)

    seven=Button(btn_frame,text='7',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(7)).grid(row=1,column=0)
    eight=Button(btn_frame,text='8',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(8)).grid(row=1,column=1)
    nine=Button(btn_frame,text='9',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(9)).grid(row=1,column=2)
    multiply=Button(btn_frame,text='*',fg=colour,width=10,height=3,bg='red',command=lambda:btn_clk("*")).grid(row=4,column=2)

    four=Button(btn_frame,text='4',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(4)).grid(row=2,column=0)
    five=Button(btn_frame,text='5',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(5)).grid(row=2,column=1)
    six=Button(btn_frame,text='6',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(6)).grid(row=2,column=2)
    minus=Button(btn_frame,text='-',fg=colour,width=10,height=3,bg='red',command=lambda:btn_clk("-")).grid(row=2,column=3)

    one=Button(btn_frame,text='1',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(1)).grid(row=3,column=0)
    two=Button(btn_frame,text='2',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(2)).grid(row=3,column=1)
    three=Button(btn_frame,text='3',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(3)).grid(row=3,column=2)
    plus=Button(btn_frame,text='+',fg=colour,width=10,height=3,bg='red',command=lambda:btn_clk("+")).grid(row=3,column=3)

    zero=Button(btn_frame,text='0',fg=colour,width=10,height=3,bg=colour2,command=lambda:btn_clk(0)).grid(row=4,column=0)
    point=Button(btn_frame,text='.',fg=colour,width=10,height=3,bg='red',command=lambda:btn_clk(".")).grid(row=4,column=1)
    equals=Button(btn_frame,text='=',fg=colour,width=10,height=3,bg='yellow',command=lambda:btn_equal()).grid(row=1,column=3)
    square=Button(btn_frame,text='x^2',fg=colour,width=10,height=3,bg='red',command=lambda:btn_sqr()).grid(row=4,column=3)
    divide_by_one=Button(btn_frame,text='1/x',fg=colour,width=10,height=3,bg='red',command=lambda:btn_div()).grid(row=0,column=2)
    square_root=Button(btn_frame,text='x^1/2',fg=colour,width=10,height=3,bg='red',command=lambda:btn_sqrt()).grid(row=0,column=3)
    percent=Button(btn_frame,text='%',fg=colour,width=10,height=3,bg='red',command=lambda:btn_clk("%")).grid(row=5,column=0)

    raise_to=Button(btn_frame,text='^',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk('^')).grid(row=0,column=4)
    log=Button(btn_frame,text='log(a,b)',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk('log(')).grid(row=1,column=4)
    starting_bracket=Button(btn_frame,text='(',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk('(')).grid(row=2,column=4)
    ending_bracket=Button(btn_frame,text=')',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk(')')).grid(row=3,column=4)
    char=Button(btn_frame,text=',',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk(',')).grid(row=4,column=4)
    pi=Button(btn_frame,text='pi',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk(3.14159265359)).grid(row=5,column=1)
    e=Button(btn_frame,text='e',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk(2.71828182846)).grid(row=5,column=2)
    exponent=Button(btn_frame,text='!',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk('!')).grid(row=5,column=3)
    hypo=Button(btn_frame,text='hypo(a,b)',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk('hypo(')).grid(row=5,column=4)

    sin=Button(btn_frame,text='sin()',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk('sin(')).grid(row=0,column=5)
    cos=Button(btn_frame,text='cos()',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk('cos(')).grid(row=1,column=5)
    tan=Button(btn_frame,text='tan()',fg=colour,width=10,height=3,bg='red', command=lambda:btn_clk('tan(')).grid(row=2,column=5)

    degree=Button(btn_frame,text='degree',fg=colour,width=10,height=3,bg='red', command=lambda:btn_degree()).grid(row=3,column=5)
    radians=Button(btn_frame,text='radians',fg=colour,width=10,height=3,bg='red', command=lambda:btn_radians()).grid(row=4,column=5)


    exit=Button(window,text='Exit',fg='white',bg='grey',width=20,height=3, command=window.destroy,relief='groove').pack(side=BOTTOM)

    window.mainloop()