{{ config(
    materialized='table'
) }}

-- Simplest possible model
SELECT 1 as test_column
