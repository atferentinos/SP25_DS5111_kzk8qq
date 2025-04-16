{{ config(
    materialized='table'
) }}

-- This model develops day-specific trading strategies based on historical patterns
-- Identifies which days show the best performance characteristics for different trading approaches

WITH day_stats AS (
    SELECT
        dow.day_of_week,
        dow.gainer_count,
        dow.avg_change_percent,
        dow.max_change_percent,
        dow.distinct_dates
    FROM {{ ref('int_day_of_week_stats') }} dow
),

day_recurring AS (
    SELECT
        gc.day_of_week,
        sf.symbol,
        sf.appearance_count
    FROM {{ ref('gainers_consolidated') }} gc
    JOIN {{ ref('int_symbol_frequency') }} sf ON gc.symbol = sf.symbol
    WHERE sf.appearance_count > 1
)

SELECT
    ds.day_of_week,
    -- Calculate average gainers per day
    ds.gainer_count / NULLIF(ds.distinct_dates, 0) AS avg_gainers_per_day,
    ds.avg_change_percent,
    ds.max_change_percent,
    -- Calculate percentage of gainers that are recurring symbols
    COUNT(DISTINCT dr.symbol) AS recurring_symbols_count,
    (COUNT(DISTINCT dr.symbol) / NULLIF(COUNT(DISTINCT CASE WHEN dr.symbol IS NOT NULL THEN dr.symbol ELSE NULL END) + 
                                  COUNT(DISTINCT CASE WHEN dr.symbol IS NULL THEN dr.symbol ELSE NULL END), 0)) * 100 AS repeat_percentage,
    -- Volume trend (placeholder since we don't have volume data)
    CASE
        WHEN ds.avg_change_percent > 5 THEN 'High Activity Day'
        WHEN ds.avg_change_percent > 3 THEN 'Moderate Activity Day'
        ELSE 'Low Activity Day'
    END AS activity_level,
    -- Trading strategy recommendations by day
    CASE
        WHEN ds.day_of_week = 'Monday' AND ds.avg_change_percent > 5 THEN 'Monday Momentum Strategy'
        WHEN ds.day_of_week = 'Friday' AND ds.avg_change_percent > 4 THEN 'Weekend Holding Strategy'
        WHEN ds.avg_change_percent > 6 THEN 'Aggressive Day Trading'
        WHEN ds.avg_change_percent > 4 THEN 'Selective Trading'
        ELSE 'Conservative Trading'
    END AS trading_strategy
FROM day_stats ds
LEFT JOIN day_recurring dr ON ds.day_of_week = dr.day_of_week
GROUP BY 
    ds.day_of_week, 
    ds.gainer_count, 
    ds.avg_change_percent, 
    ds.max_change_percent, 
    ds.distinct_dates
ORDER BY 
    CASE 
        WHEN ds.day_of_week = 'Monday' THEN 1
        WHEN ds.day_of_week = 'Tuesday' THEN 2
        WHEN ds.day_of_week = 'Wednesday' THEN 3
        WHEN ds.day_of_week = 'Thursday' THEN 4
        WHEN ds.day_of_week = 'Friday' THEN 5
        WHEN ds.day_of_week = 'Saturday' THEN 6
        WHEN ds.day_of_week = 'Sunday' THEN 7
    END
