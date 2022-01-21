from tkinter import *
 
languages = ["Python", "Java", "JavaScript", "C#", "C/C++", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]
 
root = Tk()
root.title("GUI на Python")
 
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
 
languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=40)
 
for language in languages:
    languages_listbox.insert(END, language)
 
languages_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=languages_listbox.yview)
 
root.mainloop()
