CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    total INTEGER,
    "user" INTEGER REFERENCES users(id)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    category VARCHAR,
    description VARCHAR,
    prix_unitaire FLOAT,
    stock INTEGER
);

CREATE TABLE line_sales (
    id SERIAL PRIMARY KEY,
    quantite INTEGER,
    prix FLOAT,
    sale INTEGER REFERENCES sales(id),
    product INTEGER REFERENCES products(id)
);

INSERT INTO users (name) VALUES
('Alice Johnson'), ('Bob Smith'), ('Catherine Lee'), ('David Miller'), ('Emma Davis'),
('Frank Wilson'), ('Grace Thompson'), ('Henry Anderson'), ('Isla Moore'), ('Jack Taylor'),
('Kylie Martinez'), ('Liam Thomas'), ('Mia Garcia'), ('Noah Martin'), ('Olivia Jackson'),
('Paul White'), ('Quincy Harris'), ('Rachel Lewis'), ('Samuel Walker'), ('Tina Hall'),
('Umar Allen'), ('Victoria Young'), ('William King'), ('Xander Scott'), ('Yasmin Green'),
('Zachary Adams'), ('Aaron Baker'), ('Bella Rivera'), ('Caleb Hughes'), ('Diana Stewart'),
('Ethan Phillips'), ('Fiona Simmons'), ('George Foster'), ('Hannah Bennett'), ('Ian Graham'),
('Jasmine Barnes'), ('Kevin Coleman'), ('Luna Perry'), ('Marcus Powell'), ('Nina Cox'),
('Oscar Gray'), ('Penelope Rogers'), ('Quentin Reed'), ('Ruby Patterson'), ('Sean Bryant'),
('Talia Alexander'), ('Uriel Price'), ('Vanessa Sanders'), ('Wyatt Long'), ('Zoe Hunter');

INSERT INTO products (name, category, description, prix_unitaire, stock) VALUES
('Timbits', 'Snacks', 'Tim Horton treats in the shape of a small ball', 0.25, 100),
('Coffee', 'Beverages', 'Hot brewed coffee', 1.99, 50),
('Donut', 'Snacks', 'Glazed donut', 1.25, 70),
('Bagel', 'Snacks', 'Sesame seed bagel', 1.50, 40),
('Muffin', 'Snacks', 'Blueberry muffin', 2.00, 60),
('Latte', 'Beverages', 'Milk coffee with foam', 3.75, 80),
('Cappuccino', 'Beverages', 'Foamy espresso drink', 3.50, 90),
('Espresso', 'Beverages', 'Strong shot of coffee', 2.25, 55),
('Iced Coffee', 'Beverages', 'Chilled coffee drink', 2.50, 30),
('Green Tea', 'Beverages', 'Herbal tea', 1.75, 25),
('Black Tea', 'Beverages', 'Standard tea', 1.50, 35),
('Croissant', 'Pastries', 'Butter croissant', 2.25, 45),
('Chocolate Chip Cookie', 'Snacks', 'Large cookie with chocolate chips', 1.50, 100),
('Smoothie', 'Beverages', 'Fruit blended smoothie', 4.50, 20),
('Scone', 'Pastries', 'Raisin scone', 2.00, 50),
('Turkey Sandwich', 'Food', 'Sliced turkey and lettuce on bread', 5.00, 30),
('Ham Wrap', 'Food', 'Ham and cheese wrap', 4.50, 20),
('Veggie Panini', 'Food', 'Pressed sandwich with vegetables', 5.50, 15),
('Yogurt Parfait', 'Snacks', 'Yogurt with granola and fruit', 3.25, 25),
('Orange Juice', 'Beverages', 'Freshly squeezed OJ', 2.75, 60),
('Apple Juice', 'Beverages', 'Pressed apple juice', 2.50, 50),
('Milk', 'Beverages', 'Whole milk', 1.99, 40),
('Chocolate Milk', 'Beverages', 'Flavored milk', 2.25, 40),
('Trail Mix', 'Snacks', 'Nuts, dried fruit, and chocolate mix', 2.99, 30),
('Banana', 'Fruit', 'Fresh banana', 0.75, 80),
('Apple', 'Fruit', 'Red apple', 0.80, 90),
('Granola Bar', 'Snacks', 'Oats and honey bar', 1.10, 70),
('Energy Drink', 'Beverages', 'Caffeinated drink', 3.00, 25),
('Cheese Stick', 'Snacks', 'Individually wrapped cheese', 0.90, 65),
('Salad Bowl', 'Food', 'Garden salad with dressing', 4.25, 15),
('Pasta Box', 'Food', 'Microwavable pasta meal', 5.75, 10),
('Protein Shake', 'Beverages', 'Chocolate protein shake', 4.75, 20),
('Macarons', 'Pastries', 'French colorful sweets', 3.25, 12),
('Cupcake', 'Pastries', 'Vanilla cupcake with frosting', 2.50, 25),
('Hot Chocolate', 'Beverages', 'Sweet chocolate drink', 2.99, 35),
('Cinnamon Roll', 'Pastries', 'Sweet roll with icing', 3.00, 20),
('Tuna Sandwich', 'Food', 'Tuna and mayo on bread', 4.99, 18),
('Chicken Wrap', 'Food', 'Grilled chicken with lettuce in wrap', 5.25, 22),
('Ginger Ale', 'Beverages', 'Carbonated soft drink', 1.75, 40),
('Sparkling Water', 'Beverages', 'Carbonated water', 1.50, 50),
('Fruit Cup', 'Snacks', 'Mixed fruit in container', 2.25, 30),
('Bottle Water', 'Beverages', '500ml bottled water', 1.00, 100),
('Lemonade', 'Beverages', 'Fresh squeezed lemonade', 2.50, 30),
('Pizza Slice', 'Food', 'Single slice of cheese pizza', 3.25, 12),
('Mozzarella Sticks', 'Snacks', 'Cheesy fried snack', 3.75, 10),
('Nachos', 'Snacks', 'Chips with cheese', 3.50, 15),
('Poutine', 'Food', 'Fries, cheese, gravy', 4.50, 20),
('Mini Donuts', 'Snacks', 'Small cinnamon donuts', 2.25, 30),
('Bacon Egg Sandwich', 'Food', 'Breakfast sandwich', 4.75, 18),
('Avocado Toast', 'Food', 'Toasted bread with avocado', 5.50, 10);