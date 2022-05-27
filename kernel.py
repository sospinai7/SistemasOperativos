from signal import signal
from flask import Blueprint, render_template, request
from ctypes.wintypes import HLOCAL
from io import StringIO
from subprocess import call
import subprocess
import os, signal, datetime

kernel = Blueprint('kernel', __name__,
                        template_folder='templates',
                        static_folder='static')

@kernel.route('/')
def show():
    return render_template('app3.html')

def new_log(log):
    add_log = log
    with open('myfile.txt', 'a+') as fp:
        fp.write(add_log)
        fp.close()
        pass

@kernel.route('/open_app/<string:slug>/<int:number>', methods=['GET', 'POST'])
def open_app(slug, number=None):
    calc_is_open = False
    notepad_is_open = False
    paint_is_open = False
    
    if request.method == 'GET':
        time = datetime.datetime.now()
        if slug == "notepad":
            app_name = "notepad.exe"
            
            if number == 1:
                if notepad_is_open == False:
                    new_log("[{}/{}/{} - {}:{}:{}] open notepad\n".format(str(time.day), str(time.month), str(time.year), str(time.hour), str(time.minute), str(time.second)))
                    os.system('notepad.exe')
                    print("open notepaad")
                    notepad_is_open = True
            elif number == 2:
                new_log("[{}/{}/{} - {}:{}:{}] close notepad\n".format(str(time.day), str(time.month), str(time.year), str(time.hour), str(time.minute), str(time.second)))
                command = "taskkill /IM {} /F".format(str(app_name))
                os.system(command)
                print("close notepad")
                notepad_is_open = False
        elif slug == "calc":
            app_name = '"Calculator.exe"'
            if number == 1:
                if calc_is_open == False:
                    new_log("[{}/{}/{} - {}:{}:{}] open calc\n".format(str(time.day), str(time.month), str(time.year), str(time.hour), str(time.minute), str(time.second)))
                    os.system('calc.exe') 
                    print("open calc1")
                    calc_is_open = True
            elif number == 2:
                new_log("[{}/{}/{} - {}:{}:{}] close calc\n".format(str(time.day), str(time.month), str(time.year), str(time.hour), str(time.minute), str(time.second)))
                command = "taskkill /IM {} /F".format(str(app_name))
                os.system(command)
                print("close clac1")
                calc_is_open = False
        elif slug == "paint":
            app_name = '"mspaint.exe"'
            if number == 1:
                if paint_is_open == False:
                    new_log("[{}/{}/{} - {}:{}:{}] open paint\n".format(str(time.day), str(time.month), str(time.year), str(time.hour), str(time.minute), str(time.second)))
                    call(['mspaint']) 
                    print("open paint")
                    paint_is_open = True
            elif number == 2:
                new_log("[{}/{}/{} - {}:{}:{}] close paint\n".format(str(time.day), str(time.month), str(time.year), str(time.hour), str(time.minute), str(time.second)))
                command = "taskkill /IM {} /F".format(str(app_name))
                os.system(command)
                print("close paint")
                paint_is_open = False

        return render_template('index.html')

    return render_template('index.html')