# Pelvis
#### Video Demo:  <URL https://youtu.be/Uj1nMpW8zFU>


## What is Pelvis?
In the final year of my HBO education, I conducted an in-depth study on pelvic floor muscle tension, leading to the conceptualization of the PELVIS app. This app is designed specifically for women experiencing elevated pelvic floor muscle tension. Currently, I have actively worked on translating this concept into a functional website. It serves as a hub where a wealth of information is consolidated and easily accessible. Women can also find videos here featuring exercises that may help alleviate pelvic floor muscle tension. These videos are categorized into yoga, meditation, physiotherapy, and breathing exercises. Originally, there was mention of a specialists' page. Currently, it's stated that the specialists' page is still in development as it's currently not feasible. The idea was to provide a platform on this site where women could connect with various specialists, such as physiotherapists and doctors, but this is currently not feasible. Users can collect their favorite articles and videos on this site by clicking on the heart icons associated with the video or article. These favorites can be accessed on the favorites page.


## Register page:
#### register.html
The first page the user encounters when opening the site is the login and registration page. Clicking on the Pelvis logo reloads the page. It's not possible to access the index page without logging in. In the top right corner, you can click on "login" which leads to the login page. At the bottom, the user has the option to log in instead of registering. When registering, there are several requirements added.

Username requirements:
* The username field must be filled in / cannot be left empty;
* The username must be longer than 3 characters;
* The username must not already be in use by someone else and must therefore be unique.

Email requirements:
* Email field must be filled in / cannot be left empty;
* Email must follow the format of an email address, such as @ and .;
* Email address must not already be in use.

Password requirements:
* Password field must be filled in;
* Password must be at least 6 characters long;
* Password must not exceed 20 characters;
* Password must contain at least one lowercase letter;
* Password must contain at least one uppercase letter;
* Password must contain at least one digit;
* Password must contain at least one of the following special characters: !?@#$%*&;
* Password must not contain spaces.

Repeat password:
* Repeat password field must be filled in / cannot be left empty;
* The repeated password must match the password entered above.

If these requirements are not met, an alert box will appear indicating what is missing or incorrect.
If everything is filled in correctly, the data will be saved in pelvis.db under the users table. The password is converted into a hash code and stored in the pelvis.db as well.


## Login page:
#### login.html
The first page you encounter when opening the site is the login and registration page. Clicking on the Pelvis logo reloads the page. It's not possible to access the index page without logging in. In the top right corner, you can click on "login" which leads to the login page. At the bottom, you can choose to register instead of logging in. When logging in, there are several requirements added.

Username:
* The username field must be filled in / cannot be left empty;
* Username must exist in the database and therefore be in use.

Password:
* The password field must be filled in / cannot be left empty;
* The password must match the username entered. They must both be stored under the same ID in the database.

If these requirements are not met, an alert box will appear indicating what is missing or incorrect.
If everything is filled in correctly, the user will be redirected to the index page.


## Index page:
#### index.html
After logging in, you will be redirected to the index page. On this page, you will find an overview of several aspects of the site. In the navigation bar on the left side, you will see the Pelvis logo and links to the information, exercise, and specialists pages. The Pelvis logo links back to the index page. On the right side, you will see a profile icon, a heart icon, and a logout option. The profile icon links to the profile page. The heart icon links to the favorites page, and clicking on logout will log you out. When hovering over the different links, that section of the navigation bar turns blue. When hovering over the profile symbol, the symbol turns pink.

At the top of the page, you will find a brief explanation of what Pelvis exactly is and a stress meter. Currently, this stress meter is not functional, but it will be further developed outside of this task. Below this, there is an image of an article, which is also a link to the article about stress. When hovering over this, a shadow appears behind the image. Below this link, you will find four different images, each of which is also a link to another page. Yoga links to the yoga videos, Breathing links to the breathing videos, and so on. When hovering over these, a shadow appears behind the image.


## Excersiselink page:
#### exerciselink.html
Clicking on one of the four images (yoga, breathing, meditation, physio) on the index page will take you to the exercise link page. Each link from these four images will display different content but on the same HTML page with the same layout. For example, clicking on Yoga will display the videos related to yoga.

Here, you will see three videos related to the subject. When hovering over the video images, they darken with a transition effect, and a play button appears. When the mouse leaves the image, it returns to its original state.

At the top right corner of each video, there is an outline of a heart icon. Clicking on it will fill the heart icon with a pink color. Through the collaboration of JavaScript, CSS, HTML, and Python, the information linked to this video is stored in the Pelvis database under the "favorites" table, associated with the user's ID. When you reload the page, it will retrieve the new information and recognize that you have liked that particular video. The heart icon will remain filled until you click on it again. Clicking on it again will revert the heart icon back to just an outline, and the video will be removed from your favorites within the database. When you reload the page, it will no longer be in your favorites, and thus the heart icon will no longer be filled for that video on this page.

Clicking on a video image will redirect you to the specific video on the video page (as explained later in the explanation).


## Excersises page:
#### exercises.html
By clicking on the "exercises" link at the top of the navigation bar, you will arrive at the exercises page. This page has a similar layout to the exercise link page but contains videos from all topics. The functionality of this page is the same as the exercise link page. The favorites system works similarly here as well.


## Videos page:
#### videos.html
When you click on one of the videos displayed on exercise.html or exerciselink.html, you will be directed to the videos page. On this page, each video utilizes the same HTML file and has the same layout. From the HTML file of exercises.html or exerciselink.html, depending on which page you clicked a video image, the video information is passed through the internet URL to the videos page. As a result, you will see the video that corresponds to the video image you previously clicked. The video will start playing immediately with sound.


## Information page:
#### information.html
When you click on the "information" link at the top of the navigation bar, you will arrive at the information page. On this page, you will currently find three different articles. When you hover over them, the image gets a shadow effect. At the top right of each image, you will find the same heart icons mentioned and described earlier. The favorites system works the same way as on the exercises page. Each image links to an article (article.html).


## Article page:
#### article.html
When the user clicks on an image of an article on the information page, the user will be directed to the article page (article.html). This page displays the selected article. From information.html, it retrieves the information about which specific article is clicked and what exact information is needed. Through the Python file, the required information is fetched from the text files and displayed via article.html. The formatting is relatively consistent across the articles, but the content varies.


## Specialists page:
#### specialists.html
The specialists page can be accessed by clicking on the "specialists" link at the top of the navigation bar. The user will then be redirected to specialists.html. On this page, there is a message indicating that this page is still under development. The specialists page was part of the original idea but is currently not feasible, as it requires contacting specialists for its implementation.


## Profile page:
#### profile.html
By clicking on the profile icon at the top right of the navigation bar, you will be directed to the profile page (profile.html). On this page, you will find an overview of the user's information. On the left, if you haven't chosen a profile photo yet, you will see a blank profile photo image with a "change" button below it. On the right, there is a section where the user is greeted, displaying the current email address of the user with a "change" button next to it and below that, there is a link to the favorites page, and at the bottom, there is a button to change the password. The information about the profile photo, the username, and the user's email address is retrieved from the pelvis.db from the "users" table.

By clicking on "change" below the profile photo, an alert box will appear. Here, you have the option to upload a photo file. When you press "change," the profile photo will be updated. Pressing the "x" will close the alert box. There are certain requirements for changing the profile photo:
* It must be an image file, such as JPG, jpg, png, and so on;
* An image must be uploaded / the field cannot be left empty.

If the file does not meet these requirements, an alert box will appear indicating that information is missing or that the file is incorrect. The name of the file is stored in pelvis.db under the "users" table under "profilepic". The file itself is stored in the static file of finalproject through Python. If there is already a profile photo in use and you change the profile photo, it will delete the old photo from the static file and save the new one. It will also delete the old name from pelvis.db and save the new one.

Next to the email address on the right, you will find a "change" button. Clicking on this will redirect you to change-email.html. This page will be explained later in this document.

Below the email address, you will find the word "favorites" next to the heart symbol. Clicking on "favorites" will redirect you to favorites.html. This page will be explained later in this document.

At the bottom of the right box, you will find the "change password" button. Clicking on this will redirect you to changepassword.html. This page will be explained later in this document.


## Favorites page:
#### favorites.html
When you click on "favorites" on the profile page or when you click on the heart icon at the top right of the navigation bar, you will be redirected to favorites.html. On this page, you will find all the articles and videos that you have previously liked by filling in the heart symbols next to the corresponding articles and/or videos. The content of this page depends on what you have liked. This information is retrieved from pelvis.db from the "favorites" table. It fetches all favorites linked to the user's ID. When you hover over the articles, they will have a shadow effect. When you hover over the videos, the shadow effect intensifies, the image becomes darker, and a play button appears. Otherwise, these image links work the same as on the information page, exercises page, and exerciselink pages.


## Change Password page:
#### changepassword.html
By clicking on the "change Password" button on the profile page, you will be redirected to changepassword.html. On this page, the user can change their password. Here, the user needs to enter their old password and their new password twice. There are several requirements for this:
* Old password field must be filled in / cannot be left empty;
* New password field must be filled in / cannot be left empty;
* Confirmation password field must be filled in / cannot be left empty;
* The old password must match the user's current password;
* New password must be at least 6 characters long;
* New password must not exceed 20 characters;
* New password must contain at least one lowercase letter;
* New password must contain at least one uppercase letter;
* New password must contain at least one digit;
* New password must contain at least one of the following special characters: !?@#$%*&;
* New password must not contain spaces;
* The repeated password must match the password entered above.

The user's current password is retrieved from pelvis.db from the "users" table. It checks which password matches the hash currently used.

When you click on "change password" and the requirements are not met, an alert box will appear with information about what is missing or incorrect. When everything is filled in correctly, the hashed password in pelvis.db is updated. The old password is removed, and the new password is hashed and stored under the current user.


## Change Email page:
#### change-email.html
By clicking on the "change" button next to the email address on the profile page, you will be directed to the change email page (change-email.html). On this page, the user can update their email address. There are several requirements for changing the email address:
* All three email fields must be filled in / cannot be left empty;
* The old email address must match the user's current email address;
* New email must follow the format of an email address, such as @ and . ;
* The new email address must not already be in use;
* The repetition of the new email address must match the one entered above.

The user's current email address is retrieved from pelvis.db from the "users" table.

When you click on "change Email" and the requirements are not met, an alert box will appear with information about what is missing or incorrect. When everything is filled in correctly, the email address in pelvis.db is updated. The old email address is removed, and the new email address is stored under the current user.


### Sources:
https://www.w3schools.com/css/default.asp (multiple toppics)

https://chat.openai.com/auth/login (used like it is a rubber duck)

