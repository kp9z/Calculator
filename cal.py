from tkinter import *

root = Tk()
root.title('My Calculator')
e = Entry(root,width=13,justify=RIGHT,font="Helvetica 32")
e.insert(0,0)
e.grid(row=1,column=1,columnspan=4,ipady=3)
button_click = 0

def button_num(x):
    old_value=e.get()
    if old_value == '0':
        old_value = ''
    e.delete(0,END)
    new_value= str(old_value)+str(x)
    e.insert(0,new_value)
    
def button_clear():
    e.delete(0,END)
    e.insert(0,0)

def button_divide():
    global math
    global first_value
    global button_click
    # if button_click == 2:
    #     math="divide"
    #     button_equal()
    # else:
    first_value = e.get()
    math="divide" 
    button_clear()  

def button_multiply():
    global math
    global first_value
    first_value = e.get()
    math="multiply"
    button_clear()
def button_subtract():
    global math
    global first_value
    first_value = e.get()
    math="subtract"
    button_clear()
def button_add():
    global math
    global first_value
    first_value = e.get()
    math="add"
    button_clear()

def button_equal():
    global math
    global first_value
    # global button_click
    first_value = float(first_value)
    second_value= float(e.get())
    e.delete(0,END)
    if math=='divide':
        e.insert(0,first_value / second_value )
    if math=='multiply':
        e.insert(0,first_value * second_value )
    if math=='subtract':
        e.insert(0,first_value - second_value )
    if math=='add':
        e.insert(0,first_value + second_value )
    # button_click=0

Button(root,text="Clear",width=17,height=2,command=button_clear).grid(row=2,column=1,columnspan=3)

Button(root,text="1",width=2,height=2,command=lambda :button_num(1)).grid(row=5,column=1)
Button(root,text="2",width=2,height=2,command=lambda :button_num(2)).grid(row=5,column=2)
Button(root,text="3",width=2,height=2,command=lambda :button_num(3)).grid(row=5,column=3)
Button(root,text="4",width=2,height=2,command=lambda :button_num(4)).grid(row=4,column=1)
Button(root,text="5",width=2,height=2,command=lambda :button_num(5)).grid(row=4,column=2)
Button(root,text="6",width=2,height=2,command=lambda :button_num(6)).grid(row=4,column=3)
Button(root,text="7",width=2,height=2,command=lambda :button_num(7)).grid(row=3,column=1,padx=3)
Button(root,text="8",width=2,height=2,command=lambda :button_num(8)).grid(row=3,column=2,padx=3)
Button(root,text="9",width=2,height=2,command=lambda :button_num(9)).grid(row=3,column=3,padx=3)
Button(root,text="0",width=10,height=2,command=lambda :button_num(0)).grid(row=6,column=1,padx=3,columnspan=2)
Button(root,text=".",width=2,height=2,command=lambda :button_num(".")).grid(row=6,column=3,padx=3)

Button(root,text="/",width=2,height=2,command=button_divide).grid(row=2,column=4)
Button(root,text="X",width=2,height=2,command=button_multiply).grid(row=3,column=4)
Button(root,text="-",width=2,height=2,command=button_subtract).grid(row=4,column=4)
Button(root,text="+",width=2,height=2,command=button_add).grid(row=5,column=4)
Button(root,text="=",width=2,height=2,command=button_equal).grid(row=6,column=4)


root.mainloop()