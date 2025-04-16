{{ config(
    materialized='table'
) }}



WITH day_stats AS (
    SELECT
        dow.day_of_week,
        dow.gainer_count,
        dow.avg_change_percent,
        dow.max_change_percent,
        dow.distinct_dates,
        cg.symbol,
        sf.appearance_count
    FROM {{ ref('int_day_of_week_stats') }} dow
    JOIN {{ ref('stg_consolidated_gainers') }} cg ON dow.day_of_week = cg.day_of_week
    LEFT JOIN {{ ref('int_symbol_frequency') }} sf ON cg.symbol = sf.symbol
)

SELECT
    day_of_week,
    -- Calculate average gainers per day
    gainer_count / NULLIF(distinct_dates, 0) AS avg_gainers_per_day,
    avg_change_percent,
    -- Calculate percentage of gainers that are recurring symbols
    (COUNT(DISTINCT CASE WHEN appearance_count > 1 THEN symbol END) / 
     NULLIF(COUNT(DISTINCT symbol), 0)) * 100 AS repeat_percentage,
    -- Volume trend (placeholder - would use actual volume data if available)
    CASE
        WHEN avg_change_percent > 5 THEN 'High Volume Day'
        WHEN avg_change_percent > 3 THEN 'Moderate Volume Day'
        ELSE 'Low Volume Day'
    END AS volume_trend,
    -- Trading strategy recommendations by day
    CASE
        WHEN day_of_week = 'Monday' AND avg_change_percent > 5 THEN 'Monday Momentum Strategy'
        WHEN day_of_week = 'Friday' AND avg_change_percent > 4 THEN 'Weekend Holding Strategy'
        WHEN avg_change_percent > 6 THEN 'Aggressive Day Trading'
        WHEN avg_change_percent > 4 THEN 'Selective Trading'
        ELSE 'Conservative Trading'
    END AS trading_strategy
FROM day_stats
GROUP BY 
    day_of_week, 
    gainer_count, 
    avg_change_percent, 
    max_change_percent, 
    distinct_dates
ORDER BY 
    CASE 
        WHEN day_of_week = 'Monday' THEN 1
        WHEN day_of_week = 'Tuesday' THEN 2
        WHEN day_of_week = 'Wednesday' THEN 3
        WHEN day_of_week = 'Thursday' THEN 4
        WHEN day_of_week = 'Friday' THEN 5
    END
