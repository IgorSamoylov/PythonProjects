
from tkinter import Tk, ttk, filedialog, Frame
from tkinter.messagebox import showinfo
from IMAGE_CONVERTER import ImageConverter

root = Tk()
root.title("IMAGE CONVERTER")
root.geometry("560x100+300+300")
root.resizable(False, False)

frame = Frame(root, bg="black")
frame.grid()

def select_file():
    filetypes =(("webp", "*.webp"), ("All files", "*.*"))
    
    filename = filedialog.askopenfilename(
        title="Open a file",
        initialdir='/',
        filetypes=filetypes)
    
    showinfo(
        title='Selected File',
        message=filename
    )
    ImageConverter.convert_file(filename) 


def select_directory():
    dir_name = filedialog.askdirectory(
        title="Open directory",
        initialdir="C:/Users/A12/Downloads/PICTURES"
        )
    ImageConverter.convert_dir(dir_name, dir_name)
    

open_button1 = ttk.Button(root, text="Open a File", command=select_file)
open_button1.configure(width=30)
open_button1.grid(column=0, row=1, sticky='w', padx=15, pady=15)

open_button2 = ttk.Button(root, text="Open Directory", command=select_directory)
open_button2.configure(width=30)
open_button2.grid(column=1, row=1, sticky='e', padx=15, pady=15)


root.mainloop()
