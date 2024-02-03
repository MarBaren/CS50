CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    hash TEXT NOT NULL
);

CREATE UNIQUE INDEX username ON users (username);
