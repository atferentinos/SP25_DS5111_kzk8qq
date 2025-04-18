-- Create price distribution analysis
SELECT 
    CASE 
        WHEN price < 10 THEN 'Under $10'
        WHEN price >= 10 AND price < 25 THEN '$10-$25'
        WHEN price >= 25 AND price < 50 THEN '$25-$50'
        WHEN price >= 50 AND price < 100 THEN '$50-$100'
        ELSE 'Over $100'
    END as price_range,
    COUNT(*) as count,
    AVG(price_percent_change) as avg_percent_change,
    date as analysis_date
FROM {{ ref('int_daily_combined') }}
GROUP BY price_range, date
