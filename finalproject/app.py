import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "Marianne"
Session(app)

db = SQL("sqlite:///pelvis.db")

def login_required(f):
    """ Decorate routes to require login. """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@login_required
def index():
    """Homepage"""
    if session.get("user_id") is None:
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username", "error")
            return redirect("/login")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password", "error")
            return redirect("/login")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("Invalid username and/or password", "error")
            return redirect("/login")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username", "error")
            return redirect("/register")

        if not request.form.get("email"):
            flash("Must profide email", "error")
            return redirect("/register")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password", "error")
            return redirect("/register")

        # Ensure password (again) was submitted
        elif not request.form.get("confirmation"):
            flash("Must provide password again", "error")
            return redirect("/register")

        # Ensure Password (again) matches the Password
        elif request.form.get("confirmation") != request.form.get("password"):
            flash("Passwords do not match", "error")
            return redirect("/register")

        # Ensure username doesn't already exist
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 0:
            flash("User already exists", "error")
            return redirect("/register")

        # Ensure email doesn't already exist
        rows = db.execute(
            "SELECT * FROM users WHERE email = ?", request.form.get("email")
        )

        if len(rows) != 0:
            flash("Email already exists", "error")
            return redirect("/register")

        # Add the user's entry into the database:
        db.execute(
            "INSERT INTO users (username, email, hash) VALUES (?, ?, ?)",
            request.form.get("username"), request.form.get("email"),
            generate_password_hash(request.form.get("password")),
        )

        # Query database for newly inserted user
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/explenationstressmeter")
    else:
        return render_template("register.html")

@app.route("/explenationstressmeter")
@login_required
def explenationstressmeter():
    """Homepage"""
    return render_template("explenationstressmeter.html")
