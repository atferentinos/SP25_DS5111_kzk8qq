-- Combine all insights into final analysis table
SELECT 
    sp.symbol,
    sp.appearance_count,
    sp.avg_percent_change,
    CASE 
        WHEN MAX(dc.price) < 10 THEN 'Low Price'
        WHEN MAX(dc.price) >= 10 AND MAX(dc.price) < 50 THEN 'Mid Price'
        ELSE 'High Price'
    END as price_category,
    sp.week_performance,
    sp.volatility,
    sp.trading_volume,
    -- Flag recurring symbols (appeared 3+ times in the week)
    CASE WHEN sp.appearance_count >= 3 THEN TRUE ELSE FALSE END as recurring_flag
FROM {{ ref('int_symbol_performance') }} sp
JOIN {{ ref('int_daily_combined') }} dc ON sp.symbol = dc.symbol
GROUP BY 
    sp.symbol, 
    sp.appearance_count,
    sp.avg_percent_change, 
    sp.week_performance,
    sp.volatility,
    sp.trading_volume
