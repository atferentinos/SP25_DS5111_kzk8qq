{{ config(
    materialized='table'
) }}

-- This simple model bypasses the problematic column
SELECT
    "Symbol" as symbol,
    "Name" as name,
    "Price" as price,
    "Change" as change,
    'Wall Street Journal' as source,
    "Timestamp" as timestamp
FROM {{ source('raw', 'wsjgainers_norm') }}
LIMIT 10
