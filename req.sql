CREATE TABLE users (
   id SERIAL PRIMARY KEY,
    email varchar NOT NULL,
    Pass VARCHAR NOT NULL
       
);


SELECT email,pass FROM users JOIN bpok_user ON users.email=bpok_user.email


CREATE TABLE bpok_user (
   id SERIAL PRIMARY KEY,
    email varchar NOT NULL,
    book_name VARCHAR NOT NULL,
    book_id INT NOT NULL
       
);