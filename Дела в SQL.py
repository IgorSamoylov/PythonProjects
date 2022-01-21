import time
import sqlite3
from tkinter import *

path = "C:/Users/A12/Desktop/SQL/Programs/work.db"
conn = sqlite3.Connection(path)
cursor = conn.cursor()


# 1. Создаем главное окно root, устнавливаем заголовок и размер
root = Tk()
root.title('Текущие дела')
#root.geometry("410x450")

# 2. Создаем объекты виджетов для root, которые будут размещены далее
entry = Entry(root, width=50)
label = Label(root, width=50, bg='black',\
              fg='lightblue', font=('Arial', 15), justify=LEFT) # Выравнивание текста по левому краю
button = Button(root, text='Выполнить SQL', width=15, font=('Impact',11))
buttonT = Button(root, text='>>>', width=5) 
list_tables = Listbox(root, width=20, font=('Arial', 13))
# Устанавливаем возможность выбора только одной записи в list_box 
list_tables.selectmode=SINGLE

#scrollbar = Scrollbar(list_tables)


# Используем менеджер геометрии grid для позиционирования элементов
# sticky - "приклеить" или "растянуть" по "сторонам света",
# padx, pady - отступы по горизонтали и вертикали
list_tables.grid(row=0,column=0, sticky=W+N+S, padx=10, pady=10)
entry.grid(row=1, column=0, padx=10)
buttonT.grid(row=0, column=0, sticky=E, padx=10)
label.grid(row=0, column=2, padx=10, pady=10)
button.grid(row=1, column=2, sticky=W+E, padx=10, pady=10)
#scrollbar.grid(row=0, column=2)


all_tables_list = []
current_table = 0


def show_tables():
    # Таким SQL запросом можно получить список всех таблиц в БД
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")

    # Очищаем список всех таблиц и заносим новый
    all_tables_list.clear()
    for table in cursor.fetchall():
        all_tables_list.append(table[0])
        
    # Удаляем все записи в listbox
    list_tables.delete(0, 100)
    
    # Заполняем listbox
    for index, table in enumerate(all_tables_list):
        list_tables.insert(index, table)


def show_database(table):
    """Получает все данные из таблицы в виде кортежей и выводит их по строкам в label"""
    db_entry = [entry_tuple for entry_tuple in cursor.execute(f"SELECT * FROM {table}")]
    db_in_string = ''
    for entry_tuple in db_entry:
        db_in_string += str(entry_tuple) + '\n'
        
    label['text'] = db_in_string


def select_database(event):
    # Функция curselection возвращает кортеж, содержащий индексы выбранных записей в listbox
    selection = list_tables.curselection()
    if not selection:
        selection = (0,)
        
    global current_table
    current_table = selection[0]
    show_database(all_tables_list[current_table])

    

def execute_sql():
    """Выполняет SQL запрос и обновляет отображение БД в label"""
    inp = entry.get()
    try:
        cursor.execute(inp)
    except sqlite3.DatabaseError as err:
        label['text'] = 'ERROR!'
        #time.sleep(2)
    else:
        conn.commit() # Не забыть commit транзакцию или установить autocommit!

    show_tables()
    show_database(all_tables_list[current_table])
    

# Логика первичного запуска
show_tables()
show_database(all_tables_list[current_table])

# Так можно забиндить функцию на нажатие button,
# первым значением всегда передается строка <Button-1> - именно так написанное имя кнопки  
button.bind('<Button-1>', execute_sql) 
buttonT.bind('<Button-1>', select_database)

# Так биндится нажатие Enter для поля ввода entry с использованием лямбды
entry.bind('<Return>', (lambda event: execute_sql()))


# Импортируем виджет всплывающего окна message
from tkinter import messagebox  
def on_closing():
    if messagebox.askokcancel("Выход", "Вы уверены что хотите выйти?"): # Работаем с месседж-боксом
        conn.close() # Закрываем соединение с БД
        root.destroy() # Уничтожаем главное окно
        
# Прикрепляем к крестику закрытия окна windows по протокол-handeler нашу функцию on_closing()
root.protocol("WM_DELETE_WINDOW", on_closing)

# 4.Запускаем главный луп
root.mainloop()





