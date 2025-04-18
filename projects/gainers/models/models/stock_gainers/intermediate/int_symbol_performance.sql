-- Rewritten version without nested aggregates
WITH dates AS (
  SELECT 
    sf.symbol,
    MIN(rc.date) as min_date,
    MAX(rc.date) as max_date
  FROM {{ ref('int_symbol_frequency') }} sf
  LEFT JOIN {{ source('stock_data', 'raw_candlestick') }} rc ON sf.symbol = rc.symbol
  WHERE rc.date BETWEEN sf.first_appearance AND sf.last_appearance
  GROUP BY sf.symbol
),
first_prices AS (
  SELECT 
    d.symbol,
    rc.open as first_open
  FROM dates d
  LEFT JOIN {{ source('stock_data', 'raw_candlestick') }} rc 
    ON d.symbol = rc.symbol AND d.min_date = rc.date
),
last_prices AS (
  SELECT 
    d.symbol,
    rc.close as last_close
  FROM dates d
  LEFT JOIN {{ source('stock_data', 'raw_candlestick') }} rc 
    ON d.symbol = rc.symbol AND d.max_date = rc.date
)
SELECT 
    sf.symbol,
    sf.appearance_count,
    sf.avg_percent_change,
    -- Calculate week performance safely
    CASE 
      WHEN fp.first_open > 0 THEN (lp.last_close / fp.first_open - 1) * 100 
      ELSE NULL 
    END as week_performance,
    -- Calculate volatility
    STDDEV_SAMP(CASE WHEN rc.open != 0 THEN (rc.close - rc.open) / rc.open * 100 ELSE 0 END) as volatility,
    AVG(rc.volume) as trading_volume
FROM {{ ref('int_symbol_frequency') }} sf
LEFT JOIN {{ source('stock_data', 'raw_candlestick') }} rc ON sf.symbol = rc.symbol
LEFT JOIN first_prices fp ON sf.symbol = fp.symbol
LEFT JOIN last_prices lp ON sf.symbol = lp.symbol
WHERE (rc.date BETWEEN sf.first_appearance AND sf.last_appearance) OR rc.date IS NULL
GROUP BY sf.symbol, sf.appearance_count, sf.avg_percent_change, 
         CASE WHEN fp.first_open > 0 THEN (lp.last_close / fp.first_open - 1) * 100 ELSE NULL END
