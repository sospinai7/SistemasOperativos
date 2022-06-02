from email.mime import application
from flask import Flask, render_template
import sys, os

from kernel import kernel
from application import application

app = Flask(__name__)
app.register_blueprint(kernel, url_prefix='/kernel')
app.register_blueprint(application, url_prefix='/application')

posts = []

###
 #  Create txt
###
cwd = os.getcwd()
dir_name = cwd
listOfFiles = os.listdir(dir_name)
txt_name = "\myfile.txt"                            ##Nombre del archivo del logs
txt_file_path = cwd+txt_name
file_exists = os.path.exists(txt_file_path)

def rename_txt(new_name):
    new_txt_name = cwd+new_name
    # txt_name = new_name
    print(new_txt_name)
    os.rename(txt_file_path, new_txt_name)

def delete_file():
    for file in listOfFiles:
        if file.endswith(".txt"):
            os.remove(os.path.join(dir_name, file))
    create_txt("Gestor de archivos\n") 
    # rename_txt('\prueba.txt')                     ##Para cambiar el nombre del archivo .txt

def create_txt(log):
    with open('myfile.txt', 'w') as fp:
        fp.write(log)
        # fp.close()
        pass 

def txt_file():
    for file in listOfFiles:
        if file.endswith(".txt"):
            delete_file()
        else:
            create_txt("Gestor de archivos\n")

@app.route("/")
def index():
    print("inicio el programa")
    txt_file()
    return render_template("index.html", num_posts=len(posts))