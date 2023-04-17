from tkinter import *

def btnp(number):

    global eqtt

    eqtt = eqtt + str(number)

    eql.set(eqtt)

def clear():

    global eqtt

    eql.set("")

    eqtt = ""

def equals():

    global eqtt

    try:
        total = str(eval(eqtt))

        eql.set(total)

        eqtt = total

    except SyntaxError:
        eql.set("Syntax Error")

        eqtt = total

    except ZeroDivisionError:
        eql.set("Arithmetic Error")

        eqtt = ""

frame = Tk()
frame.geometry('600x600')
frame.title('Calculator')

eqtt = ""

eql = StringVar()

lbl = Label(frame, textvariable= eql ,height= 5, width= 20, bg= 'white')
lbl.pack()

root = Frame(frame)
root.pack()

btn1 = Button(root, text='1', height= 5, width= 10, command= lambda: btnp(1))
btn1.grid(row= 0, column= 0)

btn2 = Button(root, text='2', height= 5, width= 10, command= lambda: btnp(2))
btn2.grid(row= 0, column= 1)

btn3 = Button(root, text='3', height= 5, width= 10, command= lambda: btnp(3))
btn3.grid(row= 0, column= 2)

btn4 = Button(root, text='4', height= 5, width= 10, command= lambda: btnp(4))
btn4.grid(row= 1, column= 0)

btn5 = Button(root, text='5', height= 5, width= 10, command= lambda: btnp(5))
btn5.grid(row= 1, column= 1)

btn6 = Button(root, text='6', height= 5, width= 10, command= lambda: btnp(6))
btn6.grid(row= 1, column= 2)

btn7 = Button(root, text='7', height= 5, width= 10, command= lambda: btnp(7))
btn7.grid(row= 2, column= 0)

btn8 = Button(root, text='8', height= 5, width= 10, command= lambda: btnp(8))
btn8.grid(row= 2, column= 1)

btn9 = Button(root, text='9', height= 5, width= 10, command= lambda: btnp(9))
btn9.grid(row= 2, column= 2)

btn0 = Button(root, text='0', height= 5, width= 10, command= lambda: btnp(0))
btn0.grid(row= 3, column= 1)

btnadd = Button(root, text='+', height= 5, width= 10, command= lambda: btnp('+'))
btnadd.grid(row= 0, column= 3)

btnminus = Button(root, text='-', height= 5, width= 10, command= lambda: btnp('-'))
btnminus.grid(row= 1, column= 3)

btntimes = Button(root, text='*', height= 5, width= 10, command= lambda: btnp('*'))
btntimes.grid(row= 2, column= 3)

btndvd = Button(root, text='/', height= 5, width= 10, command= lambda: btnp('/'))
btndvd.grid(row= 3, column= 3)

btnclear = Button(root, text='Clear', height= 5, width= 10, command= clear)
btnclear.grid(row= 3, column= 2)

btnequal = Button(root, text='=', height= 5, width= 10, command= equals)
btnequal.grid(row= 4, column= 3)

btndot = Button(root, text='.', height= 5, width= 10, command= lambda: btnp('.'))
btndot.grid(row= 3, column= 0)

frame.mainloop()