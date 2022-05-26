from signal import signal
from flask import Blueprint, render_template, request
from ctypes.wintypes import HLOCAL
from io import StringIO
from subprocess import call
import subprocess
import os, signal

kernel = Blueprint('kernel', __name__,
                        template_folder='templates',
                        static_folder='static')

@kernel.route('/')
def show():
    return render_template('app3.html')


@kernel.route('/open_app/<string:slug>/<int:number>', methods=['GET', 'POST'])
def open_app(slug, number=None):
    if request.method == 'GET':
        if slug == "notepad":
            app_name = "notepad.exe"
            if number == 1:
                os.system('notepad.exe')
                print("open notepaad")
            elif number == 2:
                command = "taskkill /IM {} /F".format(str(app_name))
                os.system(command)
                print("close notepad")
        elif slug == "calc":
            app_name = '"Calculator.exe"'
            if number == 1:
                os.system('calc.exe') 
                print("open calc1")
            elif number == 2:
                command = "taskkill /IM {} /F".format(str(app_name))
                os.system(command)
                print("close clac1")
        elif slug == "paint":
            app_name = '"mspaint.exe"'
            if number == 1:
                call(['mspaint']) 
                print("open paint")
            elif number == 2:
                command = "taskkill /IM {} /F".format(str(app_name))
                os.system(command)
                print("close paint")

        return render_template('index.html')

    return render_template('index.html')