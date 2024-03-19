CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    hash TEXT NOT NULL
);

CREATE UNIQUE INDEX username ON users (username);

CREATE TABLE favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    favorite TEXT NOT NULL
);

ALTER TABLE users
ADD COLUMN profilepic TEXT;
