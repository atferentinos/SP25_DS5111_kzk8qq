{{ config(
    materialized='table'
) }}

WITH wsj_data AS (
    SELECT
        "Symbol" as symbol,
        "Name" as name,
        "Price" as price,
        "Change" as change,
       [ "Change %"] as change_percent,
        'Wall Street Journal' as source,
        "Timestamp" as timestamp
    FROM {{ source('raw', 'wsjgainers_norm') }}
),

yahoo_data AS (
    SELECT
        "Symbol" as symbol,
        "Name" as name,
        "Price" as price,
        "Change" as change,
       [ "Change %"] as change_percent,
        'Yahoo Finance' as source,
        "Timestamp" as timestamp
    FROM {{ source('raw', 'ygainers_norm') }}
),

combined_data AS (
    SELECT * FROM wsj_data
    UNION ALL
    SELECT * FROM yahoo_data
)

SELECT
    symbol,
    name,
    price,
    change,
    change_percent,
    source,
    timestamp,
    DATE(timestamp) AS date,
    DAYNAME(DATE(timestamp)) AS day_of_week
FROM combined_data
