

def make_strong(func):
    def wrapper(word): # Аргументы исходной функции передаются во вложенную (замыкание!)
        return "<strong>" + func(word) + "</strong>" # wrapper вызывает переданную функцию
    return wrapper                               # и изменяет её результат

def make_emphasis(func):
    def wrapper(word):
        return "<em>" + func(word) + "</em>"
    return wrapper                  # wrapper возвращается внешней функцией как объект
                                    # и подставляется вместо декорируемой функции

@make_strong
@make_emphasis
def return_html(word):
    return "Hello" + word + "!"

print(return_html("world"))

    
# @-декоратор аналогичен следующему вызову:
decorator = make_strong(make_emphasis(return_html)) #здесь нет вызова return_html, идет работа с самим объектом функции
print(decorator("world")) # а здесь осуществляется вызов, но уже объекта-функции "decorator"



"""

from flask import Flask
app = Flask(__name__, template_folder="templates")

@app.route("/")
def server():
    return return_html()

app.run(port=8888, host='127.0.0.1')

"""
