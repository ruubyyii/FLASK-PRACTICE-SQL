DROP DATABASE IF EXISTS flask_practice_sql; 
CREATE DATABASE flask_practice_sql;
USE flask_practice_sql;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(15),
    email VARCHAR(50),
    password VARCHAR(255)
);

CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(15),
    price FLOAT,
    img VARCHAR(255)
);

CREATE TABLE users_favorites (
    user_id INT,
    product_id INT,
    PRIMARY KEY (user_id, product_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

