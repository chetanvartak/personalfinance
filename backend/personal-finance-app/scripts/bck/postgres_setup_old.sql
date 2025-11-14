-- PostgreSQL setup script for personal-finance-app
--
-- This script will:
-- 1) create a role/user (pguser) and a database (personal_finance_dev)
-- 2) connect to the new database
-- 3) create the tables used by the application
--
-- NOTE: Running this file requires a superuser or a role with
-- privileges to create roles and databases. If you already have a
-- database and user, either edit this file (remove CREATE ROLE/DATABASE)
-- or run only the table creation section against your existing DB.

-- Adjust these values if desired
\echo 'Creating role and database (if they do not exist)'
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'pguser') THEN
       CREATE ROLE pguser WITH LOGIN PASSWORD 'pgpass';
   END IF;
EXCEPTION
   WHEN others THEN
       RAISE NOTICE 'Role creation skipped or failed: %', SQLERRM;
END
$$;

-- Create the database if it doesn't exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'personal_finance_dev') THEN
       PERFORM dblink_exec('dbname=postgres', $$CREATE DATABASE personal_finance_dev OWNER pguser$$);
   END IF;
EXCEPTION
   WHEN others THEN
       -- If dblink is not available (not installed) fallback to CREATE DATABASE directly
       BEGIN
           CREATE DATABASE personal_finance_dev OWNER pguser;
       EXCEPTION WHEN others THEN
           RAISE NOTICE 'Database creation skipped or failed: %', SQLERRM;
       END;
END
$$;

\echo 'Connecting to personal_finance_dev'
\connect personal_finance_dev

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username varchar(150) NOT NULL UNIQUE,
    email varchar(255) NOT NULL UNIQUE,
    hashed_password varchar(255) NOT NULL,
    is_active boolean NOT NULL DEFAULT true
);

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(150) NOT NULL UNIQUE
);

-- Create accounts table
CREATE TABLE IF NOT EXISTS accounts (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer REFERENCES users(id) ON DELETE CASCADE,
    name varchar(255) NOT NULL,
    balance double precision NOT NULL DEFAULT 0.0
);
CREATE INDEX IF NOT EXISTS idx_accounts_user_id ON accounts(user_id);

-- Create budgets table
CREATE TABLE IF NOT EXISTS budgets (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer REFERENCES users(id) ON DELETE CASCADE,
    name varchar(255),
    limit_amount double precision
);
CREATE INDEX IF NOT EXISTS idx_budgets_user_id ON budgets(user_id);

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    account_id integer REFERENCES accounts(id) ON DELETE CASCADE,
    category varchar(255),
    amount double precision,
    currency varchar(10) NOT NULL DEFAULT 'USD',
    created_at timestamp WITHOUT TIME ZONE NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_transactions_account_id ON transactions(account_id);

-- Grant privileges to the application role
GRANT ALL PRIVILEGES ON DATABASE personal_finance_dev TO pguser;
GRANT USAGE ON SCHEMA public TO pguser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO pguser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO pguser;

\echo 'Postgres setup complete.'
