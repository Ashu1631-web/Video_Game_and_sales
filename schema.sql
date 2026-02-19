CREATE DATABASE videogame_db;
USE videogame_db;

-- Table: Game Engagement
CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    rating FLOAT,
    genres VARCHAR(255),
    plays INT,
    wishlist INT,
    backlog INT,
    release_date DATE,
    platform VARCHAR(100),
    team VARCHAR(150)
);

-- Table: Sales Data
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    platform VARCHAR(50),
    year INT,
    genre VARCHAR(100),
    publisher VARCHAR(150),
    global_sales FLOAT,
    na_sales FLOAT,
    eu_sales FLOAT,
    jp_sales FLOAT,
    other_sales FLOAT
);
