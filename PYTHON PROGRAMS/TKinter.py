from tkinter import *

root = Tk()

ent = Entry(root, width=200)
but = Button(root, text="Преобразовать")
lab = Label(root, bg='black', fg='white', width=200)


def str_to_sort_list(event):
    s = ent.get()
    s = s.split()
    s.sort()
    lab['text'] = ' '.join(s)
 
 
but.bind('<Button-1>', str_to_sort_list)


ent.pack()
but.pack()
lab.pack()
root.mainloop()
