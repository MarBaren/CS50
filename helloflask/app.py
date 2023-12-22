from flask import Flask, render_template, request

app = Flask(__name__)

character = {}
CHARACTERS = [
    "Harry Potter",
    "Hermione Granger"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", CHARACTERS=CHARACTERS)
    else:
        print("Form submitted!")
        character = request.form.get("character")
        return render_template("character.html", character=character)
