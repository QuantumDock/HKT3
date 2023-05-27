from flask import Flask, render_template, request
import re
from password import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/slownik")
def dictionary():
    return render_template("dictionary.html")


@app.route("/quiz")
def quiz():
    lines = open("static/questions.csv", "rt", encoding='utf-8').readlines()
    data_lines = lines[2:]
    pafy = []
    corrects = []
    for line in data_lines:
        items = line.split(";")
        correct_item = 0
        for i in range(len(items)):
            if re.match(r"^\$", items[i]):
                correct_item = i
        corrects.append(correct_item)
        modified_items = [item[1:] if re.match(r"^\$", item) else item for item in items]
        pafy.append(modified_items)
    return render_template("quiz.html", test=len(pafy), args=pafy, corrects=corrects) # referencja do javy


@app.route("/hasla", methods=["GET"])
def password():
    if "taffy" not in request.args or request.args["taffy"] == "":
        return render_template("password.html", display=False)
    else:
        time = time_to_crack(request.args["taffy"])
        display_time = ""
        display_class = ""
        if time < 0.01:
            display_time = "0 sekund - śmiesznie łatwe do złamania."
            display_class = "password-red-bold"
        elif time < 120:
            display_time = f"{round(time, 2)} sekund - złamanie będzie bardzo szybkie."
            display_class = "password-red"
        elif time < 7200:
            display_time = f"{round(time/60, 2)} minut - złamanie będzie bardzo szybkie."
            display_class = "password-orange"
        elif time < 259200:
            display_time = f"{round(time/3600, 2)} godzin - hasło jest trochę lepsze, ale jest miejsce na poprawę."
            display_class = "password-yellow"
        elif time < 31536000:
            display_time = f"{round(time/86400, 2)} dni - hasło zabezpieczy twoje konto dość dobrze."
            display_class = "password-green-first"
        elif time < 31536000000000:
            display_time = f"{round(time/31536000, 2)} lat - takie hasło całkowicie wystarczy do właściwie wszystkiego."
            display_class = "password-green-second"
        elif time < 31536000000000000000000000:
            display_time = f"{round(time/31536000000000, 2)} milionów lat - jesteś mistrzem tworzenia bezpiecznych haseł!"
            display_class = "password-blue"
        else:
            display_time = f"{round(time/31536000000000000000000000, 2)} trylionów lat - jesteś mistrzem tworzenia bezpiecznych haseł!"
            display_class = "password-blue"
        display_time = f"<p class={display_class}>{display_time}</p>"
        return render_template("password.html", display=True, time=display_time)
