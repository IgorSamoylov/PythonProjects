from tkinter import *
 
clicks = 0
 
 
def click_button():
    global clicks
    clicks += 1
    if e.get != "":
        w = int(e.get())
    else:
        w = 1
    btn1.config(text="Clicks "+format(clicks*w))
    if clicks%3 ==0 or clicks%4 ==0:
        btn1.pack(side=LEFT)
    if clicks%5 ==0:
        btn1.pack(side=RIGHT)
    if clicks%9 ==0:
        btn1.pack(side=BOTTOM)
    if clicks%2 ==0:
        btn1.pack(side=TOP)
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
l = Label(root, bg='black', fg='white', width=20)
e = Entry(root,width=20)
 
btn1 = Button(text="Clicks 0", background="#666", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn1.pack(side=TOP)
l.pack(side=TOP)
e.pack(side=BOTTOM)
 
root.mainloop()

