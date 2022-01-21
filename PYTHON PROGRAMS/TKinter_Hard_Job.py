from tkinter import *
import math

def hard_job():
    x = 100000
    while True:
        x = math.log(x) ** 2.8
        root.update()
        print(x)
        break

root = Tk()
root.title("Методы виджетов")
root.minsize(width=500, height=400)

button = Button(text="Обновить", command = hard_job)
button.pack()
root.after(500, hard_job)
root.mainloop()
