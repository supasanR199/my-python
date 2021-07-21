from tkinter import *
def butClick():
    hight_1   =   float(hight.get())
    weight_1   =  float(weight.get())
    result  =   weight_1/(hight_1*hight_1)
    # txt_spac1    =   Label(window,text   =   '\t').grid(row=6,column=1)
    txt_result  =   Label(window,text='').grid(row=6,column=1)
    txt_result  =   Label(window,text=result).grid(row=6,column=1)
    lavel_bmi(result)
def lavel_bmi(result_bmi):
    if  result_bmi  <= 18.5:
        tex_status  =   Label(window,text='').grid(row=7,column=1)
        tex_status  =   Label(window,text='Underweight',width=10).grid(row=7,column=1)
    elif    result_bmi >=   18.6    and result_bmi  <=  24.0:
        tex_status  =   Label(window,text='').grid(row=7,column=1)
        tex_status  =   Label(window,text='Normal',bg='green',width=10).grid(row=7,column=1)
    elif    result_bmi  >=  24.1    and result_bmi  <=  29.9:
        tex_status  =   Label(window,text='').grid(row=7,column=1)
        tex_status  =   Label(window,text='Overwieght',bg='yellow',width=10).grid(row=7,column=1)
    elif    result_bmi  >=  30:
        tex_status  =   Label(window,text='').grid(row=7,column=1)
        tex_status  =   Label(window,text='Obese',bg='red',width=10).grid(row=7,column=1)
window = Tk()
window.geometry('300x230')
window.title('Body-Mass Index(bmi)')
weight  =   StringVar()
hight   =   StringVar()
txt_spac    =   Label(window,text   =   '').grid(row=0,column=0)
txt_weight   =   Label(window,text = 'Weight').grid(row=1,column=0)
txt_hight   =   Label(window,text = 'Hight').grid(row=2,column=0)
ent_weight   =   Entry(window,width=20,textvariable=weight).grid(row=1,column=1)
ent_hight   =   Entry(window,width=20,textvariable=hight).grid(row=2,column=1)
but_cal =   Button(window,width=10,text='cal',command=butClick).grid(row=4,column=1)
txt_cal =   Label(window,text='Display').grid(row=5,column=0)
txt_bmi =   Label(window,text='\tBMI =').grid(row=6,column=0)
txt_status =   Label(window,text='\tStatus =').grid(row=7,column=0)
txt_result  =   Label(window,text='N/A').grid(row=6,column=1)
tex_status  =   Label(window,text='N/A').grid(row=7,column=1)
window.mainloop()