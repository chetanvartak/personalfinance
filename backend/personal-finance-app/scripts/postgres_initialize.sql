-- Clear all tables to start fresh
DELETE FROM transactions;
DELETE FROM accounts;
DELETE FROM categories;
DELETE FROM institutions;
DELETE FROM users;
DELETE FROM transaction_types;
DELETE FROM account_types;
DELETE FROM institution_types;

-- Reset all sequences
ALTER SEQUENCE institution_types_id_seq RESTART WITH 1;
ALTER SEQUENCE account_types_id_seq RESTART WITH 1;
ALTER SEQUENCE transaction_types_id_seq RESTART WITH 1;
ALTER SEQUENCE users_id_seq RESTART WITH 1;
ALTER SEQUENCE institutions_id_seq RESTART WITH 1;
ALTER SEQUENCE accounts_id_seq RESTART WITH 1;
ALTER SEQUENCE categories_id_seq RESTART WITH 1;
ALTER SEQUENCE transactions_id_seq RESTART WITH 1;

-- Seed the type tables with the expected values
INSERT INTO institution_types (name) VALUES
    ('bank'), ('investment'), ('credit'), ('loan'), ('other')
ON CONFLICT (name) DO NOTHING;

INSERT INTO account_types (name) VALUES
    ('checking'), ('savings'), ('credit_card'), ('investment'), ('loan'), ('retirement'),
    ('hsa'), ('health_insurance'), ('utility_gas'), ('utility_electric'), ('utility_water'),
    ('utility_trash'), ('telecom_internet'), ('telecom_mobile'), ('other')
ON CONFLICT (name) DO NOTHING;

INSERT INTO transaction_types (name) VALUES
    ('deposit'), ('withdrawal'), ('payment'), ('transfer'), ('investment'), ('fee'), ('interest')
ON CONFLICT (name) DO NOTHING;

INSERT INTO public.users(
	username, email, password_hash, first_name, last_name, date_of_birth, created_at, updated_at)
	VALUES ( 'chetan', 'chetan@example.com', 'hashed_password', 'Chetan', 'Vartak', '1971-08-01', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Insert parent categories
INSERT INTO categories (name, parent_id) VALUES
    ('Income', NULL),
    ('Expense', NULL),
    ('Other', NULL);

-- Insert child categories for Income
INSERT INTO categories (name, parent_id) VALUES
    ('Consulting', (SELECT id FROM categories WHERE name='Income')),
    ('Deposits', (SELECT id FROM categories WHERE name='Income')),
    ('Dividends Received', (SELECT id FROM categories WHERE name='Income')),
    ('Dividends Received (tax-advantaged)', (SELECT id FROM categories WHERE name='Income')),
    ('Interest', (SELECT id FROM categories WHERE name='Income')),
    ('Investment Income', (SELECT id FROM categories WHERE name='Income')),
    ('Other Income', (SELECT id FROM categories WHERE name='Income')),
    ('Paychecks/Salary', (SELECT id FROM categories WHERE name='Income')),
    ('Refunds & Reimbursements', (SELECT id FROM categories WHERE name='Income')),
    ('Retirement Income', (SELECT id FROM categories WHERE name='Income')),
    ('Rewards', (SELECT id FROM categories WHERE name='Income')),
    ('Sales', (SELECT id FROM categories WHERE name='Income')),
    ('Services', (SELECT id FROM categories WHERE name='Income'));

-- Insert child categories for Expense
INSERT INTO categories (name, parent_id) VALUES
    ('Advertising', (SELECT id FROM categories WHERE name='Expense')),
    ('Advisory Fee', (SELECT id FROM categories WHERE name='Expense')),
    ('ATM/Cash', (SELECT id FROM categories WHERE name='Expense')),
    ('Automotive', (SELECT id FROM categories WHERE name='Expense')),
    ('Business Miscellaneous', (SELECT id FROM categories WHERE name='Expense')),
    ('Cable/Satellite', (SELECT id FROM categories WHERE name='Expense')),
    ('Charitable Giving', (SELECT id FROM categories WHERE name='Expense')),
    ('Checks', (SELECT id FROM categories WHERE name='Expense')),
    ('Child/Dependent', (SELECT id FROM categories WHERE name='Expense')),
    ('Clothing/Shoes', (SELECT id FROM categories WHERE name='Expense')),
    ('Dues & Subscriptions', (SELECT id FROM categories WHERE name='Expense')),
    ('Education', (SELECT id FROM categories WHERE name='Expense')),
    ('Electronics', (SELECT id FROM categories WHERE name='Expense')),
    ('Entertainment', (SELECT id FROM categories WHERE name='Expense')),
    ('Gasoline/Fuel', (SELECT id FROM categories WHERE name='Expense')),
    ('General Merchandise', (SELECT id FROM categories WHERE name='Expense')),
    ('Gifts', (SELECT id FROM categories WHERE name='Expense')),
    ('Groceries', (SELECT id FROM categories WHERE name='Expense')),
    ('Healthcare/Medical', (SELECT id FROM categories WHERE name='Expense')),
    ('Hobbies', (SELECT id FROM categories WHERE name='Expense')),
    ('Home HOA', (SELECT id FROM categories WHERE name='Expense')),
    ('Home Improvement', (SELECT id FROM categories WHERE name='Expense')),
    ('Home Maintenance', (SELECT id FROM categories WHERE name='Expense')),
    ('Insurance', (SELECT id FROM categories WHERE name='Expense')),
    ('Loans', (SELECT id FROM categories WHERE name='Expense')),
    ('Mortgages', (SELECT id FROM categories WHERE name='Expense')),
    ('Office Maintenance', (SELECT id FROM categories WHERE name='Expense')),
    ('Office Supplies', (SELECT id FROM categories WHERE name='Expense')),
    ('Online Services', (SELECT id FROM categories WHERE name='Expense')),
    ('Other Bills', (SELECT id FROM categories WHERE name='Expense')),
    ('Other Expenses', (SELECT id FROM categories WHERE name='Expense')),
    ('Personal Care', (SELECT id FROM categories WHERE name='Expense')),
    ('Pets/Pet Care', (SELECT id FROM categories WHERE name='Expense')),
    ('Postage & Shipping', (SELECT id FROM categories WHERE name='Expense')),
    ('Printing', (SELECT id FROM categories WHERE name='Expense')),
    ('Rent', (SELECT id FROM categories WHERE name='Expense')),
    ('Restaurants', (SELECT id FROM categories WHERE name='Expense')),
    ('Service Charges/Fees', (SELECT id FROM categories WHERE name='Expense')),
    ('Taxes', (SELECT id FROM categories WHERE name='Expense')),
    ('Telephone', (SELECT id FROM categories WHERE name='Expense')),
    ('Travel', (SELECT id FROM categories WHERE name='Expense')),
    ('Utilities', (SELECT id FROM categories WHERE name='Expense')),
    ('Wages Paid', (SELECT id FROM categories WHERE name='Expense'));

-- Insert child categories for Other
INSERT INTO categories (name, parent_id) VALUES
    ('Allocated Excess Cash', (SELECT id FROM categories WHERE name='Other')),
    ('Cash Raised', (SELECT id FROM categories WHERE name='Other')),
    ('Client Request', (SELECT id FROM categories WHERE name='Other')),
    ('Credit Card Payments', (SELECT id FROM categories WHERE name='Other')),
    ('Diversified Transferred-in Securities', (SELECT id FROM categories WHERE name='Other')),
    ('Expense Reimbursement', (SELECT id FROM categories WHERE name='Other')),
    ('General Rebalance', (SELECT id FROM categories WHERE name='Other')),
    ('Not Traded', (SELECT id FROM categories WHERE name='Other')),
    ('Personal Strategy Implementation', (SELECT id FROM categories WHERE name='Other')),
    ('Portfolio Management', (SELECT id FROM categories WHERE name='Other')),
    ('Retirement Contributions', (SELECT id FROM categories WHERE name='Other')),
    ('Savings', (SELECT id FROM categories WHERE name='Other')),
    ('Securities Trades', (SELECT id FROM categories WHERE name='Other')),
    ('Strategy Change', (SELECT id FROM categories WHERE name='Other')),
    ('Tax Location', (SELECT id FROM categories WHERE name='Other')),
    ('Tax Loss Harvesting', (SELECT id FROM categories WHERE name='Other')),
    ('Transfers', (SELECT id FROM categories WHERE name='Other')),
    ('Uncategorized', (SELECT id FROM categories WHERE name='Other'));

-------------------------------------
-- Insert institutions using institution_type_id foreign key
INSERT INTO institutions (name, institution_type_id, website) VALUES
('Empower', (SELECT id FROM institution_types WHERE name='investment'), 'https://empower.com'),
('Betterment', (SELECT id FROM institution_types WHERE name='bank'), 'https://betterment.com'),
('Chase', (SELECT id FROM institution_types WHERE name='bank'), 'https://chase.com'),
('Fidelity Investments', (SELECT id FROM institution_types WHERE name='investment'), 'https://fidelity.com'),
('Vanguard', (SELECT id FROM institution_types WHERE name='investment'), 'https://vanguard.com'),
('American Express Cards', (SELECT id FROM institution_types WHERE name='credit'), 'https://americanexpress.com'),
('Citibank', (SELECT id FROM institution_types WHERE name='credit'), 'https://citi.com'),
('Target Credit Card', (SELECT id FROM institution_types WHERE name='credit'), 'https://target.com'),
('T. Rowe Price', (SELECT id FROM institution_types WHERE name='investment'), 'https://troweprice.com'),
('Home', (SELECT id FROM institution_types WHERE name='other'), 'https://empower.com'); -- Home address as asset
-- Insert dummy user_id (e.g., 1) for all accounts below
-- Use institution_id from above: order matches previous insert (1 = Empower, etc.)
-- All currency assumed 'USD'

-- Empower Accounts (using account_type_id foreign key)
INSERT INTO accounts (user_id, institution_id, account_type_id, account_name, account_number_last4, balance, currency, status) VALUES
(1, 1, (SELECT id FROM account_types WHERE name='checking'), 'Cash ending in 6197', '6197', 7033.67, 'USD', 'active'),
(1, 1, (SELECT id FROM account_types WHERE name='retirement'), 'CHETAN S VARTAK RO IRA', '0000', 788068.59, 'USD', 'active'),
(1, 1, (SELECT id FROM account_types WHERE name='retirement'), 'CHETAN S VARTAK ROTH IRA', '0000', 33756.44, 'USD', 'active'),
(1, 1, (SELECT id FROM account_types WHERE name='investment'), 'Vartak Family Revocable Trust', '0000', 278022.85, 'USD', 'active'),
(1, 10, (SELECT id FROM account_types WHERE name='retirement'), 'SOGETI USA 401(K) PROFIT SHARING PLAN', '0000', 233544.83, 'USD', 'active');

-- Bank/Cash
INSERT INTO accounts (user_id, institution_id, account_type_id, account_name, account_number_last4, balance, currency, status) VALUES
(1, 2, (SELECT id FROM account_types WHERE name='checking'), 'Checking - Ending in 1983', '1983', 1150.00, 'USD', 'active'),
(1, 3, (SELECT id FROM account_types WHERE name='savings'), 'Chase Savings - Ending in 2079', '2079', 215.78, 'USD', 'active'),
(1, 3, (SELECT id FROM account_types WHERE name='checking'), 'Total Checking - Ending in 8490', '8490', 14993.50, 'USD', 'active');

-- Investment
INSERT INTO accounts (user_id, institution_id, account_type_id, account_name, account_number_last4, balance, currency, status) VALUES
(1, 2, (SELECT id FROM account_types WHERE name='investment'), 'General Investing Trust Taxable - Ending in 5224', '5224', 10269.63, 'USD', 'active'),
(1, 4, (SELECT id FROM account_types WHERE name='investment'), 'Cash Management (joint Wros) - Ending in 3717', '3717', 142.73, 'USD', 'active'),
(1, 4, (SELECT id FROM account_types WHERE name='investment'), 'Individual Youth Account - Ending in 4963', '4963', 2375.90, 'USD', 'active');

-- Credit Cards
INSERT INTO accounts (user_id, institution_id, account_type_id, account_name, account_number_last4, balance, currency, status) VALUES
(1, 6, (SELECT id FROM account_types WHERE name='credit_card'), 'Blue Cash Preferred - Ending in 1003', '1003', -348.47, 'USD', 'active'),
(1, 7, (SELECT id FROM account_types WHERE name='credit_card'), 'Costco Anywhere Visa Card By Citi - Ending in 1323', '1323', -1616.43, 'USD', 'active'),
(1, 4, (SELECT id FROM account_types WHERE name='credit_card'), 'Fidelity Rewards Visa Signature Card - Ending in 6962', '6962', -1577.47, 'USD', 'active'),
(1, 8, (SELECT id FROM account_types WHERE name='credit_card'), 'Target Circle Card - Ending in 8108', '8108', -98.77, 'USD', 'active');

-- Loan/Mortgage
INSERT INTO accounts (user_id, institution_id, account_type_id, account_name, account_number_last4, balance, currency, status) VALUES
(1, 3, (SELECT id FROM account_types WHERE name='loan'), 'Mortgage Loan - Ending in 4078', '4078', -195490.66, 'USD', 'active');

-- Vanguard example (investment/retirement)
INSERT INTO accounts (user_id, institution_id, account_type_id, account_name, account_number_last4, balance, currency, status) VALUES
(1, 5, (SELECT id FROM account_types WHERE name='investment'), 'Sejal C Vartak Individual 529 College Savings Account - Ending in 01', '01', 139675.65, 'USD', 'active');

-- Home Asset (closed)
INSERT INTO accounts (user_id, institution_id, account_type_id, account_name, account_number_last4, balance, currency, status) VALUES
(1, 10, (SELECT id FROM account_types WHERE name='other'), '273 Valero Circle', '0000', 0.00, 'USD', 'closed');


-------------------------------------
-- Sample transaction inserts based on some of the recent transactions shown in the browser

INSERT INTO transactions (
    account_id, date, amount, transaction_type_id, category_id, description, related_account_id, created_at
) VALUES
-- Income transactions
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-14 09:00:00-08', 5000.00, (SELECT id FROM transaction_types WHERE name='deposit'), (SELECT id FROM categories WHERE name='Paychecks/Salary'), 'Monthly Salary Deposit', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-13 10:00:00-08', 250.00, (SELECT id FROM transaction_types WHERE name='deposit'), (SELECT id FROM categories WHERE name='Rewards'), 'Rewards Cash Back', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Vartak Family Revocable Trust'), '2025-11-13 12:00:00-08', 15.08, (SELECT id FROM transaction_types WHERE name='interest'), (SELECT id FROM categories WHERE name='Dividends Received'), 'AAPL - Apple Inc Dividend', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='CHETAN S VARTAK RO IRA'), '2025-11-12 14:00:00-08', 45.32, (SELECT id FROM transaction_types WHERE name='interest'), (SELECT id FROM categories WHERE name='Interest'), 'Interest Income', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-11 11:00:00-08', 1200.00, (SELECT id FROM transaction_types WHERE name='deposit'), (SELECT id FROM categories WHERE name='Refunds & Reimbursements'), 'Project Reimbursement', NULL, CURRENT_TIMESTAMP),

-- Expense transactions - Groceries
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-14 08:30:00-08', -45.67, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Groceries'), 'Safeway Grocery Store', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-13 19:00:00-08', -78.92, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Groceries'), 'Whole Foods Market', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-12 10:15:00-08', -32.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Groceries'), 'Trader Joes', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Costco Anywhere Visa Card By Citi - Ending in 1323'), '2025-11-11 14:30:00-08', -125.43, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Groceries'), 'Costco Wholesale', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-10 17:00:00-08', -22.15, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Groceries'), 'Local Farmer Market', NULL, CURRENT_TIMESTAMP),

-- Restaurants
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 12:30:00-08', -42.80, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Restaurants'), 'Chipotle Mexican Grill', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-13 19:45:00-08', -85.33, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Restaurants'), 'The Italian Place - Dinner', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-12 12:00:00-08', -15.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Restaurants'), 'Starbucks Coffee', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Fidelity Rewards Visa Signature Card - Ending in 6962'), '2025-11-11 18:30:00-08', -125.60, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Restaurants'), 'Japanese Restaurant Sushi', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-10 20:00:00-08', -55.44, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Restaurants'), 'Pizza Palace Delivery', NULL, CURRENT_TIMESTAMP),

-- Gasoline/Fuel
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 07:00:00-08', -62.34, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Gasoline/Fuel'), 'Shell Gas Station', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-12 16:45:00-08', -58.91, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Gasoline/Fuel'), 'Chevron Fuel', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-10 09:30:00-08', -52.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Gasoline/Fuel'), 'Exxon Mobil Gas', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-09 17:00:00-08', -48.77, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Gasoline/Fuel'), 'Murphy USA Gas Station', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Costco Anywhere Visa Card By Citi - Ending in 1323'), '2025-11-08 14:30:00-08', -71.25, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Gasoline/Fuel'), 'Costco Gas', NULL, CURRENT_TIMESTAMP),

-- Utilities
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-12 20:00:00-08', -145.67, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Utilities'), 'Southern California Edison - Electric Bill', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-11 10:00:00-08', -89.50, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Utilities'), 'Water Department - Water Bill', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-10 15:00:00-08', -120.00, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Utilities'), 'Gas Company - Natural Gas Bill', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-09 11:00:00-08', -99.99, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Utilities'), 'Internet Provider - Broadband', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-08 09:00:00-08', -75.00, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Telephone'), 'Mobile Phone Provider - Cellular Bill', NULL, CURRENT_TIMESTAMP),

-- Healthcare/Medical
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-14 11:30:00-08', -250.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Healthcare/Medical'), 'Dr. Johnson Medical Office - Copay', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-13 14:00:00-08', -125.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Healthcare/Medical'), 'CVS Pharmacy - Prescriptions', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-11 10:00:00-08', -45.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Healthcare/Medical'), 'Walgreens - Medical Supplies', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Fidelity Rewards Visa Signature Card - Ending in 6962'), '2025-11-09 09:00:00-08', -380.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Healthcare/Medical'), 'Dental Office - Cleaning & Exam', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-07 16:00:00-08', -89.75, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Healthcare/Medical'), 'Vision Center - Eye Exam', NULL, CURRENT_TIMESTAMP),

-- Entertainment
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 18:00:00-08', -35.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Entertainment'), 'Cinemark Movie Theater', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-13 20:30:00-08', -19.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Entertainment'), 'Netflix Subscription', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-12 19:00:00-08', -14.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Entertainment'), 'Spotify Premium', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-11 17:00:00-08', -28.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Entertainment'), 'Paramount+ Movie Streaming', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Costco Anywhere Visa Card By Citi - Ending in 1323'), '2025-11-10 19:30:00-08', -55.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Entertainment'), 'Concert Tickets - Live Event', NULL, CURRENT_TIMESTAMP),

-- Clothing/Shoes
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 15:00:00-08', -89.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Clothing/Shoes'), 'Target Department Store', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-12 14:30:00-08', -120.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Clothing/Shoes'), 'Nike Store - Athletic Shoes', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Fidelity Rewards Visa Signature Card - Ending in 6962'), '2025-11-11 13:00:00-08', -75.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Clothing/Shoes'), 'Gap Clothing', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-10 16:00:00-08', -45.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Clothing/Shoes'), 'Local Thrift Store', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-09 11:00:00-08', -135.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Clothing/Shoes'), 'Macys Department Store', NULL, CURRENT_TIMESTAMP),

-- Personal Care
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 10:00:00-08', -65.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Personal Care'), 'Hair Salon - Haircut & Style', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-13 09:00:00-08', -32.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Personal Care'), 'Barbershop - Grooming', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-11 15:00:00-08', -28.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Personal Care'), 'Dry Cleaning - Clothes', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Fidelity Rewards Visa Signature Card - Ending in 6962'), '2025-11-10 10:00:00-08', -95.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Personal Care'), 'Spa Day - Massage & Facial', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-09 14:00:00-08', -22.75, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Personal Care'), 'Beauty Supply Store', NULL, CURRENT_TIMESTAMP),

-- Pets/Pet Care
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 09:00:00-08', -85.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Pets/Pet Care'), 'Veterinary Clinic - Pet Checkup', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-12 11:00:00-08', -45.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Pets/Pet Care'), 'Pet Supply Store - Food & Toys', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-10 15:30:00-08', -120.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Pets/Pet Care'), 'Dog Grooming Salon', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-08 10:00:00-08', -35.75, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Pets/Pet Care'), 'Petco - Pet Supplies', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Costco Anywhere Visa Card By Citi - Ending in 1323'), '2025-11-07 09:00:00-08', -200.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Pets/Pet Care'), 'Pet Insurance Annual Premium', NULL, CURRENT_TIMESTAMP),

-- Electronics
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 12:00:00-08', -450.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Electronics'), 'Best Buy - Electronics', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-12 09:00:00-08', -29.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Electronics'), 'Amazon - USB Cable', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Fidelity Rewards Visa Signature Card - Ending in 6962'), '2025-11-10 14:00:00-08', -350.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Electronics'), 'Apple Store - iPhone Accessories', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-08 11:00:00-08', -89.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Electronics'), 'Best Buy - Computer Monitor', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-06 15:00:00-08', -199.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Electronics'), 'Amazon - Smart Speaker', NULL, CURRENT_TIMESTAMP),

-- Travel
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 06:00:00-08', -375.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Travel'), 'Delta Airlines - Flight Ticket', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-13 11:00:00-08', -225.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Travel'), 'Hotel Resort - Accommodation', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Fidelity Rewards Visa Signature Card - Ending in 6962'), '2025-11-12 16:00:00-08', -85.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Travel'), 'Uber Car Rental', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-11 13:00:00-08', -45.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Travel'), 'Parking Fee - Downtown', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-10 12:00:00-08', -150.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Travel'), 'Expedia - Vacation Package', NULL, CURRENT_TIMESTAMP),

-- Home Improvement & Maintenance
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 08:00:00-08', -250.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Home Improvement'), 'Home Depot - Building Materials', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-12 14:00:00-08', -500.00, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Home Maintenance'), 'Plumber Service Call - Repairs', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Fidelity Rewards Visa Signature Card - Ending in 6962'), '2025-11-11 10:00:00-08', -300.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Home Maintenance'), 'Electrician - Wiring Repair', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-09 09:00:00-08', -85.50, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Home Improvement'), 'Lowes - Paint & Supplies', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-07 15:00:00-08', -150.00, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Home Maintenance'), 'HVAC Service - AC Maintenance', NULL, CURRENT_TIMESTAMP),

-- Dues & Subscriptions
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-14 05:00:00-08', -120.00, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Dues & Subscriptions'), 'Gym Membership - Annual Fee', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-13 12:00:00-08', -15.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Dues & Subscriptions'), 'Apple Music Subscription', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Costco Anywhere Visa Card By Citi - Ending in 1323'), '2025-11-12 11:00:00-08', -60.00, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Dues & Subscriptions'), 'Costco Membership Renewal', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-10 14:00:00-08', -9.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Dues & Subscriptions'), 'Adobe Creative Cloud Monthly', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-08 10:00:00-08', -49.99, (SELECT id FROM transaction_types WHERE name='withdrawal'), (SELECT id FROM categories WHERE name='Dues & Subscriptions'), 'Professional Software Subscription', NULL, CURRENT_TIMESTAMP),

-- Transfers
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-14 10:00:00-08', -2000.00, (SELECT id FROM transaction_types WHERE name='transfer'), (SELECT id FROM categories WHERE name='Transfers'), 'Transfer to Savings Account', 2, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-13 09:00:00-08', 2000.00, (SELECT id FROM transaction_types WHERE name='transfer'), (SELECT id FROM categories WHERE name='Transfers'), 'Transfer from Checking Account', 1, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='CHETAN S VARTAK RO IRA'), '2025-11-12 11:00:00-08', -500.00, (SELECT id FROM transaction_types WHERE name='transfer'), (SELECT id FROM categories WHERE name='Transfers'), 'Transfer to Investment Account', 8, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Individual Youth Account - Ending in 4963'), '2025-11-11 15:00:00-08', 500.00, (SELECT id FROM transaction_types WHERE name='transfer'), (SELECT id FROM categories WHERE name='Transfers'), 'Transfer from Retirement', 7, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-10 12:00:00-08', -1500.00, (SELECT id FROM transaction_types WHERE name='payment'), (SELECT id FROM categories WHERE name='Credit Card Payments'), 'Credit Card Payment - Chase', 1, CURRENT_TIMESTAMP),

-- Investment Transactions
((SELECT id FROM accounts WHERE account_name='CHETAN S VARTAK RO IRA'), '2025-11-14 15:00:00-08', 150.00, (SELECT id FROM transaction_types WHERE name='investment'), (SELECT id FROM categories WHERE name='Securities Trades'), 'Buy: VTSAX - Total Stock Market ETF', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Vartak Family Revocable Trust'), '2025-11-13 14:00:00-08', -200.00, (SELECT id FROM transaction_types WHERE name='investment'), (SELECT id FROM categories WHERE name='Securities Trades'), 'Sell: BRK.B - Berkshire Hathaway', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Individual Youth Account - Ending in 4963'), '2025-11-12 10:00:00-08', 300.00, (SELECT id FROM transaction_types WHERE name='investment'), (SELECT id FROM categories WHERE name='Securities Trades'), 'Buy: VOO - S&P 500 Index', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='CHETAN S VARTAK RO IRA'), '2025-11-11 09:00:00-08', -100.00, (SELECT id FROM transaction_types WHERE name='investment'), (SELECT id FROM categories WHERE name='Securities Trades'), 'Sell: MSFT - Microsoft', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Vartak Family Revocable Trust'), '2025-11-10 13:00:00-08', 250.00, (SELECT id FROM transaction_types WHERE name='investment'), (SELECT id FROM categories WHERE name='Securities Trades'), 'Buy: VB - Small Cap Value ETF', NULL, CURRENT_TIMESTAMP),

-- Service Charges/Fees
((SELECT id FROM accounts WHERE account_name='Total Checking - Ending in 8490'), '2025-11-14 03:00:00-08', -10.00, (SELECT id FROM transaction_types WHERE name='fee'), (SELECT id FROM categories WHERE name='Service Charges/Fees'), 'Monthly Account Maintenance Fee', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Blue Cash Preferred - Ending in 1003'), '2025-11-13 03:00:00-08', -5.00, (SELECT id FROM transaction_types WHERE name='fee'), (SELECT id FROM categories WHERE name='Service Charges/Fees'), 'Credit Card Annual Fee', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Cash ending in 6197'), '2025-11-12 03:00:00-08', -2.50, (SELECT id FROM transaction_types WHERE name='fee'), (SELECT id FROM categories WHERE name='Service Charges/Fees'), 'ATM Withdrawal Fee - Out of Network', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Vartak Family Revocable Trust'), '2025-11-11 03:00:00-08', -50.00, (SELECT id FROM transaction_types WHERE name='fee'), (SELECT id FROM categories WHERE name='Advisory Fee'), 'Investment Advisory Fee', NULL, CURRENT_TIMESTAMP),
((SELECT id FROM accounts WHERE account_name='Target Circle Card - Ending in 8108'), '2025-11-10 03:00:00-08', -0.00, (SELECT id FROM transaction_types WHERE name='fee'), (SELECT id FROM categories WHERE name='Service Charges/Fees'), 'No Fee - Card Partner Benefit', NULL, CURRENT_TIMESTAMP);

-- Add more as needed following the pattern above.
