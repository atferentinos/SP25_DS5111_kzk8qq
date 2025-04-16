{{ config(
    materialized='table'
) }}


SELECT
    vd.volume_range,
    vd.avg_change_percent,
    -- This would be calculated with actual correlation in a real implementation
    -- For now, using a simplified approximation
    CASE
        WHEN vd.avg_change_percent > 6 THEN 0.8
        WHEN vd.avg_change_percent > 4 THEN 0.6
        ELSE 0.4
    END AS price_correlation,
    -- Liquidity score based on volume range
    CASE
        WHEN vd.volume_range = 'Very High Volume (>1M)' THEN 0.9
        WHEN vd.volume_range = 'High Volume (500K-1M)' THEN 0.7
        WHEN vd.volume_range = 'Medium Volume (100K-500K)' THEN 0.5
        WHEN vd.volume_range = 'Low Volume (<100K)' THEN 0.3
        ELSE 0.1
    END AS liquidity_score,
    -- Trading recommendation based on volume and price change
    CASE
        WHEN vd.avg_change_percent > 5 AND 
             vd.volume_range IN ('High Volume (500K-1M)', 'Very High Volume (>1M)')
        THEN 'Strong Buy Signal'
        WHEN vd.avg_change_percent > 4 AND 
             vd.volume_range IN ('Medium Volume (100K-500K)', 'High Volume (500K-1M)')
        THEN 'Buy Signal'
        WHEN vd.avg_change_percent > 3
        THEN 'Watch Closely'
        ELSE 'Monitor'
    END AS trading_recommendation
FROM {{ ref('int_volume_distribution') }} vd
