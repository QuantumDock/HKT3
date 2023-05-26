from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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

