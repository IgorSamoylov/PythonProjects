from flask import Flask, render_template, redirect, url_for, request
import threading

server_app = Flask(__name__, template_folder="templates")

thread_pool = []

css_style = """ style="font-family: sans-serif; font-size: larger; font-weight: bold; color: aqua; bottom: -50%;" """
link = """ <a href="/clock"> Посмотреть часы </a> """
#file_clock = open("C:/Users/A12/Desktop/resourses/clock.html", "r")
#clock_html = file_clock.read()
#file_clock.close()


@server_app.route("/")
def balancer():
    task = Task(len(thread_pool))
    task.start()
    thread_pool.append(task)
    return task.get_result()

@server_app.route("/clock")
def clock_show():
    return render_template("clock.html")
    
    


class Task(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        
        self.number = number

    def run(self):
        thread_id = threading.get_ident()
        self.result = "<p" + css_style + f">Hello, World! Thread: {thread_id} </p>" + link  

    def get_result(self):
        return self.result


if __name__ == '__main__':
    server_app.run(port=8888, host='127.0.0.1')
