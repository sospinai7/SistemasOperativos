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
    msg_res = response(app, timer)

    if request.method == 'GET':
        if app == 'calc':
            if msg_res <= 5:
                calculator(state, timer)
            elif msg_res > 5 and msg_res != 10:
                print('esperar 3 sgundos')
                time.sleep(3)
                calculator(state, timer)
            elif msg_res == 10:
                print('ERROR')
        elif app == 'paint':
            if msg_res <= 5:
                paint(state, timer)
            elif msg_res > 5 and msg_res != 10:
                print('esperar 3 sgundos')
                time.sleep(3)
                paint(state, timer)
            elif msg_res == 10:
                print('ERROR')
        elif app == 'notepad':
            if msg_res <= 5:
                notepad(state, timer)
            elif msg_res > 5 and msg_res != 10:
                print('esperar 3 sgundos')
                time.sleep(3)
                notepad(state, timer)
            elif msg_res == 10:
                print('ERROR')

    return render_template('index.html')


def calculator(state, timer):
    app_name = '"Calculator.exe"'
    if state == 'open':
        os.system('calc.exe')
        print('abrir calculadora')
    elif state == 'close':
        command = "taskkill /IM {} /F".format(str(app_name))
        os.system(command)
        print('cerrar calculadora')

def paint(state, timer):
    app_name = '"mspaint.exe"'
    if state == 'open':
        call(['mspaint']) 
        print('abrir paint')
    elif state == 'close':
        command = "taskkill /IM {} /F".format(str(app_name))
        os.system(command)
        print('cerrar paint')

def notepad(state, timer):
    app_name = "notepad.exe"
    if state == 'open':
        os.system('notepad.exe')
        print('abrir notepad')
    elif state == 'close':
        command = "taskkill /IM {} /F".format(str(app_name))
        os.system(command)
        print('cerrar notepad')

def response(app, timer):
    number = random.randint(1, 10)

    # if number <= 5:
    #     # msg = '[{}/{}/{} - {}:{}:{}] [app] ({}): OK!'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)
    # if number > 5 and number != 10:
    #     # msg = '[{}/{}/{} - {}:{}:{}] [APP] ({}): Espera 3 segundos...'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(time.second), app)
    # if number == 10:
        # msg = '[{}/{}/{} - {}:{}:{}] [APP] ({}): ERROR'.format(str(timer.day), str(timer.month), str(timer.year), str(timer.hour), str(timer.minute), str(timer.second), app)

    return number