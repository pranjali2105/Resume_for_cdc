import tkinter
import math
from tkinter import *
first_number=second_number=operator=None
def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)
def clear():
    result_label.config(text='')
def get_operator(op):
    global first_number,operator
    first_number=float(result_label['text'])
    operator=op
    result_label.config(text='')
def get_result():
    global first_number,second_number,operator
    second_number= float(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number/second_number)))
def negate():
    res=float(result_label['text'])
    result_label.config(text=str(-res))
def expo():
    res=float(result_label['text'])
    result_label.config(text=str(round(math.exp(res),5)))
def lne():
    res=float(result_label['text'])
    result_label.config(text=str(round(math.log(res),5)))
def dele():
    res=float(result_label['text'])
    result_label.config(text=str(int(res//10)))
def inverse():
    res=float(result_label['text'])
    result_label.config(text=str(float(1/res)))
def square():
    res=float(result_label['text'])
    result_label.config(text=str(int(res**2)))
def sq_root():
    res=float(result_label['text'])
    if res<0:
        result_label.config(text='Error')
    else:
        result_label.config(text=str(round(math.sqrt(res),5)))
def deci():
    current = result_label['text']
    if '.' not in current:
        result_label.config(text=current + '.')
root = Tk()  # Make sure this is the only Tk() instance
root.title("Calculator")  # Set title AFTER creating root, BEFORE mainloop
root.geometry("280x500")
root.resizable(False, False)
root.configure(background="#2d1903")

class MyLabel(tkinter.Label):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(master, text=text, **kwargs)
        self.pack()
result_label = MyLabel(root,text='',bg="#2d1903",fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))
btn7 = Button(root,text='7',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=3,column=0)
btn7.config(font=('verdana',14))
btnexp = Button(root,text='exp',bg='#664436',fg='white',width=5,height=2,command=lambda:expo())
btnexp.grid(row=1,column=0)
btnexp.config(font=('verdana',14))
btnln = Button(root,text='ln',bg='#664436',fg='white',width=5,height=2,command=lambda:lne())
btnln.grid(row=1,column=1)
btnln.config(font=('verdana',14))
btndel = Button(root,text='del',bg='#664436',fg='white',width=5,height=2,command=lambda:dele())
btndel.grid(row=1,column=3)
btndel.config(font=('verdana',14))
btnin = Button(root,text='1/x',bg='#664436',fg='white',width=5,height=2,command=lambda:inverse())
btnin.grid(row=2,column=0)
btnin.config(font=('verdana',14))
btnsq = Button(root,text='x^2',bg='#664436',fg='white',width=5,height=2,command=lambda:square())
btnsq.grid(row=2,column=1)
btnsq.config(font=('verdana',14))
btnroot = Button(root,text='root',bg='#664436',fg='white',width=5,height=2,command=lambda:sq_root())
btnroot.grid(row=2,column=2)
btnroot.config(font=('verdana',14))

btn8 = Button(root,text='8',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=3,column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=3,column=2)
btn9.config(font=('verdana',14))

btnp = Button(root,text='+',bg='#664436',fg='white',width=5,height=2,command=lambda:get_operator('+'))
btnp.grid(row=5,column=3)
btnp.config(font=('verdana',14))
btnneg = Button(root,text='+/-',bg='#664436',fg='white',width=5,height=2,command=lambda:negate())
btnneg.grid(row=6,column=0)
btnneg.config(font=('verdana',14))

btndec = Button(root,text='.',bg='#664436',fg='white',width=5,height=2,command=lambda:deci())
btndec.grid(row=6,column=1)
btndec.config(font=('verdana',14))


btn4 = Button(root,text='4',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=4,column=0)
btn4.config(font=('verdana',14))


btn5 = Button(root,text='5',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=4,column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=4,column=2)
btn6.config(font=('verdana',14))

btnm = Button(root,text='-',bg='#664436',fg='white',width=5,height=2,command=lambda:get_operator('-'))
btnm.grid(row=4,column=3)
btnm.config(font=('verdana',14))

btn1 = Button(root,text='1',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=5,column=0)
btn1.config(font=('verdana',14))
btn2 = Button(root,text='2',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=5,column=1)
btn2.config(font=('verdana',14))
btn3 = Button(root,text='3',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=5,column=2)
btn3.config(font=('verdana',14))
btnu = Button(root,text='*',bg='#664436',fg='white',width=5,height=2,command=lambda:get_operator('*'))
btnu.grid(row=3,column=3)
btnu.config(font=('verdana',14))
btn0 = Button(root,text='0',bg='#664436',fg='white',width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=6,column=2)
btn0.config(font=('verdana',14))
btnc = Button(root,text='C',bg='#664436',fg='white',width=5,height=2,command=lambda:clear())
btnc.grid(row=1,column=2)
btnc.config(font=('verdana',14))
btne = Button(root,text='=',bg='#664436',fg='white',width=5,height=2,command=get_result)
btne.grid(row=6,column=3)
btne.config(font=('verdana',14))
btns= Button(root,text='/',bg='#664436',fg='white',width=5,height=2,command=lambda:get_operator('/'))
btns.grid(row=2,column=3)
btns.config(font=('verdana',14))
root.mainloop()