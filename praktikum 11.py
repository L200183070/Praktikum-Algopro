## Activity 1
from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Personal Data')

L1 = Label(my_app, text = 'Personal Data' , font = ('Arial' , 24))
L1.grid(row=0 , column=0)


L2 = Label(my_app, text = 'Name')
L2.grid(row=1 , column=0)
str2 = StringVar(value='Aulia S.R Nurcahyani')
E2 = Entry (my_app, textvariable=str2)
E2.grid(row=1 , column=1)

L3 = Label(my_app , text = 'NIM')
L3.grid(row=2 , column=0)
str3 = StringVar(value='L200183070')
E3 = Entry(my_app, textvariable=str3)
E3.grid(row=2 , column=1)

L4 = Label(my_app, text = 'Favourite Book')
L4.grid(row=3 , column=0)
str4 = StringVar(value='Spring in London')
E4 = Entry(my_app, textvariable=str4)
E4.grid(row=3, column=1)

L5 = Label(my_app , text = 'Idol among Friends')
L5.grid(row=4 , column=0)
str5 = StringVar(value='Umar bin Khattab')
E5 = Entry(my_app, textvariable=str5)
E5.grid(row=4 , column=1)

L6 = Label(my_app , text = 'Motto')
L6.grid(row=5 , column=0)
str6 = StringVar(value='When Autumn Breeze Come We Will Meet Again')
E6 = Entry(my_app, textvariable=str6)
E6.grid(row=5 , column=1)


def close():
    my_app.destroy()

B = Button(my_app.quit(), text = 'close' , command = close )
B.grid(row=6 , column=1)

my_app.mainloop()


## activity 2
##
##from Tkinter import Tk, Label, Entry, Button, StringVar
##from Tkinter import LEFT, RIGHT
##
##
##my_app = Tk(className = 'Calculator')
##
##L1 = Label(my_app, text='first number')
##L1.grid(row=0 , column=0 )
##str1 = StringVar()
##E1 = Entry (my_app, textvariable=str1)
##E1.grid(row=0 , column=1 , columnspan=3)
##L2 = Label(my_app , text = 'second number')
##L2.grid(row=1 , column=0)
##str2 = StringVar()
##E2 = Entry(my_app , textvariable=str2)
##E2.grid(row=1 , column=1 , columnspan=3)
##L3 = Label(my_app , text = 'result')
##L3.grid(row=4 , column=0)
##L4 = Label(my_app, text='0')
##L4.grid(row=4 , column=1)
##
##def plus ():
##    a = float (str1.get())
##    b = float (str2.get())
##    hasil = a+b
##    L4.config(text=hasil)
##
##def minus ():
##    c = float (str1.get())
##    d = float (str2.get())
##    hasil = c-d
##    L4.config(text=hasil)
##
##def times ():
##    e = float(str1.get())
##    f = float (str2.get())
##    hasil = e*f
##    L4.config(text=hasil)
##    
##def devide ():
##    g = float (str1.get())
##    h = float (str2.get())
##    hasil = g/h
##    L4.config(text=hasil)
##
##B1 = Button (my_app , text = '+' , command = plus)
##B1.grid(row=3 , column=0)
##B2 = Button (my_app, text= '-' , command = minus)
##B2.grid(row=3 , column=1)
##
##B3 = Button (my_app , text = 'x' , command = times)
##B3.grid(row=3 , column=2)
##B4 = Button (my_app, text= ':' , command = devide)
##B4.grid(row=3 , column=3)
##
##my_app.mainloop()
##

    
