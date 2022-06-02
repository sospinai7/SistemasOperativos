from flask import Blueprint, render_template, abort, request
import os, datetime, time
import random
from subprocess import call

archivo = Blueprint('archivo', __name__,
                        template_folder='templates',
                        static_folder='static')

@archivo.route('/')
def show():
    return render_template('index.html')


@archivo.route('/archivo/controller/<string:action>')
def controller(action):
    print(action)

    return render_template('index.html')