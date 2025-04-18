{{ config(
    materialized='table'
) }}
-- Combine all the gainers data from various sources and dates
SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250307_165202_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250307_165602_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250307_185502_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250310_154613_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250310_163102_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250310_173002_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250310_191246_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250310_200420_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250311_093102_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250311_123002_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250311_160103_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250311_163102_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250312_093102_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250312_123002_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'WSJ' as source
FROM {{ ref('wsjgainers_norm_20250312_160102_norm') }}

UNION ALL

-- Yahoo gainers data
SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-06') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250306_174044_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250307_165203_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250307_165402_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250307_165503_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-07') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250307_185503_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250310_154600_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250310_163003_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250310_173002_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250310_191235_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-10') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250310_200410_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250311_093102_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250311_123002_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250311_160103_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-11') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250311_163002_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250312_093103_norm') }}

UNION ALL

SELECT 
    symbol,
    price,
    price_change,
    price_percent_change,
    TO_DATE('2025-03-12') as date,
    'Yahoo' as source
FROM {{ ref('ygainers_norm_20250312_123003_norm') }}
