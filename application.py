from flask import Blueprint, render_template, abort, request
import os, datetime, time
import random
from subprocess import call

application = Blueprint('application', __name__,
                        template_folder='templates',
                        static_folder='static')

@application.route('/')
def show():
    return render_template('index.html')

@application.route('/application/controller/<string:app>/<string:state>', methods=['GET', 'POST'])
def controller(app, state):

    timer = datetime.datetime.now()
    msg_res = response(app, state)

    if request.method == 'GET':
        if app == 'calc':
            if msg_res <= 5:
                calculator(state, app)
            elif msg_res > 5 and msg_res != 10:
                print('esperar 3 sgundos')
                time.sleep(3)
                calculator(state, app)
            elif msg_res == 10:
                print('ERROR')
        elif app == 'paint':
            if msg_res <= 5:
                paint(state, app)
            elif msg_res > 5 and msg_res != 10:
                print('esperar 3 sgundos')
                time.sleep(3)
                paint(state, app)
            elif msg_res == 10:
                print('ERROR')
        elif app == 'notepad':
            if msg_res <= 5:
                notepad(state, app)
            elif msg_res > 5 and msg_res != 10:
                print('esperar 3 sgundos')
                time.sleep(3)
                notepad(state, app)
            elif msg_res == 10:
                print('ERROR')

    return render_template('index.html')


def calculator(state, app):

    timer = datetime.datetime.now()

    app_name = '"Calculator.exe"'
    if state == 'open':
        msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): Abrio!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
        new_log(msg)
        os.system('calc.exe')
        print('abrir calculadora')
    elif state == 'close':
        command = "taskkill /IM {} /F".format(str(app_name))
        os.system(command)
        msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): Cerro!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
        new_log(msg)
        print('cerrar calculadora')

def paint(state, app):
    timer = datetime.datetime.now()

    app_name = '"mspaint.exe"'
    if state == 'open':
        msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): Abrio!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
        new_log(msg)
        call(['mspaint']) 
    elif state == 'close':
        command = "taskkill /IM {} /F".format(str(app_name))
        os.system(command)
        msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): Cerro!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
        new_log(msg)
        print('cerrar paint')

def notepad(state, app):
    timer = datetime.datetime.now()
    app_name = "notepad.exe"
    if state == 'open':
        msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): Abrio!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
        new_log(msg)
        os.system('notepad.exe')
        print('abrir notepad')
    elif state == 'close':
        command = "taskkill /IM {} /F".format(str(app_name))
        os.system(command)
        msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): Cerro!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
        new_log(msg)
        print('cerrar notepad')

def response(app, state):
    timer = datetime.datetime.now()
    number = random.randint(1, 10)

    if state == 'open':
        if number <= 5:
            msg = '[{}/{}/{} - {}:{}:{}] [user] ({}): Abrir!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [kernel] ({}): Abriendo!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): OK!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            print(msg)
        if number > 5 and number != 10:
            msg = '[{}/{}/{} - {}:{}:{}] [user] ({}): Abrir!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [kernel] ({}): Abriendo!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): Espera 3 segundos...\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            print(msg)
        if number == 10:
            msg = '[{}/{}/{} - {}:{}:{}] [user] ({}): Abrir!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [kernel] ({}): Abriendo!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): ERROR\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            print(msg)
    elif state == 'close':
        if number <= 5:
            msg = '[{}/{}/{} - {}:{}:{}] [user] ({}): Cerrar!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [kernel] ({}): Cerrando!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): OK!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            print(msg)
        if number > 5 and number != 10:
            msg = '[{}/{}/{} - {}:{}:{}] [user] ({}): Cerrar!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [kernel] ({}): Cerrando!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): Espera 3 segundos...\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            print(msg)
        if number == 10:
            msg = '[{}/{}/{} - {}:{}:{}] [user] ({}): Cerrar!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [kernel] ({}): Cerrando!\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): ERROR\n'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
            new_log(msg)
            print(msg)

    return number

def new_log(log):
    add_log = log
    with open('myfile.txt', 'a+') as fp:
        fp.write(add_log)
        fp.close()
        pass