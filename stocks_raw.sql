DROP TABLE IF EXISTS stocks_raw;

CREATE TABLE stocks_raw (
    ticker TEXT,
    close NUMERIC,
    date DATE,
    high NUMERIC,
    low NUMERIC,
    month TEXT,
    open NUMERIC,
    volume BIGINT
);

SELECT * FROM stocks_raw LIMIT 5;

CREATE TABLE stocks_clean AS
SELECT
    ticker AS symbol,
    date::DATE AS trade_date,
    open,
    high,
    low,
    close,
    volume
FROM stocks_raw
WHERE
    open IS NOT NULL
    AND high IS NOT NULL
    AND low IS NOT NULL
    AND close IS NOT NULL;


	--VERIFY CLEAN TABLE
	SELECT COUNT(*) FROM stocks_clean;
	
	SELECT * FROM stocks_clean LIMIT 5;

-- COMFIRM HOW MUCH DATA IS PRESENT
	SELECT COUNT(*) AS total_rows
	FROM stocks_clean;
	
	SELECT * FROM stocks_clean LIMIT 5;
	
-- SHOWS HOW MANY YEARS/MONTHS OF STOCK DATA
SELECT 
	MIN(trade_date) AS start_date,
	MAX(trade_date) AS end_date
FROM stocks_clean;

--NUMBER OF STOCK AVAILABLE
SELECT COUNT(DISTINCT symbol) AS total_stocks
FROM stocks_clean;

--shows top expensive stocks
SELECT
    symbol,
    ROUND(AVG(close), 2) AS avg_close_price
FROM stocks_clean
GROUP BY symbol
ORDER BY avg_close_price DESC
LIMIT 10;


--HIGHEST TRADING VOLUME STOCKS
SELECT
	symbol,
	trade_date,
	(high-low) AS daily_range
FROM stocks_clean
ORDER BY daily_range DESC
LIMIT 10;


	