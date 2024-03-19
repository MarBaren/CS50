import os
import re
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "Marianne"
Session(app)

db = SQL("sqlite:///pelvis.db")


# allowed filename (jpg, png and so on)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Login required
def login_required(f):
    """ Decorate routes to require login. """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# Check if email adress meets the requirements
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


# Ensuring that the line breaks in the text files are properly converted into the HTML files
def replace_newlines_with_html(text):
    return "<br>".join(text.split("\n"))


# Stress article text from textfiles
readfile = open('text1stress.txt', 'r')
file1 = readfile.read().split("\n")
filestress1 = '\n'.join(file1)
stress1 = replace_newlines_with_html(filestress1)

readfile = open('text2stress.txt', 'r')
file2 = readfile.read().split("\n")
filestress2 = '\n'.join(file2)
stress2 = replace_newlines_with_html(filestress2)

readfile = open('text3stress.txt', 'r')
file3 = readfile.read().split("\n")
filestress3 = '\n'.join(file3)
stress3 = replace_newlines_with_html(filestress3)

readfile = open('text4stress.txt', 'r')
file4 = readfile.read().split("\n")
filestress4 = '\n'.join(file4)
stress4 = replace_newlines_with_html(filestress4)

readfile = open('text5stress.txt', 'r')
file5 = readfile.read().split("\n")
filestress5 = '\n'.join(file5)
stress5 = replace_newlines_with_html(filestress5)

readfile = open('text6stress.txt', 'r')
file6 = readfile.read().split("\n")
filestress6 = '\n'.join(file6)
stress6 = replace_newlines_with_html(filestress6)


# Pelvic article text from textfiles
readfile = open('text1pelvic.txt', 'r')
file1 = readfile.read().split("\n")
filepelvic1 = '\n'.join(file1)
pelvic1 = replace_newlines_with_html(filepelvic1)

readfile = open('text1.1pelvic.txt', 'r')
file1_1 = readfile.read().split("\n")
filepelvic1_1 = '\n'.join(file1_1)
pelvic1_1 = replace_newlines_with_html(filepelvic1_1)

readfile = open('text2pelvic.txt', 'r')
file2 = readfile.read().split("\n")
filepelvic2 = '\n'.join(file2)
pelvic2 = replace_newlines_with_html(filepelvic2)

readfile = open('text3pelvic.txt', 'r')
file3 = readfile.read().split("\n")
filepelvic3 = '\n'.join(file3)
pelvic3 = replace_newlines_with_html(filepelvic3)

readfile = open('text4pelvic.txt', 'r')
file4 = readfile.read().split("\n")
filepelvic4 = '\n'.join(file4)
pelvic4 = replace_newlines_with_html(filepelvic4)


# Stories article text from textfiles
readfile = open('text3stories.txt', 'r')
file3 = readfile.read().split("\n")
filestories3 = '\n'.join(file3)
stories3 = replace_newlines_with_html(filestories3)

readfile = open('text4stories.txt', 'r')
file4 = readfile.read().split("\n")
filestories4 = '\n'.join(file4)
stories4 = replace_newlines_with_html(filestories4)

readfile = open('text5stories.txt', 'r')
file5 = readfile.read().split("\n")
filestories5 = '\n'.join(file5)
stories5 = replace_newlines_with_html(filestories5)

# Ensuring that the correct information from the text files can be retrieved in the HTML files
articles = {
    # https://thevagwhisperer.com/2023/04/25/stress-and-pelvic-floor-tension/
    'article1': {
        'title': 'Stress and Pelvic Floor Tension',
        'undertitle': 'What is stress?',
        'text1': stress1,
        'text2': stress2,
        'text3': stress3,
        'text4': stress4,
        'text5': stress5,
        'text6': stress6,
        'image1': '../static/stressarticleimg1.jpg',
        'image2': '../static/stressarticleimg2.jpg',
        'image3': '../static/stressarticleimg3.png'
    },
    # https://www.continence.org.au/news/hypertonic-pelvic-floor
    'article2': {
        'title': 'The hypertonic pelvic floor',
        'undertitle': 'What is a hypertonic pelvic floor?',
        'text1': pelvic1,
        'text1.1': pelvic1_1,
        'text2': pelvic2,
        'text3': pelvic3,
        'text4': pelvic4,
        'image1': '../static/pelvicarticleimg1.jpg',
        'image1.1': '../static/pelvicarticleimg1.1.jpg',
        'image2': '../static/pelvicarticleimg2.jpg',
        'image3': '../static/pelvicarticleimg3.png'
    },
    'article3': {
        'title': 'Stories from women with pelvic pain',
        'text3': stories3,
        'text4': stories4,
        'text5': stories5,
        'image1': '../static/storiesarticleimg1.jpg',
        'image2': '../static/storiesarticleimg2.jpeg'
    }
}


@app.route("/")
@login_required
def index():
    """Homepage"""
    if session.get("user_id") is None:
        return redirect("/login")
    return render_template("index.html")


@app.route("/exerciselink/<exerciselink_id>")
@login_required
def exerciselink(exerciselink_id):
    """exerciselink page"""
    favorite_words = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id", user_id=session["user_id"])
    favoritewords = []
    if favorite_words:
        for row in favorite_words:
            favoritewords.append(row["favorite"])

    print(favoritewords)

    if request.method == "POST":
        data = request.get_json()
        word = data.get("word")
        fill_status = data.get("fillStatus")

        if fill_status == 1:
            # Adding to favorites
            db.execute("INSERT INTO favorites (favorite, user_id) VALUES (:word, :user_id)",
                       word=word, user_id=session["user_id"])
        else:
            # Deleting from favorites
            db.execute("DELETE FROM favorites WHERE favorite = :word AND user_id = :user_id",
                       word=word, user_id=session["user_id"])

    # Ensuring that the correct information is showed in the HTML files
    yoga_link = exerciselink_id == "yoga"
    breathing_link = exerciselink_id == "breathing"
    meditation_link = exerciselink_id == "meditation"
    fysio_link = exerciselink_id == "fysio"

    return render_template('exerciselink.html', favorite_words=favoritewords, yoga_link=yoga_link, breathing_link=breathing_link, meditation_link=meditation_link, fysio_link=fysio_link)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    if session.get("first_load") is None:
        # Fist time loading the page, so session clear
        session.clear()

        # When the page is loaded
        session["first_load"] = True

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
    if session.get("first_load") is None:
        # Fist time loading the page, so session clear
        session.clear()

        # When the page is loaded
        session["first_load"] = True

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            flash("Must provide username", "error")
            return redirect("/register")

        # Ensure username is longer than three characters
        if len(username) < 3:
            flash("Username to short, minimal 3 characters", "error")
            return redirect("/register")

        # Ensure email was submitted
        elif not email:
            flash("Must profide email", "error")
            return redirect("/register")

        # Check if email has requered characters
        elif not validate_email(email):
            flash("Email is invalid")
            return redirect("/register")

        # Ensure password was submitted
        if not password:
            flash("Must provide password", "error")
            return redirect("/register")

        # Ensure that password meets the requirements
        if len(password) < 6 or len(password) > 20:
            flash("New password must contain at least 6 character and can not be longer than 20 characters", "error")
            return redirect("/register")
        elif not re.search("[a-z]", password):
            flash("New password must contain at least one lowercase letter", "error")
            return redirect("/register")
        elif not re.search("[A-Z]", password):
            flash("New password must contain at least one highercase letter", "error")
            return redirect("/register")
        elif not re.search("[0-9]", password):
            flash("New password must contain at least one digit", "error")
            return redirect("/register")
        elif not re.search("[!?@#$%*&]", password):
            flash("New password must contain at least one of these: !?@#$%*&", "error")
            return redirect("/register")
        elif re.search("\s", password):
            flash("New password can not contain any white spaces", "error")
            return redirect("/register")

        # Ensure password (again) was submitted
        if not confirmation:
            flash("Must provide password again", "error")
            return redirect("/register")

        # Ensure Password (again) matches the Password
        elif confirmation != password:
            flash("Passwords do not match", "error")
            return redirect("/register")

        # Ensure username doesn't already exist
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", username
        )

        if len(rows) != 0:
            flash("User already exists", "error")
            return redirect("/register")

        # Ensure email doesn't already exist
        rows = db.execute(
            "SELECT * FROM users WHERE email = ?", email
        )

        if len(rows) != 0:
            flash("Email already exists", "error")
            return redirect("/register")

        # Add the user's entry into the database:
        db.execute(
            "INSERT INTO users (username, email, hash) VALUES (?, ?, ?)",
            username, email,
            generate_password_hash(password),
        )

        # Query database for newly inserted user
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", username
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Show profile information"""
    result = db.execute(
        "SELECT username, email FROM users WHERE id = :user_id", user_id=session["user_id"]
    )

    result1 = db.execute(
        "SELECT profilepic FROM users WHERE id = :user_id", user_id=session["user_id"]
    )

    if result1:
        # Getting the first row of result1 and get the 'profilepic' value
        profile_pic = result1[0]['profilepic']
    else:
        profile_pic = None

    print(profile_pic)
    is_profile_page = True

    if request.method == "POST":
        # Ensure that there is a file uploaded
        if 'profilepic' not in request.files:
            flash('No file part')
            return redirect("/profile")

        file = request.files['profilepic']

        # Ensure there is a file selected
        if file.filename == '':
            flash('No file selected')
            return redirect("/profile")

        # Ensure that image isn't already in use
        if file.filename == profile_pic:
            flash('You already have this image as profile picture')
            return redirect("/profile")

        # Saving the new image
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if not "NULL":
                deletefilepath = os.path.join(app.config['UPLOAD_FOLDER'], profile_pic)
                os.remove(deletefilepath)
                file.save(filepath)
            file.save(filepath)

        db.execute(
            "UPDATE users SET profilepic = :profilepic WHERE id = :user_id",
            profilepic=file.filename,
            user_id=session["user_id"],
        )

        return redirect("/profile")

    return render_template("profile.html", result=result, is_profile_page=is_profile_page, profile_pic=profile_pic)


@app.route("/specialists")
@login_required
def specialists():
    """Specialists page"""
    is_specialists_page = True

    return render_template("specialists.html", is_specialists_page=is_specialists_page)


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

        # Ensure that new password meets the requirements
        if len(newpassword) < 6 or len(newpassword) > 20:
            flash("New password must contain at least 6 character and can not be longer than 20 characters", "error")
            return redirect("/changepassword")
        elif not re.search("[a-z]", newpassword):
            flash("New password must contain at least one lowercase letter", "error")
            return redirect("/changepassword")
        elif not re.search("[A-Z]", newpassword):
            flash("New password must contain at least one highercase letter", "error")
            return redirect("/changepassword")
        elif not re.search("[0-9]", newpassword):
            flash("New password must contain at least one digit", "error")
            return redirect("/changepassword")
        elif not re.search("[!?@#$%*&]", newpassword):
            flash("New password must contain at least one of these: !?@#$%*&", "error")
            return redirect("/changepassword")
        elif re.search("\s", newpassword):
            flash("New password can not contain any white spaces", "error")
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

        else:
            flash("Old password is incorrect", "error")
            return redirect("/changepassword")

        flash("Password successfully changed", "success")
        return redirect("/profile")

    else:
        return render_template("changepassword.html")


@app.route("/change-email", methods=["GET", "POST"])
@login_required
def changeemail():
    """Change email"""
    if request.method == "POST":

        oldemail = request.form.get("oldemail")
        newemail = request.form.get("newemail")
        confirmation = request.form.get("confirmation")


        # Ensure that all three fields are filled in
        if not oldemail:
            flash("Must provide old email")
            return redirect("/change-email")

        if not newemail:
            flash("Must provide new email")
            return redirect("/change-email")

        if not confirmation:
            flash("Must provide new email again")
            return redirect("/change-email")


        if confirmation != newemail:
            flash("New email adresses do not match")
            return redirect("/change-email")

        # Check if email has requered characters
        if not validate_email(newemail):
            flash("New email is invalid")
            return redirect("/change-email")

        # Check if old emailadress and current email adress match
        currentemail_query = db.execute(
            "SELECT email FROM users WHERE id = :user_id", user_id=session["user_id"]
        )

        currentemail = currentemail_query[0]["email"]

        if currentemail != oldemail:
            print(currentemail)
            flash("This old emailadress doesn't match your current emailadress")
            return redirect("/change-email")

        # Check if email isn't already in use
        rows = db.execute(
            "SELECT * FROM users WHERE email = ?", request.form.get("newemail")
        )

        if len(rows) != 0:
            flash("Email already exists", "error")
            return redirect("/change-email")

        db.execute(
            "UPDATE users SET email = :newemail WHERE id = :user_id", newemail=newemail, user_id=session["user_id"]
        )
        return redirect("/profile")

    else:
        return render_template("change-email.html")


@app.route("/information", methods=["GET", "POST"])
@login_required
def information():
    """Information Page"""

    favorite_words = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id", user_id=session["user_id"])
    favoritewords = []
    if favorite_words:
        for row in favorite_words:
            favoritewords.append(row["favorite"])

    print(favoritewords)

    if request.method == "POST":
        data = request.get_json()
        word = data.get("word")
        fill_status = data.get("fillStatus")

        if fill_status == 1:
            # Toevoegen aan favorieten
            db.execute("INSERT INTO favorites (favorite, user_id) VALUES (:word, :user_id)",
                       word=word, user_id=session["user_id"])
        else:
            # Verwijderen uit favorieten
            db.execute("DELETE FROM favorites WHERE favorite = :word AND user_id = :user_id",
                       word=word, user_id=session["user_id"])

    return render_template("information.html", favorite_words=favoritewords, articles=articles)


@app.route("/article/<article_id>")
@login_required
def article(article_id):
    """article page"""
    article_content = articles.get(article_id)
    stress_article = article_id == "article1"
    pelvic_article = article_id == "article2"
    stories_article = article_id == "article3"
    readfile.close()
    return render_template('article.html', article_content=article_content, stress_article=stress_article, pelvic_article=pelvic_article, stories_article=stories_article)


@app.route("/exercises")
@login_required
def exercises():
    """Excersise page"""
    favorite_words = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id", user_id=session["user_id"])
    favoritewords = []
    if favorite_words:
        for row in favorite_words:
            favoritewords.append(row["favorite"])

    print(favoritewords)

    if request.method == "POST":
        data = request.get_json()
        word = data.get("word")
        fill_status = data.get("fillStatus")

        if fill_status == 1:
            # Toevoegen aan favorieten
            db.execute("INSERT INTO favorites (favorite, user_id) VALUES (:word, :user_id)",
                       word=word, user_id=session["user_id"])
        else:
            # Verwijderen uit favorieten
            db.execute("DELETE FROM favorites WHERE favorite = :word AND user_id = :user_id",
                       word=word, user_id=session["user_id"])

    return render_template("exercises.html", favorite_words=favoritewords)


@app.route("/videos")
@login_required
def videos():
    """videos page"""
    videoUrl = request.args.get('videoUrl')
    print(videoUrl)

    return render_template("videos.html")


@app.route("/favorites")
@login_required
def favorites():
    """favorites page"""
    favorite_words = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id", user_id=session["user_id"])
    favoritewords = []
    if favorite_words:
        for row in favorite_words:
            favoritewords.append(row["favorite"])
        favWords = True
    else:
        favWords = False

    print(favorite_words)

    info = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id AND favorite LIKE '%info%'", user_id=session["user_id"])
    if info:
        info = True
    else:
        info = False

    yoga = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id AND favorite LIKE '%yoga%'", user_id=session["user_id"])
    if yoga:
        yoga = True
    else:
        yoga = False

    breathing = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id AND favorite LIKE '%breathing%'", user_id=session["user_id"])
    if breathing:
        breathing = True
    else:
        breathing = False

    meditating = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id AND favorite LIKE '%meditating%'", user_id=session["user_id"])
    if meditating:
        meditating = True
    else:
        meditating = False

    fysio = db.execute(
        "SELECT favorite FROM favorites WHERE user_id = :user_id AND favorite LIKE '%fysio%'", user_id=session["user_id"])
    if fysio:
        fysio = True
    else:
        fysio = False

    return render_template("favorites.html", favorite_words=favoritewords, favoritewords=favoritewords, yoga=yoga, breathing=breathing, meditating=meditating, fysio=fysio, info=info, favWords=favWords)
