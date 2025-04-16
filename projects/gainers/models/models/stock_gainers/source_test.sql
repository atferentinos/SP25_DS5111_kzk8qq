{{ config(
    materialized='table'
) }}


SELECT COUNT(*) as row_count
FROM {{ source('raw', 'wsjgainers_norm') }}
