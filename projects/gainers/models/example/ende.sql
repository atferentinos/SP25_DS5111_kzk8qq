{{ config(materialized='table') }}

SELECT EN,DE 
FROM DATA_SCIENCE.KZK8QQ_RAW.NUMBERS
