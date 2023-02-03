

CREATE TABLE qacafe (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_name VARCHAR(50) NOT NULL,
  order_date DATE NOT NULL,
  item_name VARCHAR(50) NOT NULL,
  item_quantity INTEGER NOT NULL,
  item_price DECIMAL(10,2) NOT NULL,
  total_cost DECIMAL(10,2) NOT NULL
);

INSERT INTO qacafe (customer_name, order_date, item_name, item_quantity, item_price, total_cost)
VALUES ('Akash Sharma', '2023-02-01', 'Coffee', 2, 3.5, 7.00),
       ('Nick Jones', '2023-02-02', 'Tea', 1, 2.5, 2.50),
       ('Alan Sugar', '2023-02-03', 'Coffee', 1, 3.5, 3.50),
       ('Jim Gates', '2023-02-03', 'Tea', 2, 2.5, 5.00),
       ('Amanda Jonny', '2023-02-04', 'Sandwich', 2, 5.0, 10.00),
       ('Ewelina Jones', '2023-02-04', 'Coffee', 2, 3.5, 7.00),
       ('David Smith', '2023-02-04', 'Sandwich', 5, 5.0, 25.00);
