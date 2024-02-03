import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get stocks and shares
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
        user_id=session["user_id"],
    )

    # Value of stock at that moment
    cash = db.execute(
        "SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"]
    )[0]["cash"]

    total_value = 0
    grand_total = cash
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = quote["price"]
        stock["value"] = stock["price"] * stock["total_shares"]
        total_value += stock["value"]
        grand_total += stock["value"]
    return render_template(
        "index.html",
        stocks=stocks,
        cash=cash,
        total_value=total_value,
        grand_total=grand_total,
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        quote = lookup(symbol)

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide symbole", 403)
        elif not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("must provide a positive number of shares")

        if not quote:
            return apology("invalid symbol", 400)

        price = quote["price"]
        total_cost = int(shares) * price
        cash_query = db.execute(
            "SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"]
        )
        if not cash_query:
            return apology("Unable to fetch user's cash balance")

        cash = cash_query[0]["cash"]

        if cash < total_cost:
            return apology("not enough cash")

        transaction = "Buy"

        # Update user data
        db.execute(
            "UPDATE users SET cash = cash - :total_cost WHERE id = :user_id",
            total_cost=total_cost,
            user_id=session["user_id"],
        )

        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, transactie) VALUES (:user_id, :symbol, :shares, :price, :transaction)",
            user_id=session["user_id"],
            symbol=symbol,
            shares=shares,
            price=(-price),
            transaction=transaction,
        )

        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stocks = db.execute(
        "SELECT symbol, transactie, price, timestamp, shares FROM transactions WHERE user_id = :user_id ORDER BY timestamp DESC",
        user_id=session["user_id"],
    )

    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)

        # Ensure username was submitted
        if not quote:
            return apology("invalid symbol", 400)
        return render_template("quoted.html", quote=quote)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password (again) was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password again", 400)

        # Ensure Password (again) matches the Password
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("passwords do not match", 400)

        # Ensure username doesn't already exist
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 0:
            return apology("user already exists", 400)

        # Add the user's entry into the database:
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            request.form.get("username"),
            generate_password_hash(request.form.get("password")),
        )

        # Query database for newly inserted user
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # Get owned symbols of the current user
        stocks = db.execute(
            "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
            user_id=session["user_id"],
        )

        # Value of total cash owned by the user at that moment
        cash = db.execute(
            "SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"]
        )[0]["cash"]

        # Get the selected symbol from the form
        selected_symbol = request.form.get("symbol")

        # Find the selected stock in the list of owned stocks
        selected_stock = next(
            (stock for stock in stocks if stock["symbol"] == selected_symbol), None
        )

        # Ensure symbol was submitted
        if not selected_stock:
            return apology("Invalid symbol", 403)

        quote = lookup(selected_stock["symbol"])
        selected_stock["name"] = quote["name"]
        selected_stock["price"] = quote["price"]

        shares = request.form.get("shares")

        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("Must provide a positive number of shares")
        elif int(shares) > selected_stock["total_shares"]:
            return apology("You don't own that many shares")

        price = selected_stock["price"]
        total_sell = int(shares) * price

        if cash < total_sell:
            return apology("Not enough cash")

        transaction = "Sell"

        # Update user data
        db.execute(
            "UPDATE users SET cash = cash + :total_sell WHERE id = :user_id",
            total_sell=total_sell,
            user_id=session["user_id"],
        )

        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, transactie) VALUES (:user_id, :symbol, :shares, :price, :transaction)",
            user_id=session["user_id"],
            symbol=selected_stock["symbol"],
            shares=-int(shares),
            price=price,
            transaction=transaction,
        )

        return redirect("/")

    # Retrieve the owned symbols again for rendering the sell page
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
        user_id=session["user_id"],
    )

    return render_template("sell.html", stocks=stocks)


@app.route("/profile")
@login_required
def profile():
    """Show profile information"""
    result = db.execute(
        "SELECT username FROM users WHERE id = :user_id", user_id=session["user_id"]
    )

    return render_template("profile.html", result=result)


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    """Change password"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        oldpassword = request.form.get("oldpassword")
        newpassword = request.form.get("newpassword")
        confirmation = request.form.get("confirmation")

        # Ensure old password was submitted
        if not oldpassword:
            flash("Must provide old password", "error")
            return redirect("/changepassword")

        # Ensure new password was submitted
        elif not newpassword:
            flash("Must provide new password", "error")
            return redirect("/changepassword")

        # Ensure repeat new password was submitted
        elif not confirmation:
            flash("Must reapeat new password", "error")
            return redirect("/changepassword")

        # Ensure Password (again) matches the Password
        elif confirmation != newpassword:
            flash("New passwords do not match", "error")
            return redirect("/changepassword")

        # Ensure that old password matches current password user
        currentPasswordHash = db.execute(
            "SELECT hash FROM users WHERE id = :user_id", user_id=session["user_id"]
        )

        if currentPasswordHash and check_password_hash(
            currentPasswordHash[0]["hash"], oldpassword
        ):
            newpasswordHash = generate_password_hash(newpassword)
            db.execute(
                "UPDATE users SET hash = :newpasswordHash WHERE id = :user_id",
                newpasswordHash=newpasswordHash,
                user_id=session["user_id"],
            )
            flash("Password successfully changed", "success")

        else:
            flash("Old password is incorrect", "error")
            return redirect("/changepassword")

        return redirect("/")

    else:
        return render_template("changepassword.html")
