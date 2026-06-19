CREATE TABLE if NOT EXISTS flower_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE if NOT EXISTS flowers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type INTEGER NOT NULL REFERENCES flower_types(id),
    primary_color VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL, 
    stock INTEGER CHECK (stock >= 0) NOT NULL
);


CREATE OR REPLACE VIEW available_flowers AS
    SELECT * FROM flowers WHERE stock > 0;