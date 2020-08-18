from tkinter import *


def enter_num(x):
    if entry.get() == '0':
        if x == '.':
            entry.insert(1, '.')
        else:
            entry.delete(0, 'end')
            entry.insert(0, str(x))
    else:
        content = entry.get()
        if content[-1] == '.' and x == '.':
            pass
        else:
            leng = len(entry.get())
            entry.insert(leng, str(x))


def enter_op(x):
    if entry.get() != '0':
        leng = len(entry.get())
        allchar = entry.get()
        last = allchar[-1]
        if last in ['+', '-', '/'] or allchar[-2:] == '**':
            pass
        else:
            entry.insert(leng, btn_op[x]['text'])


def fnclear():
    entry.delete(0, 'end')
    entry.insert(0, '0')


history = []


def fn():
    content = entry.get()
    result = eval(content)
    entry.delete(0, END)
    entry.insert(0, result)
    history.append(content)
    history.reverse()
    status.configure(text='History :' + '|'.join(history[:4]))


def del_it():
    leng = len(entry.get())
    entry.delete(leng-1, END)
    if leng == 1:
        entry.insert(0, '0')


root = Tk()
root.title('Calculator')
root.geometry("380x500+350+100")
root.resizable(False, False)

# taking entry
entry = Entry(root, font="verdana 14 bold", width=27, bd=4, justify=RIGHT)
entry.insert(0, '0')
entry.place(x=30, y=10)

# number buttons

btn_list = []
for i in range(1, 10):
    btn_list.append(Button(root, text=str(i), width=4, bd=10, command=lambda x=i: enter_num(x)))
k = 0
for i in range(0, 3):
    for j in range(0, 3):
        btn_list[k].place(x=30+j*90, y=70+i*70)
        k += 1

btn_zero = Button(root, text='0', width=27, bd=10, command=lambda x=0: enter_num(x))
btn_zero.place(x=25, y=280)

btn_clear = Button(root, text='C', width=4, bd=10, command=fnclear)
btn_clear.place(x=25, y=340)


# operator buttons

btn_op = []
for i in range(4):
    btn_op.append(Button(root, width=4, bd=10, command=lambda x=i: enter_op(x)))

btn_op[0]['text'] = '+'
btn_op[1]['text'] = '-'
btn_op[2]['text'] = '*'
btn_op[3]['text'] = '/'


for i in range(0, 4):
    btn_op[i].place(x=290, y=70+i*70)


btn_dot = Button(root, text='.', width=4, bd=10, command=lambda x='.': enter_num(x))
btn_dot.place(x=110, y=340)

btn_equal = Button(root, text='=', width=4, bd=10, command=fn)
btn_equal.place(x=200, y=340)

btn_del = Button(root, text='del', width=4, bd=10, command=del_it)
btn_del .place(x=290, y=340)


status = Label(root, text='History :', height=3, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
