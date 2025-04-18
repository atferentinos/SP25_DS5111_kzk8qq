{{ config(
    materialized='table'
) }}
-- Combine all the gainers data from various sources and dates
-- WSJ Gainers
SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250307_165202_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250307_165602_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250307_185502_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250310_154613_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250310_163102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250310_173002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250310_191246_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250310_200420_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250311_093102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250311_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250311_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250311_163102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250312_093102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250312_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250312_160102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250312_163102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-13') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250313_093102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-13') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250313_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-13') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250313_160102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-13') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250313_163101_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-14') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250314_093103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-14') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250314_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-14') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250314_160102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-14') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250314_163101_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-15') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250315_163102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-16') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250316_163102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-17') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250317_093102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-17') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250317_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-17') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250317_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-17') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250317_163102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-18') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250318_093102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-18') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250318_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-18') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250318_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-18') as date,
    'WSJ' as source
FROM {{ source('snowflake_tables', 'WSJGAINERS_NORM_20250318_163102_NORM') }}

UNION ALL

-- Yahoo gainers data
SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-06') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250306_012908_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-06') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250306_174044_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250307_165203_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250307_165402_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250307_165603_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250307_185503_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250310_154600_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250310_163003_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250310_173002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250310_191235_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250310_200410_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250311_093102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250311_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250311_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250311_163002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250312_093103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250312_123003_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250312_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250312_163002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-13') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250313_123003_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-13') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250313_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-13') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250313_163002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-14') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250314_093103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-14') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250314_123003_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-14') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250314_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-14') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250314_163002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-15') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250315_163002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-16') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250316_163002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-17') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250317_093102_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-17') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250317_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-17') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250317_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-17') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250317_163002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-18') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250318_093103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-18') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250318_123002_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-18') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250318_160103_NORM') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-18') as date,
    'Yahoo' as source
FROM {{ source('snowflake_tables', 'YGAINERS_NORM_20250318_163002_NORM') }}
