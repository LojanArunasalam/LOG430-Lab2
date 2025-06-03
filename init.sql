CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE stores (
    id SERIAL PRIMARY KEY, 
    name VARCHAR
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    total INTEGER,
    "user" INTEGER REFERENCES users(id),
    store INTEGER REFERENCES stores(id)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    category VARCHAR,
    description VARCHAR,
    prix_unitaire FLOAT
);

CREATE TABLE line_sales (
    id SERIAL PRIMARY KEY,
    quantite INTEGER,
    prix FLOAT,
    sale INTEGER REFERENCES sales(id),
    product INTEGER REFERENCES products(id)
);

CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    quantite INTEGER,
    product INTEGER REFERENCES products(id),
    store INTEGER REFERENCES stores(id)
);

CREATE TABLE products_depot (
    id SERIAL PRIMARY KEY,
    quantite_depot INTEGER,
    product INTEGER REFERENCES products(id)
);

INSERT INTO stores (name) VALUES
('Magasin Centre-Ville'),
('Magasin Nord'),
('Magasin Sud'),
('Magasin Est'),
('Maison Mère');

INSERT INTO users (name) VALUES
('Alice Johnson'), ('Bob Smith'), ('Catherine Lee'), ('David Miller'), ('Emma Davis'),
('Frank Wilson'), ('Grace Thompson'), ('Henry Anderson'), ('Isla Moore'), ('Jack Taylor');

INSERT INTO products (name, category, description, prix_unitaire) VALUES
('Timbits', 'Snacks', 'Tim Horton treats in the shape of a small ball', 0.25),
('Coffee', 'Beverages', 'Hot brewed coffee', 1.99),
('Donut', 'Snacks', 'Glazed donut', 1.25),
('Bagel', 'Snacks', 'Sesame seed bagel', 1.50),
('Muffin', 'Snacks', 'Blueberry muffin', 2.00);

INSERT INTO stocks (quantite, product, store) VALUES
(10, 1, 1), (10, 2, 1), (10, 3, 1), (10, 4, 1), (10, 5, 1), 
(10, 1, 2), (10, 2, 2), (10, 3, 2), (10, 4, 2), (10, 5, 2), 
(10, 1, 3), (10, 2, 3), (10, 3, 3), (10, 4, 3), (10, 5, 3), 
(10, 1, 4), (10, 2, 4), (10, 3, 4), (10, 4, 4), (10, 5, 4), 
(10, 1, 5), (10, 2, 5), (10, 3, 5), (10, 4, 5), (10, 5, 5);



INSERT INTO products_depot (quantite_depot, product) VALUES
(100, 1), (100, 2), (100, 3), (100, 4), (100, 5);




