from tkinter import *

root = Tk()
root.title("Методы виджетов")
root.minsize(width=500, height=400)

# Виджет входа
e1 = Entry(root)
e1.pack(expand = 1, fill = BOTH)

# Виджет кнопки, который в данный момент имеет фокус
e2 = Button(root, text ="Button")

# здесь метод focus_set () используется для установки фокуса
e2.focus_set()
e2.pack(pady = 5)
root.mainloop()
