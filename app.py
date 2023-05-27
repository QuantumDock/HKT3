from flask import Flask, render_template, request, url_for
import re
from password import *
from scam import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/slownik")
def dictionary():
    return render_template("dictionary.html")


@app.route("/gry")
def time():
    return render_template("gry.html")


@app.route("/portale")
def portals():
    return render_template("start.html")


@app.route("/portale/jak")
def jak():
    return render_template("portals.html")


@app.route("/portale/jak/facebook")
def facebook():
    return render_template("facebook.html")


@app.route("/portale/porady")
def porady():
    return render_template("advice.html")


@app.route("/link")
def link():
    return render_template("linki.html")


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
    if "pass" not in request.args or request.args["pass"] == "":
        return render_template("password.html", display=False)
    else:
        try:
            time = time_to_crack(request.args["pass"])
        except:
            return render_template("password.html", display=False)
        display_time = ""
        display_class = ""
        if time < 0.01:
            display_time = "0 sekund - złamanie jest tak proste, że hasło nie jest żadnym zabezpieczeniem."
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
        display_end = f"<p class={display_class}>{display_time}</p>"
        return render_template("password.html", display=True, time=display_end)
@app.route("/oszustwa", methods=["GET"])
def scam():
    if "tel" not in request.args or request.args["tel"] == "":
        return render_template("scam.html", display=False)
    else:
        try:
            time = check_scam(request.args["tel"])
            display_time = ""
            display_class = ""
            if time:
                display_time = "Oszust! Dzwoniący może chcieć wyłudzić od ciebie pieniądze!"
                display_class = "password-red"
            else:
                display_time = "Bezpieczny numer!"
                display_class = "password-green-second"
            display_end = f"<p class={display_class}>{display_time}</p>"
            return render_template("scam.html", display=True, time=display_end)
        except Exception:
            return render_template("scam.html", display=False)

