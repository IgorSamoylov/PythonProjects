
from flask import Flask # Импортируем класс Flask
from flask import render_template

app = Flask(__name__) # Создаем объект класса Flask

@app.route('/') # Декорируем функцию методом из класса Flask.route
@app.route('/<name>') #Любой URL-запрос после / идет в переменную name
def hello(name=None):
    return render_template('HelloPage.html', name=name) #Рендер html-шаблона посредством Jinja2

@app.route('/name')
def hello_name():
    return "<p>Hello Igor!</p>"

@app.route('/auth')
def auth():
    return "<p>Enter Login!</p>"

app.debug = True
app.run() # Запускаем сервер вызовом метода объекта app Flask.run
