DROP TABLE IF EXISTS CARTS;
DROP TABLE IF EXISTS USER_PURCHASE_HISTORY;
DROP TABLE IF EXISTS USERS_LIBRARY;
DROP TABLE IF EXISTS REVIEWS;
DROP TABLE IF EXISTS GENRES;
DROP TABLE IF EXISTS GAMES;
DROP TABLE IF EXISTS USERS;


CREATE TABLE USERS (
  userID INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  password TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  address TEXT NOT NULL
);


CREATE TABLE GENRES (
  genreID INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE GAMES (
  gameID INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  developer TEXT NOT NULL,
  price REAL NOT NULL,
  image TEXT NOT NULL,
  genre INTEGER NOT NULL,
  avergeRating REAL NOT NULL,
  FOREIGN KEY (genre) REFERENCES GENRES (genreID)
);

CREATE TABLE USER_PURCHASE_HISTORY (
  purchaseID INTEGER PRIMARY KEY AUTOINCREMENT,--for uniqueness purposes.
  purchase_number INTEGER NOT NULL,
  userID INTEGER NOT NULL,
  gameID INTEGER NOT NULL,
  purchase_date TEXT NOT NULL,
  total_price REAL NOT NULL,
  FOREIGN KEY (userID) REFERENCES USERS (userID),
  FOREIGN KEY (gameID) REFERENCES GAMES (gameID)
);

CREATE TABLE CARTS (
  cartID INTEGER PRIMARY KEY AUTOINCREMENT, --for uniqueness purposes.
  userID INTEGER NOT NULL,
  gameID INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  total_price REAL NOT NULL,
  FOREIGN KEY (userID) REFERENCES USERS (userID),
  FOREIGN KEY (gameID) REFERENCES GAMES (gameID)
);

CREATE TABLE USERS_LIBRARY (
  userID INTEGER NOT NULL PRIMARY KEY,
  gameID INTEGER NOT NULL,
  purchase_date TEXT NOT NULL,
  download_link TEXT NOT NULL,
  FOREIGN KEY (userID) REFERENCES USERS (userID),
  FOREIGN KEY (gameID) REFERENCES GAMES (gameID)
);

CREATE TABLE REVIEWS (
  reviewID INTEGER PRIMARY KEY AUTOINCREMENT,
  userID INTEGER NOT NULL,
  gameID INTEGER NOT NULL,
  rating INTEGER NOT NULL,
  description TEXT NOT NULL,
  FOREIGN KEY (userID) REFERENCES USERS (userID),
  FOREIGN KEY (gameID) REFERENCES GAMES (gameID)
);

INSERT INTO USERS (name, password,email, address) VALUES ('Miguel', '1234', 'miguel.soto@email.com', 'Santo Domingo, Heredia');
INSERT INTO USERS (name, password,email, address) VALUES ('Ricardo', '1234', 'ricardo.munoz@email.com', 'Higuito, Desamparados');
INSERT INTO USERS (name, password,email, address) VALUES ('Abel', '1234', 'abel.hooker@email.com', 'Minneapolis, Minnesota');

INSERT INTO GENRES (name) VALUES ('Horror');
INSERT INTO GENRES (name) VALUES ('Adventure');
INSERT INTO GENRES (name) VALUES ('First_Person_Shooter');
INSERT INTO GENRES (name) VALUES ('Third_Person');
INSERT INTO GENRES (name) VALUES ('Puzzle');

INSERT INTO GAMES (name, description, developer, price, image, genre, avergeRating) VALUES ('Halo 3', 'The best Game ever made','Bungie', 59.99, 'https://cdn.vox-cdn.com/thumbor/oFM-rZEfJNCTrCPerSLKNk-f08U=/0x0:1857x1106/1820x1213/filters:focal(443x235:739x531):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/67025788/halo_3.6.jpg',3, 10);
INSERT INTO GAMES (name, description, developer, price, image, genre, avergeRating) VALUES ('Escape From Tarkov', 'The best extraction Royale','Battle State Games', 59.99, 'https://blog.turtlebeach.com/wp-content/uploads/2022/05/Escape-From-Tarkov-1024x576.jpeg',3, 8.9);
INSERT INTO GAMES (name, description, developer, price, image, genre, avergeRating) VALUES ('Dark Souls', 'The Game that popularized the term Souls Like','From Soft', 39.99, 'https://static.bandainamcoent.eu/high/dark-souls/brand-setup/ds3_thumb_brand_624x468.jpg',2, 9);
INSERT INTO GAMES (name, description, developer, price, image, genre, avergeRating) VALUES ('Harry Potter: Hogwards Legacy', 'New Game based in the Harry Potter World. 200 years prior to the events of the movies.','Warne Bros', 59.99, 'https://cloudfront-eu-central-1.images.arcpublishing.com/thenational/D7X7Q25XSZHTBP6NOB4BWQ4EOI.jpg',2, 7);
INSERT INTO GAMES (name, description, developer, price, image, genre, avergeRating) VALUES ('Dead Space', 'Remake of the successful 2007 horror game. Inventive and hardcore','EA',  59.99, 'https://assets.reedpopcdn.com/Dead-Space-Review-Site.jpg/BROK/resize/1200x1200%3E/format/jpg/quality/70/Dead-Space-Review-Site.jpg', 1, 9);
INSERT INTO GAMES (name, description, developer, price, image, genre, avergeRating) VALUES ('Metroid Prime Remake', 'Remake of the successful 2002 Game Cube','Retro Games', 39.99, 'https://media.cnn.com/api/v1/images/stellar/prod/230224110929-metroid-prime-remastered-review-cnnu-2.jpg?c=16x9&q=w_800,c_fill',3, 7);
INSERT INTO GAMES (name, description, developer, price, image, genre, avergeRating) VALUES ('Elden Ring', 'Battle Through the Lands Between, in search of the Elden Ring and becoming the Elden Lord','From Soft', 49.99, 'https://www.videogameschronicle.com/files/2022/02/sds5.jpg', 2, 8.9);
INSERT INTO GAMES (name, description, developer, price, image, genre, avergeRating) VALUES ('Tetris', 'One of the best games ever created', 'EA',  9.99, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Typical_Tetris_Game.svg/1200px-Typical_Tetris_Game.svg.png',5, 2);

INSERT INTO CARTS (userID, gameID, quantity, total_price) VALUES (1,3,1,59.99);
INSERT INTO CARTS (userID, gameID, quantity, total_price) VALUES (1,2,1,59.99);
INSERT INTO CARTS (userID, gameID, quantity, total_price) VALUES (1,6,2,19.98);


-- this represent a single purchase of a game. So, if a user purchases other games, in one single transaction, it will look like this.
-- Take into account that you'll need to generate this random 6 digit number every time you insert something in the database.
INSERT INTO USER_PURCHASE_HISTORY (purchase_number, userID, gameID, purchase_date, total_price) VALUES (850674, 1, 1, '2023-03-05 20:39:00', 59.99);
INSERT INTO USER_PURCHASE_HISTORY (purchase_number, userID, gameID, purchase_date, total_price) VALUES (850674, 1, 2, '2023-03-05 20:39:00', 59.99);
INSERT INTO USER_PURCHASE_HISTORY (purchase_number, userID, gameID, purchase_date, total_price) VALUES (850674, 1, 6, '2023-03-05 20:39:00', 19.98);

INSERT INTO REVIEWS (userID, gameID, rating, description) VALUES (1, 1, 10, 'It is simply, the best game every made, the perfect combination between heroism and glory, there are no word to describe love for this game.');


