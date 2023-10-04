import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='templates')

with open("csv file.csv", "r") as f:
    reader = csv.DictReader(f)
    csv_file = list(reader) 

@app.route("/")
def index():
    #template found in templates/index.html
    return render_template("index.html")

@app.route("/csv_file")
def csvfile():
    return jsonify(csv_file)



app.run(debug=True)

