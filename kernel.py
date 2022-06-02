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
