#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from  tkinter import *

def calculate(*args):
    try:
        ticket=float(tickets.get())
        value=v.get()
        if(ticket>=50):
            if(value=='160'):
                money.set(ticket*160.0*0.8)
            elif(value=='130'):
                money.set(ticket*130.0*0.8)
            elif(value=='60'):
                money.set(ticket*60.0*0.8)
        elif(ticket>=20 and ticket<50):
            if (value == '160'):
                money.set(ticket * 160.0 * 0.95)
            elif (value == '130'):
                money.set(ticket * 130.0 * 0.95)
            elif (value == '60'):
                money.set(ticket * 60.0 * 0.95)
        elif(ticket>0 and ticket<20):
            if (value == '160'):
                money.set(ticket * 160.0 )
            elif (value == '130'):
                money.set(ticket * 130.0 )
            elif (value == '60'):
                money.set(ticket * 60.0 )
    except ValueError:
        pass

root=Tk()
root.title("景点购票")
root.geometry('400x300')

v=StringVar()
v.set('160')
tickets = StringVar()
money = StringVar()

label1=Label(text="请选择景点").pack()
rd1=Radiobutton(root,text="东方明珠",value='160',variable=v).pack()
rd2=Radiobutton(root,text="野生动物园",value='130',variable=v).pack()
rd3=Radiobutton(root,text="科技馆",value='60',variable=v).pack()
label2=Label(root,text="请输入购票张数").pack()
entry=Entry(root,bd=5,textvariable=tickets).pack()
button1=Button(root,text="计算")
button1.bind('<Button-1>',calculate)
button1.pack()
label3=Label(root,text='票价为').pack()
label4=Label(root,textvariable=money).pack()
root.mainloop()
