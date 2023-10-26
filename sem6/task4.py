

from tkinter import *
from tkinter import ttk


def opposite_color():
    try:
        hexi = str(entryColor.get())
    except ValueError:
        pass
    A = []
    opposite = []
    for i in range(3):
        t = int(hexi[1 + 2 * i] + hexi[2 + 2 * i], base=16)
        A.append(255 - t)
        if A[i] <= 15:
            opposite.append('0' + hex(A[i])[:0] + hex(A[i])[2:])
        else:
            opposite.append(hex(A[i])[:0] + hex(A[i])[2:])
        Opposite = ''.join(opposite)
        Opposite = "#" + Opposite
    labelColor["background"] = hexi
    labelColor["foreground"] = hexi
    labelOpposite["background"] = Opposite
    labelOpposite["foreground"] = Opposite
    labelOppositeName["text"] = Opposite



root = Tk()
root.title('Генератор цветов')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
labelColor = Label(root, bg='white')
labelColor.place(relx=0.45, rely=0.3, anchor=E, width=150, height=130)

labelOpposite = Label(root, bg='white')
labelOpposite.place(relx=0.55, rely=0.3, anchor=W, width=150, height=130)

entryColor = Entry(root, borderwidth=4)
entryColor.place(relx=0.45, rely=0.5, anchor=E, width=150, height=30)



btnGenerate = Button(root, text='Сгенерировать', font='Arial 13 bold', borderwidth=4, command=opposite_color)
btnGenerate.place(relx=0.5, rely=0.8, anchor=CENTER, width=150, height=60)


labelOppositeName = Label(root)
labelOppositeName.place(relx=0.55, rely=0.5, anchor=W, width=150, height=30)
root.mainloop()