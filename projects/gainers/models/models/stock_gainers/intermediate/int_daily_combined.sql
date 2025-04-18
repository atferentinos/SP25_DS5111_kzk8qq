-- Combine all daily gainers data
SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    date,
    source
FROM {{ source('stock_data', 'raw_gainers') }}
