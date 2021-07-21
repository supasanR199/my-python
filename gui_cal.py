from tkinter import *
window  =   Tk()
window.title('Calculater')
text_in =   StringVar()
ent_cal =   Entry(window,textvar=text_in)
def but_click(number):
    current =   ent_cal.get()
    ent_cal.delete(0,END)
    ent_cal.insert(0,str(current)+str(number))
def clr_click():
    ent_cal.delete(0,END)
def add_click():
    first_number  =   ent_cal.get()
    global  first_num
    global  math
    math    =   0
    first_num   =   int(first_number)
    ent_cal.delete(0,END)
def subtra_click():
    first_number  =   ent_cal.get()
    global  first_num
    global  math
    math    =   1
    first_num   =   int(first_number)
    ent_cal.delete(0,END)
def mutip_click():
    first_number  =   ent_cal.get()
    global  first_num
    global  math
    math    =   2
    first_num   =   int(first_number)
    ent_cal.delete(0,END)
def divi_click():
    first_number  =   ent_cal.get()
    global  first_num
    global  math
    math    =   3
    first_num   =   int(first_number)
    ent_cal.delete(0,END)
def equle_click():
    secone_number   =   ent_cal.get()
    ent_cal.delete(0,END)
    if  math    ==   0:
        ent_cal.insert(0,first_num+int(secone_number))
    elif    math    ==  1:
        ent_cal.insert(0,first_num-int(secone_number))
    elif    math    ==  2:
        ent_cal.insert(0,first_num*int(secone_number))
    elif    math    ==  3:
        if  int(secone_number)   ==  0:
            ent_cal.insert(0,"ERROR")
        else:
            ent_cal.insert(0,first_num/int(secone_number))
            
ent_cal.grid(row=0,column=0,columnspan=3)
but_1   =   Button(window,text='1',command=lambda:but_click(1))
but_2   =   Button(window,text='2',command=lambda:but_click(2))
but_3   =   Button(window,text='3',command=lambda:but_click(3))
but_4   =   Button(window,text='4',command=lambda:but_click(4))
but_5   =   Button(window,text='5',command=lambda:but_click(5))
but_6   =   Button(window,text='6',command=lambda:but_click(6))
but_7   =   Button(window,text='7',command=lambda:but_click(7))
but_8   =   Button(window,text='8',command=lambda:but_click(8))
but_9   =   Button(window,text='9',command=lambda:but_click(9))
but_0   =   Button(window,text='0',command=lambda:but_click(0))
but_equle   =   Button(window,text='=',command=equle_click)
but_add =   Button(window,text='+',command=add_click)
but_subtra  =   Button(window,text='-',command=subtra_click)
but_mutip   =   Button(window,text='x',command=mutip_click)
but_divi    =   Button(window,text='/',command=divi_click)
but_clr =   Button(window,text='clr',command=clr_click)
but_1.grid(row=1,column=0)
but_2.grid(row=1,column=1)
but_3.grid(row=1,column=2)
but_4.grid(row=2,column=0)
but_5.grid(row=2,column=1)
but_6.grid(row=2,column=2)
but_7.grid(row=3,column=0)
but_8.grid(row=3,column=1)
but_9.grid(row=3,column=2)
but_0.grid(row=4,column=0)
but_equle.grid(row=5,column=2)
but_add.grid(row=4,column=1)
but_subtra.grid(row=4,column=2)
but_mutip.grid(row=5,column=0)
but_divi.grid(row=5,column=1)
but_clr.grid(row=6,column=0)
window.mainloop()