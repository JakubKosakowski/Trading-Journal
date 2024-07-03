CREATE SEQUENCE IF NOT EXISTS transactions_id
INCREMENT 1
START 1000;

CREATE SEQUENCE IF NOT EXISTS exit_tactics_id
INCREMENT 1
START 0;

CREATE TABLE IF NOT EXISTS transactions(
	id INTEGER NOT NULL DEFAULT NEXTVAL('transactions_id') PRIMARY KEY,
	stock_code VARCHAR(20) NOT NULL,
	quantity INTEGER NOT NULL,
	type_of_transaction VARCHAR(1) NOT NULL,
	entry DECIMAL(8,2) NOT NULL,
	entry_date DATE NOT NULL,
	entry_period_high DECIMAL(8,2) NOT NULL,
	entry_period_low DECIMAL(8,2) NOT NULL,
	exit DECIMAL(8, 2) NOT NULL,
	exit_date DATE NOT NULL,
	exit_period_high DECIMAL(8,2) NOT NULL,
	exit_period_low DECIMAL(8,2) NOT NULL,
	fee DECIMAL(8, 2) NOT NULL,
	profit_loss DECIMAL(10, 2) NOT NULL,
	net DECIMAL(10, 2) NOT NULL
)

CREATE TABLE IF NOT EXISTS exit_tactics(
	id INTEGER NOT NULL DEFAULT NEXTVAL('exit_tactics_id') PRIMARY KEY,
	exit_tactics TEXT NOT NULL 
)