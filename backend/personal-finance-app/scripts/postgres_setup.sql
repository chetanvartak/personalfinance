CREATE DATABASE personalfinance
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


-- TYPE TABLES
-- Separate lookup tables for institution, account and transaction types.
CREATE TABLE IF NOT EXISTS institution_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS account_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS transaction_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- MAIN TABLES
-- USERS
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- ACCOUNT PROVIDERS (Banks, Credit Cards, Investment Firms)
CREATE TABLE institutions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    institution_type_id INTEGER REFERENCES institution_types(id),
    website VARCHAR(255)
);

-- ACCOUNTS (Bank, Investment, Credit Card, Loan)
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    institution_id INTEGER REFERENCES institutions(id),
    account_type_id INTEGER REFERENCES account_types(id),
    account_name VARCHAR(255) UNIQUE NOT NULL,
    account_number_last4 VARCHAR(4),
    balance NUMERIC(18, 2) DEFAULT 0,
    currency VARCHAR(10) DEFAULT 'USD',
    opened_date DATE,
    closed_date DATE,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    parent_id INTEGER REFERENCES categories(id) ON DELETE SET NULL
);

-- TRANSACTIONS (Spending, Deposits, Credit, Investments)
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    account_id INTEGER REFERENCES accounts(id),
    date TIMESTAMPTZ,
    amount NUMERIC(18,2) NOT NULL,
    transaction_type_id INTEGER REFERENCES transaction_types(id),
    category_id INTEGER REFERENCES categories(id),
    description TEXT,
    related_account_id INTEGER REFERENCES accounts(id),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_transaction UNIQUE (account_id, date, amount, description)
);
