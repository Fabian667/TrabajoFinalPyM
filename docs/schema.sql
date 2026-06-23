-- Modelo ER - ERP para Fabricación de Muebles

-- Tabla: category
CREATE TABLE category (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT
);

-- Tabla: supplier
CREATE TABLE supplier (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    address TEXT
);

-- Tabla: raw_material
CREATE TABLE raw_material (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    unit VARCHAR(50) NOT NULL,
    stock DECIMAL(10, 2) NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    supplier_id BIGINT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);

-- Tabla: product
CREATE TABLE product (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    sku VARCHAR(255) UNIQUE,
    image_url VARCHAR(255),
    category_id BIGINT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category(id)
);

-- Tabla: bill_of_materials
CREATE TABLE bill_of_materials (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    product_id BIGINT NOT NULL,
    raw_material_id BIGINT NOT NULL,
    required_quantity DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (raw_material_id) REFERENCES raw_material(id)
);

-- Tabla: production_stage
CREATE TABLE production_stage (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    `order` INT NOT NULL,
    description TEXT
);

-- Tabla: users
CREATE TABLE users (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

-- Tabla: production_order
CREATE TABLE production_order (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    number VARCHAR(255) NOT NULL UNIQUE,
    creation_date DATE NOT NULL,
    start_date DATE,
    end_date DATE,
    status VARCHAR(50) NOT NULL,
    product_id BIGINT NOT NULL,
    quantity INT NOT NULL,
    observations TEXT,
    FOREIGN KEY (product_id) REFERENCES product(id)
);

-- Tabla: stage_log
CREATE TABLE stage_log (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    production_order_id BIGINT NOT NULL,
    production_stage_id BIGINT NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    user_id BIGINT NOT NULL,
    observations TEXT,
    FOREIGN KEY (production_order_id) REFERENCES production_order(id),
    FOREIGN KEY (production_stage_id) REFERENCES production_stage(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tabla: material_consumption
CREATE TABLE material_consumption (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    production_order_id BIGINT NOT NULL,
    raw_material_id BIGINT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (production_order_id) REFERENCES production_order(id),
    FOREIGN KEY (raw_material_id) REFERENCES raw_material(id)
);

-- Tabla: customer
CREATE TABLE customer (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(255),
    address TEXT
);

-- Tabla: orders
CREATE TABLE orders (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    number VARCHAR(255) NOT NULL UNIQUE,
    date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    customer_id BIGINT NOT NULL,
    is_ecommerce BOOLEAN NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

-- Tabla: order_item
CREATE TABLE order_item (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

-- Tabla: purchase_order
CREATE TABLE purchase_order (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    number VARCHAR(255) NOT NULL UNIQUE,
    date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    supplier_id BIGINT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);

-- Tabla: purchase_item
CREATE TABLE purchase_item (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    purchase_order_id BIGINT NOT NULL,
    raw_material_id BIGINT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (purchase_order_id) REFERENCES purchase_order(id),
    FOREIGN KEY (raw_material_id) REFERENCES raw_material(id)
);
