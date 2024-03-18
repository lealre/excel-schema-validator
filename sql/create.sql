CREATE TABLE sales (
    email VARCHAR(255) NOT NULL,
    data TIMESTAMP NOT NULL,
    value NUMERIC(10, 2) NOT NULL CHECK (value >= 0),
    amount INTEGER NOT NULL CHECK (amount >= 0),
    product VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL
);